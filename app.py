from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)
OUTPUT_FILE = "static/output.mp3"


@app.route('/')
def index():
    return render_template("frontend/index.html")

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


@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')
    lang = data.get('lang', 'en')

    if not text.strip():
        return jsonify({"error": "Text cannot be empty"}), 400

    try:
        # Generate speech file
        tts = gTTS(text=text, lang=lang)
        tts.save(OUTPUT_FILE)
        return jsonify({"status": "success", "file": "/" + OUTPUT_FILE})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/stop', methods=['POST'])
def stop():
    # Simulate stop by deleting audio file
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    return jsonify({"status": "Speech stopped"})


@app.route('/reset', methods=['POST'])
def reset():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    return jsonify({"status": "System reset"})


if __name__ == '__main__':
    app.run(debug=True)
