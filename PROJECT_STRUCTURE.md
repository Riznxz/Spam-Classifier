# Project Structure

```
spam_classifier/
├── app.py                 # Main Flask application with ML logic
├── run.py                 # Python script to run the application
├── run.bat                # Windows batch file for easy execution
├── run.sh                 # Unix/Linux/macOS shell script
├── requirements.txt       # Python dependencies
├── README.md             # Comprehensive documentation
├── PROJECT_STRUCTURE.md  # This file
└── templates/
    └── index.html        # Modern, responsive UI template
```

## File Descriptions

### Core Application Files

- **`app.py`**: The main Flask application containing:
  - SpamClassifier class with ML/NLP functionality
  - Flask routes for API endpoints
  - Text preprocessing with NLTK
  - TF-IDF vectorization and Naive Bayes classification
  - Sample training data

- **`run.py`**: Helper script that:
  - Checks Python version compatibility
  - Verifies all dependencies are installed
  - Downloads required NLTK data
  - Starts the Flask application with proper error handling

### Execution Scripts

- **`run.bat`**: Windows batch file for easy execution
  - Automatically creates virtual environment
  - Installs dependencies
  - Runs the application

- **`run.sh`**: Unix/Linux/macOS shell script
  - Same functionality as run.bat but for Unix systems
  - Automatically executable

### Configuration & Documentation

- **`requirements.txt`**: Lists all Python package dependencies
- **`README.md`**: Comprehensive documentation including:
  - Installation instructions
  - Usage guide
  - API documentation
  - Customization options
  - Troubleshooting

### Frontend

- **`templates/index.html`**: Modern, responsive web interface featuring:
  - Beautiful gradient design
  - Real-time text classification
  - Interactive model training
  - Confidence score visualization
  - Sample examples
  - Mobile-responsive layout

## Key Features by File

### ML/NLP Features (app.py)
- Text preprocessing (lowercase, tokenization, lemmatization)
- Stop word removal
- TF-IDF vectorization
- Multinomial Naive Bayes classification
- Confidence scoring
- Custom model training

### UI Features (templates/index.html)
- Modern gradient design
- Real-time classification
- Interactive training interface
- Animated confidence bars
- Responsive layout
- Sample text examples
- Error handling and notifications

### Automation Features (run scripts)
- Dependency checking
- Virtual environment management
- NLTK data download
- Cross-platform compatibility
- Error handling and user feedback

## Technology Stack

### Backend
- **Flask**: Web framework
- **scikit-learn**: Machine learning algorithms
- **NLTK**: Natural language processing
- **NumPy/Pandas**: Data manipulation

### Frontend
- **HTML5**: Structure
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### Development Tools
- **Virtual Environment**: Dependency isolation
- **Requirements.txt**: Package management
- **Cross-platform Scripts**: Easy deployment

## API Endpoints

All endpoints are defined in `app.py`:

- `GET /`: Main application page
- `POST /classify`: Text classification endpoint
- `POST /train`: Model training endpoint
- `GET /stats`: Model statistics endpoint

## Data Flow

1. **User Input** → `templates/index.html` (JavaScript)
2. **API Request** → `app.py` (Flask routes)
3. **Text Processing** → `app.py` (NLTK preprocessing)
4. **ML Classification** → `app.py` (scikit-learn)
5. **Response** → `templates/index.html` (Display results)

## Customization Points

### Model Customization
- Change classifier in `SpamClassifier` class
- Modify preprocessing in `preprocess_text` method
- Adjust TF-IDF parameters in vectorizer

### UI Customization
- Modify CSS styles in `templates/index.html`
- Add new features in JavaScript section
- Update color schemes and animations

### Data Customization
- Replace sample data in `app.py`
- Add new training examples
- Modify preprocessing rules 