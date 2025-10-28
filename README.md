# TexttoSpeech-
Group Project

Setup & Run
# 1️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# 2️⃣ Install dependencies
pip install flask pyttsx3 pypiwin32

# 3️⃣ Run the Flask app
python app.py


Then open in browser:
👉 http://127.0.0.1:5000

🧠 Features

Convert text to speech using pyttsx3

Select from English, German, Japanese, or Italian

Adjust voice speed and volume

Buttons: Speak, Stop, and Reset

📁 Folder Structure
TexttoSpeech/
│
├── app.py
├── templates/
│   └── frontend/
│       └── index.html
└── static/
    ├── javascript/
    │   └── button1.js
    └── audio/
