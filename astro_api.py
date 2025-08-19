import datetime
import streamlit as st
import google.generativeai as genai
import os

# --- Gemini Setup ---
# Replace with your Gemini API key (get from https://aistudio.google.com/)

gemini_api = st.secrets["api_keys"]["gemini_api"]

# Configure Gemini
genai.configure(api_key=gemini_api)

# Zodiac date ranges
ZODIAC_DATES = {
    "Aries": ((3, 21), (4, 19)),
    "Taurus": ((4, 20), (5, 20)),
    "Gemini": ((5, 21), (6, 20)),
    "Cancer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Scorpio": ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21)),
    "Capricorn": ((12, 22), (1, 19)),
    "Aquarius": ((1, 20), (2, 18)),
    "Pisces": ((2, 19), (3, 20))
}

# Lucky details (rule-based)
LUCKY_DETAILS = {
    "Aries": {"color": "Red", "stone": "Ruby", "number": 9},
    "Taurus": {"color": "Green", "stone": "Emerald", "number": 6},
    "Gemini": {"color": "Yellow", "stone": "Agate", "number": 5},
    "Cancer": {"color": "White", "stone": "Pearl", "number": 2},
    "Leo": {"color": "Gold", "stone": "Peridot", "number": 1},
    "Virgo": {"color": "Blue", "stone": "Sapphire", "number": 5},
    "Libra": {"color": "Pink", "stone": "Opal", "number": 6},
    "Scorpio": {"color": "Black", "stone": "Topaz", "number": 9},
    "Sagittarius": {"color": "Purple", "stone": "Turquoise", "number": 3},
    "Capricorn": {"color": "Brown", "stone": "Garnet", "number": 8},
    "Aquarius": {"color": "Sky Blue", "stone": "Amethyst", "number": 7},
    "Pisces": {"color": "Sea Green", "stone": "Aquamarine", "number": 3}
}

def get_zodiac_sign(day: int, month: int) -> str:
    for sign, ((m1, d1), (m2, d2)) in ZODIAC_DATES.items():
        if (month == m1 and day >= d1) or (month == m2 and day <= d2):
            return sign
    return "Unknown"

def generate_ai_response(zodiac: str, user_query: str = None) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    if user_query:
        prompt = f"""You are an expert astrologer. The user is a {zodiac}. You are an expert astrologer.
    The user is a {zodiac}.
    Answer their question in **5-7 short sentences only**.
    Keep it clear, friendly, and mystical.
    Do NOT include today's date.\n\nQuestion: {user_query}"""
    else:
        lucky = LUCKY_DETAILS.get(zodiac, {})
        prompt = f"""
        You are an expert astrologer. Write today's detailed horoscope for {zodiac}.
        Cover:
        - Career
        - Love/relationships
        - Health
        - Finance
        Do NOT include today's date in your response.
        End with:
        - Lucky Color:  {lucky.get('color', 'N/A')}
        - Lucky Stone:  {lucky.get('stone', 'N/A')}
        - Lucky Number:  {lucky.get('number', 'N/A')}
        in 3 different lines
        """

    response = model.generate_content(prompt)
    return response.text.strip()
