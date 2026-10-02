# CyberShield AI Cybersecurity Chatbot

##Overview

CyberShield is an educational AI-powered cybersecurity assistant developed using Python, Streamlit, Ollama, and TinyLlama.

The application provides a conversational interface for learning basic cybersecurity and networking concepts along with several basic security analysis utilities.

## Features

* AI-powered cybersecurity chatbot
* Password strength checker
* Hash generator
* URL analyzer
* Base64 encoder and decoder
* Local AI model using Ollama and TinyLlama
* Streamlit-based web interface

## Technologies Used

* Python
* Streamlit
* Ollama
* TinyLlama
* Kali Linux
* Git
* GitHub

## Project Structure

```text
CyberShield-AI-Chatbot/
│
├── app.py
├── chatbot/
│   ├── __init__.py
│   └── assistant.py
│
├── security_tools/
│   ├── __init__.py
│   ├── encoding_tool.py
│   ├── hash_tool.py
│   ├── password_checker.py
│   └── url_checker.py
│
├── screenshots/
│   ├── dashboard.png
│   └── chatbot.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aishwarya7030/CyberShield-AI-Chatbot.git
cd CyberShield-AI-Chatbot
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Ollama Setup

Install Ollama and download the TinyLlama model:

```bash
ollama pull tinyllama
```

Make sure Ollama is running before starting the application.

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

## Security Tools

### Password Strength Checker

Performs basic password complexity checks based on:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### Hash Generator

Generates hashes using:

* MD5
* SHA1
* SHA256

### URL Analyzer

Performs basic URL analysis and identifies simple indicators such as:

* Non-HTTPS URLs
* The `@` character in URLs
* Unusually long URLs
* Hyphens in domain names

### Base64 Encoder and Decoder

Provides basic Base64 encoding and decoding functionality.

## Screenshots

### Application Dashboard

![CyberShield Dashboard](screenshots/dashboard.png)

### AI Cybersecurity Chatbot

![CyberShield Chatbot](screenshots/chatbot.png)

## Purpose

This project was developed for cybersecurity learning, Python development, and defensive security education.

It demonstrates the integration of a local AI model with basic cybersecurity utilities in a web-based application.

## Disclaimer

This project is intended for educational and defensive security purposes only.

The security checks provided by this application are basic indicators and should not be considered a complete security assessment.

## Author

**Aishwarya Kognure**

Cybersecurity | Ethical Hacking | VAPT | Digital Forensics

