from flask import Blueprint, render_template, request, jsonify
from .models import Translation, db
from .utils import translate_text

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/translate', methods=['POST'])
def translate():
    data = request.json
    input_text = data['input_text']
    source_lang = data['source_language']
    target_lang = data['target_language']

    translated_text = translate_text(input_text, source_lang, target_lang)

    new_translation = Translation(
        input_text=input_text,
        source_language=source_lang,
        target_language=target_lang,
        translated_text=translated_text
    )
    db.session.add(new_translation)
    db.session.commit()

    return jsonify({'translated_text': translated_text})
