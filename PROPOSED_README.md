# ✨ CineSense: Your Personal Movie Recommender ✨

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App/ci.yml?branch=main&style=flat-square)](https://github.com/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App/actions/workflows/ci.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg?style=flat-square)](https://www.streamlit.io/)

**CineSense** is a smart, intuitive movie recommendation web app built with Streamlit. It leverages the power of cosine similarity on implicit user ratings to deliver personalized movie suggestions in an instant.

## 🚀 Core Features

-   🎬 **Personalized Suggestions:** Get movie recommendations that are tailored to your unique taste.
-   ⚡ **High-Speed Data Loading:** Utilizes the Apache Feather format for near-instant data loading.
-   🐳 **Dockerized for Portability:** Easily deploy the application in any environment with Docker.
-   🎨 **Modern & Interactive UI:** A clean and user-friendly interface powered by Streamlit.

## 🛠️ Getting Started

### Prerequisites

-   Python 3.9 or higher
-   Pip and a virtual environment tool (e.g., `venv`)

### Installation & Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chirag127/CineSense-Movie-Recommendation-Streamlit-Web-App.git
    cd CineSense-Movie-Recommendation-Streamlit-Web-App
    ```

2.  **Set up and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the application:**
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

```
.
├── .github/              # GitHub Actions, issue templates, etc.
├── data/                 # Datasets and pickled files.
├── src/                  # Source code for the application.
│   ├── data/             # Data preprocessing logic.
│   └── recommend/        # Recommendation engine.
├── tests/                # Unit and integration tests.
├── .gitignore            # Files and directories to be ignored by Git.
├── AGENTS.md             # Instructions for AI agents.
├── app.py                # The main Streamlit application file.
├── CONTRIBUTING.md       # Guidelines for contributing to the project.
├── Dockerfile            # Docker configuration for the application.
├── LICENSE               # The license for the project.
├── pyproject.toml        # Project metadata and dependencies.
├── README.md             # The main README file.
└── run.py                # A simple runner script for the application.
```

## 💖 Contributing

We welcome contributions! If you'd like to help improve CineSense, please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](LICENSE) file for more details.

---

### ⭐ Show Your Support

If you love this project, please give it a star on GitHub! It helps a lot!
