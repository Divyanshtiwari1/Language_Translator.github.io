from flask import Flask, render_template, request
from googletrans import Translator
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    source_lang = request.form.get("sourceLang")
    target_lang = request.form.get("targetLang")
    text = request.form.get("text")

    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)

    return render_template("index.html", translated_text=translated.text)

if __name__ == "__main__":
    # Use the PORT environment variable for deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
