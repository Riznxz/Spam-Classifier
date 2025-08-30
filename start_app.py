#!/usr/bin/env python3
"""
Simple startup script for the Spam Classifier Flask application
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Import required packages
    import flask
    import sklearn
    import numpy
    import pandas
    import nltk
    import joblib
    
    print("✅ All required packages are available")
    
    # Download NLTK data if needed
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("📥 Downloading NLTK punkt...")
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("📥 Downloading NLTK stopwords...")
        nltk.download('stopwords', quiet=True)
    
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        print("📥 Downloading NLTK wordnet...")
        nltk.download('wordnet', quiet=True)
    
    print("✅ NLTK data ready")
    
    # Import and start the Flask app
    from app import app
    
    print("🚀 Starting Spam Classifier Application...")
    print("=" * 60)
    print("📱 Open your browser and go to: http://localhost:5000")
    print("📱 Alternative link: http://127.0.0.1:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("=" * 60)
    
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)
    
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Please install required packages:")
    print("pip install flask scikit-learn numpy pandas nltk joblib")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1) 