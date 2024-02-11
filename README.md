Overview
QuizGenius with NLTK is a simple tool for generating quiz 
questions based on educational content using the Natural Language 
Toolkit (NLTK) library. It randomly selects sentences, preprocesses the text,
and creates questions about the meaning of specific words.
Features
Randomly generates quiz questions based on educational content.
Utilizes NLTK for text processing, tokenization, and stemming.
Provides a simple and customizable interface for generating quiz questions.
Prerequisites
Python (3.6 or higher)
NLTK
Gensim
Installation:
pip install nltk
pip install gensim
Usage:
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import random
Download NLTK resources:
nltk.download('punkt')
nltk.download('stopwords')
Example Usage:
educational_content = """
Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language. It involves the development of algorithms and models to enable computers to understand, interpret, and generate human-like text.
"""

quiz_questions = generate_quiz_questions(educational_content, num_questions=3)
for i, question in enumerate(quiz_questions, start=1):
    print(f"Question {i}: {question}")
Acknowledgments
NLTK
Gensim
