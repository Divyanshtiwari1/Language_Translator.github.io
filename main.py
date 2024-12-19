from flask import Flask, render_template, request
from googletrans import Translator

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
    app.run(debug=True)
