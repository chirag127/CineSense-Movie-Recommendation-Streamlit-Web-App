# CineSense-Movie-Recommendation-Streamlit-Web-App

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App/ci.yml?branch=main&style=flat-square)](https://github.com/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App/actions/workflows/ci.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg?style=flat-square)](https://www.streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-supported-blue.svg?style=flat-square)](https://www.docker.com/)

CineSense delivers personalized movie suggestions via a Streamlit web interface, leveraging cosine similarity on implicit ratings.

## ✨ Features

-   :clapper: **Personalized Recommendations:** Get movie suggestions tailored to your taste.
-   :rocket: **Fast and Efficient:** Uses `feather` for quick data loading.
-   :whale: **Dockerized:** Easy to deploy with Docker.
-   :art: **User-Friendly Interface:** Built with Streamlit for a smooth user experience.

## 🚀 Installation and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App.git
    cd CineSense-Movie-Recommendation-Streamlit-Web-App
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python run.py
    ```

## 🏗️ Architecture Tree

```
.
├── .github
│   ├── ISSUE_TEMPLATE
│   │   └── bug_report.md
│   ├── workflows
│   │   └── ci.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── badges.yml
├── data
│   ├── movie_list.pickle
│   ├── netflix_dataset.csv
│   └── tfidf_data.feather
├── src
│   ├── data
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   └── recommend
│       ├── __init__.py
│       └── recommend.py
├── tests
│   ├── __init__.py
│   ├── test_data.py
│   └── test_recommend.py
├── .dockerignore
├── .gitignore
├── AGENTS.md
├── app.py
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── notebook.ipynb
├── PROPOSED_README.md
├── pyproject.toml
├── README.md
├── requirements.txt
├── ruff.toml
└── run.py
```

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## 📄 License

This project is licensed under the [CC BY-NC 4.0 License](LICENSE).

---

## ⭐ Star This Repo

If you find this project useful, please consider giving it a star!
