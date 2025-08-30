from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize text preprocessing components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

class SpamClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        self.classifier = MultinomialNB()
        self.is_trained = False
        
    def preprocess_text(self, text):
        """Preprocess text for classification"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        words = nltk.word_tokenize(text)
        
        # Remove stopwords and lemmatize
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        
        return ' '.join(words)
    
    def train_model(self, data):
        """Train the spam classifier"""
        # Preprocess all texts
        processed_texts = [self.preprocess_text(text) for text in data['text']]
        
        # Vectorize the text
        X = self.vectorizer.fit_transform(processed_texts)
        y = data['label']
        
        # Train the classifier
        self.classifier.fit(X, y)
        self.is_trained = True
        
        # Calculate accuracy
        y_pred = self.classifier.predict(X)
        accuracy = accuracy_score(y, y_pred)
        
        return accuracy
    
    def predict(self, text):
        """Predict if text is spam or not"""
        if not self.is_trained:
            return "Model not trained"
        
        # Preprocess the text
        processed_text = self.preprocess_text(text)
        
        # Vectorize
        X = self.vectorizer.transform([processed_text])
        
        # Predict
        prediction = self.classifier.predict(X)[0]
        probability = self.classifier.predict_proba(X)[0]
        
        return {
            'prediction': 'Spam' if prediction == 1 else 'Not Spam',
            'confidence': max(probability) * 100,
            'spam_probability': probability[1] * 100,
            'ham_probability': probability[0] * 100
        }

# Initialize the classifier
classifier = SpamClassifier()

# Sample training data (you can replace this with your own dataset)
sample_data = {
    'text': [
        "URGENT! You have won a 1 week FREE membership in our £100,000 prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net",
        "Hi Tom, how are you doing?",
        "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply",
        "Hello! How was your weekend?",
        "URGENT! Your Mobile No. was awarded £200 Bonus Caller Prize on 1/08. This is our 2nd attempt to contact YOU! Call 09066362231 ASAP! Box97N7QP, 150ppm",
        "Hi there, just checking in to see how you're doing.",
        "FREE RINGTONE text FIRST to 87131 for a poly or text GET to 87131 for a true tone! Help? 0845 2814032 16 after 1st free, tones are 3£",
        "Good morning! Have a great day ahead.",
        "URGENT! You have won a 1 week FREE membership in our £100,000 prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net",
        "Thanks for the update, I'll get back to you soon."
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 for spam, 0 for ham
}

# Train the model on startup
if not classifier.is_trained:
    accuracy = classifier.train_model(sample_data)
    print(f"Model trained with accuracy: {accuracy:.2f}")

@app.route('/')
def index():
    """Main page with modern UI"""
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_text():
    """API endpoint for text classification"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({'error': 'Please provide some text to classify'}), 400
        
        result = classifier.predict(text)
        
        return jsonify({
            'success': True,
            'result': result,
            'text': text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train_model():
    """API endpoint for training the model with custom data"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        labels = data.get('labels', [])
        
        if len(texts) != len(labels):
            return jsonify({'error': 'Number of texts and labels must match'}), 400
        
        if len(texts) < 10:
            return jsonify({'error': 'Please provide at least 10 samples for training'}), 400
        
        training_data = {'text': texts, 'label': labels}
        accuracy = classifier.train_model(training_data)
        
        return jsonify({
            'success': True,
            'accuracy': accuracy,
            'message': f'Model trained successfully with {len(texts)} samples'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stats')
def get_stats():
    """Get model statistics"""
    return jsonify({
        'is_trained': classifier.is_trained,
        'model_type': 'Multinomial Naive Bayes',
        'vectorizer': 'TF-IDF',
        'features': 5000
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 