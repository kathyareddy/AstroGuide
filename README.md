# AstroGuide – Your Personal Astrology Assistant

AstroGuide is a Streamlit-based web app that provides personalized horoscope insights. It uses Gemini AI API to generate dynamic, AI-powered astrological responses based on your zodiac sign.

## Features
-  Get your zodiac sign based on birthdate
-  AI-powered horoscope predictions using Gemini API
-  Clean and responsive UI
-  Lightweight and easy to deploy (works locally or on Streamlit Cloud)

## Installation & Setup
```bash
git clone https://github.com/your-username/AstroGuide.git
cd AstroGuide
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

## API Key Setup

Create a file at .streamlit/secrets.toml and add:

[api_keys]
gemini_api = "your_gemini_api_key_here"

Run the App
streamlit run main.py


The app will open at http://localhost:8501/.


## Deployment (Streamlit Cloud)

Push your code to GitHub

Go to Streamlit Cloud and connect your repo

Add your secrets.toml in App → Settings → Secrets

Your app will be live


## Requirements
streamlit
google-generativeai
python-dotenv

## Contributing

Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request

## License

Licensed under the MIT License

## Author

Developed by Kathya Reddy

