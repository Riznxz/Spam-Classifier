# Spam Classifier - ML & NLP Flask Application

A modern, responsive web application for spam classification using Machine Learning and Natural Language Processing techniques.

## Features

- **Real-time Text Classification**: Instantly classify text as spam or legitimate
- **Advanced ML Algorithms**: Uses Multinomial Naive Bayes with TF-IDF vectorization
- **NLP Preprocessing**: Text preprocessing with lemmatization and stop word removal
- **Modern UI**: Beautiful, responsive design with gradient backgrounds and animations
- **Custom Training**: Train the model with your own dataset
- **Confidence Scores**: Get detailed probability distributions and confidence levels
- **Sample Examples**: Pre-loaded examples to test the system

## Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, NLTK
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Modern CSS with gradients, animations, and responsive design
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd spam_classifier
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

### Text Classification
1. Enter or paste text in the "Text Classification" section
2. Click "Classify Text" to get instant results
3. View the classification result with confidence scores
4. Try the sample examples provided

### Model Training
1. In the "Model Training" section, enter your training texts (one per line)
2. Enter corresponding labels (0 for ham/legitimate, 1 for spam, comma-separated)
3. Click "Train Model" to improve the classifier with your data
4. Minimum 10 samples required for training

## API Endpoints

- `GET /` - Main application page
- `POST /classify` - Classify text as spam/not spam
- `POST /train` - Train the model with custom data
- `GET /stats` - Get model statistics

## Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: 5000 most frequent words
- **Preprocessing**: 
  - Lowercase conversion
  - Special character removal
  - Tokenization
  - Stop word removal
  - Lemmatization

## Sample Data

The application comes pre-trained with sample spam and legitimate messages. You can replace this with your own dataset for better performance.

## Customization

### Adding More Training Data
Edit the `sample_data` dictionary in `app.py` to include more training examples:

```python
sample_data = {
    'text': [
        "Your spam message here",
        "Your legitimate message here",
        # ... more examples
    ],
    'label': [1, 0, ...]  # 1 for spam, 0 for legitimate
}
```

### Modifying the Model
You can experiment with different algorithms by changing the classifier in the `SpamClassifier` class:

```python
from sklearn.linear_model import LogisticRegression
# or
from sklearn.svm import SVC
# or
from sklearn.ensemble import RandomForestClassifier

self.classifier = LogisticRegression()  # or other classifier
```

## File Structure

```
spam_classifier/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # Main UI template
```

## Performance

- **Training Time**: ~1-2 seconds for 1000 samples
- **Classification Time**: <100ms per text
- **Memory Usage**: ~50MB for the model
- **Accuracy**: Varies based on training data quality

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Contributing

Feel free to contribute to this project by:
- Adding new ML algorithms
- Improving the UI/UX
- Adding more preprocessing techniques
- Enhancing the API endpoints

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please check the console for error messages or create an issue in the project repository.

---

**Note**: This is a demonstration application. For production use, consider:
- Adding authentication
- Implementing rate limiting
- Using a production WSGI server (Gunicorn)
- Adding logging and monitoring
- Implementing proper error handling
- Using environment variables for configuration 