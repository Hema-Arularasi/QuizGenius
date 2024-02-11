# Install Flask using: pip install Flask
# Install spaCy using: pip install spacy
# Download the English model using: python -m spacy download en_core_web_sm

from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('quizgenius.html')

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.get_json()
    content = data['content']
    num_questions = data['num_questions']

    # Process the educational content using spaCy
    doc = nlp(content)

    # Extract meaningful words for quiz questions
    meaningful_words = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # Select random words for quiz questions
    selected_words = meaningful_words[:min(num_questions, len(meaningful_words))]

    # Create quiz questions
    questions = [{'id': i + 1, 'word': word} for i, word in enumerate(selected_words)]

    return jsonify({'questions': questions})

if __name__ == '__main__':
    app.run(debug=True)
