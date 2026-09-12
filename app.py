
from flask import Flask, render_template, request
import joblib
import os
import re
from urllib.parse import urlparse

app = Flask(__name__)

MODEL_DIR = "models"
SPAM_MODEL = os.path.join(MODEL_DIR, "spam_model.pkl")
SPAM_VECTORIZER = os.path.join(MODEL_DIR, "spam_vectorizer.pkl")
URL_MODEL = os.path.join(MODEL_DIR, "url_model.pkl")

def load_models():
    spam_model = joblib.load(SPAM_MODEL)
    spam_vectorizer = joblib.load(SPAM_VECTORIZER)
    url_model = joblib.load(URL_MODEL)
    return spam_model, spam_vectorizer, url_model

def extract_url_features(url):
    if not url.startswith(("http://", "https://")):
        parsed_url = "http://" + url
    else:
        parsed_url = url

    parsed = urlparse(parsed_url)
    hostname = parsed.hostname or ""

    suspicious_words = [
        "login", "verify", "secure", "account", "update", "bank",
        "signin", "confirm", "password", "free", "bonus", "payment"
    ]

    features = {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "count_dot": url.count("."),
        "count_hyphen": url.count("-"),
        "count_at": url.count("@"),
        "count_question": url.count("?"),
        "count_equal": url.count("="),
        "count_underscore": url.count("_"),
        "count_slash": url.count("/"),
        "count_digits": sum(ch.isdigit() for ch in url),
        "https": int(url.lower().startswith("https://")),
        "has_ip": int(bool(re.search(r'(\d{1,3}\.){3}\d{1,3}', hostname))),
        "suspicious_words": sum(word in url.lower() for word in suspicious_words),
        "subdomain_count": max(0, hostname.count(".") - 1),
    }
    return list(features.values())

@app.route("/", methods=["GET", "POST"])
def index():
    spam_result = None
    spam_confidence = None
    url_result = None
    url_confidence = None

    if request.method == "POST":
        spam_model, spam_vectorizer, url_model = load_models()

        action = request.form.get("action")

        if action == "spam":
            email_text = request.form.get("email_text", "").strip()
            if email_text:
                X = spam_vectorizer.transform([email_text])
                pred = spam_model.predict(X)[0]
                probs = spam_model.predict_proba(X)[0]
                spam_result = "Spam" if pred == 1 else "Not Spam (Ham)"
                spam_confidence = round(float(max(probs)) * 100, 2)

        elif action == "url":
            url = request.form.get("url_text", "").strip()
            if url:
                features = [extract_url_features(url)]
                pred = url_model.predict(features)[0]
                probs = url_model.predict_proba(features)[0]
                url_result = "Phishing / Malicious" if pred == 1 else "Safe / Legitimate"
                url_confidence = round(float(max(probs)) * 100, 2)

    return render_template(
        "index.html",
        spam_result=spam_result,
        spam_confidence=spam_confidence,
        url_result=url_result,
        url_confidence=url_confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
