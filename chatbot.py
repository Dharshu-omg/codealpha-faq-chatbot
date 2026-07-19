import json
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer
nltk.download('punkt_tab')

# Load FAQ data
with open("faq_data.json", "r") as file:
    data = json.load(file)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Create TF-IDF model
vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_input):
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, question_vectors)
    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score < 0.2:
        return "Sorry, I couldn't find a matching answer."

    return answers[best_match]