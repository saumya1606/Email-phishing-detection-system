
# Email Spam Detection and Phishing URL Classification

A BTech/college mini-project that combines Machine Learning, NLP, Cybersecurity, and Flask.

## Features

- Email Spam / Ham classification
- Phishing / Safe URL classification
- TF-IDF + Logistic Regression for email text
- Hand-crafted URL features + Random Forest for URL classification
- Confidence score
- Model evaluation:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

## Project Structure

email_spam_phishing_project/
├── app.py
├── train_models.py
├── requirements.txt
├── README.md
├── data/
│   ├── spam_sample.csv
│   └── url_sample.csv
├── models/
├── templates/
│   └── index.html
└── static/
    └── style.css

## Installation

Open terminal in the project folder:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Train Models

```bash
python train_models.py
```

This creates:

- models/spam_model.pkl
- models/spam_vectorizer.pkl
- models/url_model.pkl

## Run Website

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Dataset Format

### Spam dataset

CSV columns:

- text
- label

Where:

- 0 = Ham / Not Spam
- 1 = Spam

### URL dataset

CSV columns:

- url
- label

Where:

- 0 = Safe
- 1 = Phishing

## Important

The included datasets are intentionally small sample datasets so that the project runs immediately.
For a final-year/mini-project demonstration, replace them with larger real-world datasets.

Recommended sources:
- SMS Spam Collection / email spam datasets from Kaggle or UCI
- Phishing URLs from PhishTank, OpenPhish, Kaggle, or academic datasets

## Future Improvements

- Add email subject and sender analysis
- Detect HTML links inside email
- Add blacklist/reputation lookup
- Add domain age / WHOIS features
- Add HTTPS certificate analysis
- Add SQLite history
- Add user login
- Add model comparison
- Deploy on Render, Railway, or PythonAnywhere


## Python 3.14.5

This version is prepared for Python 3.14.5. Pandas 2.3.3 is the first generally compatible pandas release for Python 3.14, while scikit-learn 1.7+ supports modern Python versions.

Check your version:
```bash
python --version
```
Expected: `Python 3.14.5`

For Windows, create a fresh virtual environment before installing packages:
```bash
py -3.14 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python train_models.py
python app.py
```
