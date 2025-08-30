#!/usr/bin/env python3
"""
Simple script to run the Spam Classifier Flask application
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        ('flask', 'flask'),
        ('scikit-learn', 'sklearn'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('nltk', 'nltk'),
        ('joblib', 'joblib')
    ]
    
    missing_packages = []
    
    for package_name, import_name in required_packages:
        try:
            __import__(import_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            missing_packages.append(package_name)
            print(f"❌ {package_name} is missing")
    
    if missing_packages:
        print(f"\n❌ Missing required packages: {', '.join(missing_packages)}")
        print("\nTo install missing packages, run:")
        print("pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def download_nltk_data():
    """Download required NLTK data"""
    try:
        import nltk
        print("📥 Downloading NLTK data...")
        
        # Download required NLTK data
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠️  Warning: Could not download NLTK data: {e}")
        print("The application may still work, but some features might be limited")

def main():
    """Main function to run the application"""
    print("🚀 Starting Spam Classifier Application")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check dependencies
    if not check_dependencies():
        print("\n🔧 Installing missing packages...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Packages installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run manually:")
            print("pip install -r requirements.txt")
            sys.exit(1)
    
    # Download NLTK data
    download_nltk_data()
    
    print("\n🎯 Starting Flask application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("=" * 50)
    
    try:
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("Please check if all dependencies are installed correctly")
        sys.exit(1)

if __name__ == "__main__":
    main() 