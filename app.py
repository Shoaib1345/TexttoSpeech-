from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
import pyttsx3

app = Flask(__name__)
OUTPUT_FILE = "static/output.mp3"

@app.route('/')
def index():
    return render_template("frontend/index.html")

# ✅ API Model Page (Google TTS)
@app.route('/api_model')
def api_model():
    return render_template("frontend/pyttsx.html")  # agar tumhara API model page ka naam api.html hai

# ✅ Pyttsx Model Page
@app.route('/pyttsx_model')
def pyttsx_model():
    return render_template("frontend/pyttsx_2.html")  # ye tumhara Pyttsx wala page

# ✅ gTTS Speak
@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')
    lang = data.get('lang', 'en')
    if not text.strip():
        return jsonify({"error": "Text cannot be empty"}), 400
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(OUTPUT_FILE)
        return jsonify({"status": "success", "file": "/" + OUTPUT_FILE})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Pyttsx Speak
@app.route('/speak_pyttsx', methods=['POST'])
def speak_pyttsx():
    data = request.get_json()
    text = data.get('text', '')
    rate = data.get('rate', 200)
    volume = data.get('volume', 1.0)
    if not text.strip():
        return jsonify({"error": "Text cannot be empty"}), 400
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.save_to_file(text, OUTPUT_FILE)
        engine.runAndWait()
        return jsonify({"status": "success", "file": "/" + OUTPUT_FILE})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
