# 🚀 Spam Classifier - ML & NLP Flask Application

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-brightgreen.svg)](https://github.com/Riznxz/Spam-Classifier)

A modern, responsive web application for spam classification using Machine Learning and Natural Language Processing techniques. Built with Flask, scikit-learn, and NLTK.

## ✨ Features

- 🔍 **Real-time Text Classification**: Instantly classify text as spam or legitimate
- 🤖 **Advanced ML Algorithms**: Uses Multinomial Naive Bayes with TF-IDF vectorization
- 📝 **NLP Preprocessing**: Text preprocessing with lemmatization and stop word removal
- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds and animations
- 🎯 **Custom Training**: Train the model with your own dataset
- 📊 **Confidence Scores**: Get detailed probability distributions and confidence levels
- 📋 **Sample Examples**: Pre-loaded examples to test the system
- 📱 **Mobile Responsive**: Works perfectly on all devices

## 🛠️ Technology Stack

### Backend
- **Flask** - Web framework
- **scikit-learn** - Machine learning algorithms
- **NLTK** - Natural language processing
- **NumPy/Pandas** - Data manipulation

### Frontend
- **HTML5** - Structure
- **CSS3** - Modern styling with gradients and animations
- **JavaScript** - Interactive functionality
- **Font Awesome** - Icons
- **Google Fonts** - Typography

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Riznxz/Spam-Classifier.git
   cd Spam-Classifier
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

### Alternative: One-Click Setup

**Windows:**
```bash
run.bat
```

**Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

## 📖 Usage

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

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/classify` | POST | Classify text as spam/not spam |
| `/train` | POST | Train the model with custom data |
| `/stats` | GET | Get model statistics |

### API Usage Examples

**Classify Text:**
```bash
curl -X POST http://localhost:5000/classify \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to classify"}'
```

**Train Model:**
```bash
curl -X POST http://localhost:5000/train \
  -H "Content-Type: application/json" \
  -d '{"texts": ["text1", "text2"], "labels": [0, 1]}'
```

## 🤖 Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: 5000 most frequent words
- **Preprocessing**: 
  - Lowercase conversion
  - Special character removal
  - Tokenization
  - Stop word removal
  - Lemmatization

## 📁 Project Structure

```
spam_classifier/
├── app.py                 # Main Flask application with ML logic
├── run.py                 # Python script to run the application
├── run.bat                # Windows batch file for easy execution
├── run.sh                 # Unix/Linux/macOS shell script
├── requirements.txt       # Python dependencies
├── README.md             # Comprehensive documentation
├── PROJECT_STRUCTURE.md  # Detailed project structure
└── templates/
    └── index.html        # Modern, responsive UI template
```

## ⚡ Performance

- **Training Time**: ~1-2 seconds for 1000 samples
- **Classification Time**: <100ms per text
- **Memory Usage**: ~50MB for the model
- **Accuracy**: Varies based on training data quality

## 🎨 Screenshots

*[Add screenshots of your application here]*

## 🔧 Customization

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

## 🌐 Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Adding new ML algorithms
- Improving the UI/UX
- Adding more preprocessing techniques
- Enhancing the API endpoints
- Adding unit tests
- Improving documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- None currently reported

## 🔮 Future Enhancements

- [ ] Add support for multiple languages
- [ ] Implement deep learning models
- [ ] Add email integration
- [ ] Create mobile app version
- [ ] Add user authentication
- [ ] Implement model versioning

## 📞 Support

If you encounter any issues or have questions:

1. Check the console for error messages
2. Review the [Issues](https://github.com/Riznxz/Spam-Classifier/issues) page
3. Create a new issue with detailed information
4. Contact: riznxz@gmail.com

## 🙏 Acknowledgments

- [scikit-learn](https://scikit-learn.org/) for machine learning algorithms
- [NLTK](https://www.nltk.org/) for natural language processing
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Font Awesome](https://fontawesome.com/) for icons

---

**Note**: This is a demonstration application. For production use, consider:
- Adding authentication
- Implementing rate limiting
- Using a production WSGI server (Gunicorn)
- Adding logging and monitoring
- Implementing proper error handling
- Using environment variables for configuration

---

⭐ **Star this repository if you found it helpful!** 