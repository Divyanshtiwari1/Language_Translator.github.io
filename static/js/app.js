async function translate() {
    const inputText = document.getElementById('input-text').value;
    const sourceLang = document.getElementById('source-lang').value;
    const targetLang = document.getElementById('target-lang').value;

    const response = await fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            input_text: inputText,
            source_language: sourceLang,
            target_language: targetLang
        })
    });
    const data = await response.json();
    document.getElementById('output').innerText = data.translated_text;
}
