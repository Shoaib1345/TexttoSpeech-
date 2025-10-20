from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Corrected 'render_tempate' → 'render_template'
    return render_template("frontend/index.html")

if __name__ == '__main__':
    app.run()
