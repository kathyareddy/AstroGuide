import streamlit as st
import datetime
from astro_api import get_zodiac_sign, generate_ai_response

st.set_page_config(page_title="AstroGuide – AI Astrologer", page_icon="assets/logo.png", layout="centered")

# --- Center everything using a container ---
with st.container():
    st.markdown(
        """
        <style>
        .stApp {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .stButton button {
            margin: 10px auto;
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Bigger and wider logo
    st.image("assets/logo.png", width=500)

    st.title("AstroGuide – AI Astrologer")


    # --- User Birth Details ---
    name = st.text_input("Enter Your Name")
    dob = st.date_input("Enter Your Date of Birth", datetime.date(2000, 1, 1))
    tob = st.text_input("Enter Your Time of Birth (HH:MM)", value="12:00")
    place = st.text_input("Enter Your Place of Birth")

    if dob:
        zodiac = get_zodiac_sign(dob.day, dob.month)
        st.subheader(f"Hello {name}! Your Zodiac Sign is **{zodiac}**")

        # Tabs
        tab1, tab2 = st.tabs(["Daily Horoscope", "Ask the Astrologer"])

        with tab1:
            st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
            if st.button("Get My Horoscope"):
                with st.spinner("Consulting the stars..."):
                    horoscope = generate_ai_response(zodiac)
                st.success("Here’s your daily guidance:")
                st.write(horoscope)
            st.markdown("</div>", unsafe_allow_html=True)

        with tab2:
            user_question = st.text_area("Ask any question (love, career, health, etc.)")
            st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
            if st.button("Ask"):
                if user_question.strip():
                    with st.spinner("Seeking cosmic insights..."):
                        answer = generate_ai_response(zodiac, user_question)
                    st.success("The stars respond:")
                    st.write(answer)
                else:
                    st.warning("Please type a question first.")
            st.markdown("</div>", unsafe_allow_html=True)
