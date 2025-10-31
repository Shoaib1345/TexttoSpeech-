from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
import pyttsx3

app = Flask(__name__)
OUTPUT_FILE = "static/output.mp3"

@app.route('/')
def index():
    return render_template("frontend/index.html")

@app.route('/about')
def about():
    return render_template("frontend/about.html")

@app.route('/api_model')
def api_model():
    # Renders the specific page for the Pyttsx model
    return render_template("frontend/api_model.html")

@app.route('/pyttsx_model')
def pyttsx_model():
    # Renders the Pyttsx model page (UI only)
    return render_template("frontend/pyttsx_model.html")

@app.route('/trained_model')
def trained_model():
    # Renders the Trained model page (UI only)
    return render_template("frontend/trained_model.html")


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

# ✅ Stop Speech Route
@app.route('/stop', methods=['POST'])
def stop():
    try:
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
        return jsonify({"status": "Speech stopped"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Reset System Route
@app.route('/reset', methods=['POST'])
def reset():
    try:
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
        return jsonify({"status": "System reset"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
