import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Emotion AI Mirror",
    page_icon="😊",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🪞 Emotion AI Mirror")
st.write("Emotion-based Music and Quotes Recommendation System")

# ---------------- LOAD CSV DATA ----------------
@st.cache_data
def load_data():
    # CSV file must contain columns: emotion, song, quote
    return pd.read_csv("emotionaimirror.csv")

data = load_data()

# ---------------- EMOTION SELECTION ----------------
st.subheader("Select Your Emotion")
emotion = st.selectbox(
    "Choose an emotion:",
    data["emotion"].unique()
)

# ---------------- DISPLAY RESULT ----------------
selected = data[data["emotion"] == emotion].iloc[0]

st.markdown("---")

st.subheader("🎵 Suggested Song")
st.success(selected["song"])

st.subheader("💬 Motivational Quote")
st.info(f'"{selected["quote"]}"')

# ---------------- RANDOM RECOMMENDATION ----------------
st.markdown("---")
if st.button("🎲 Surprise Me"):
    random_row = data.sample(1).iloc[0]

    st.subheader("😊 Emotion")
    st.write(random_row["emotion"])

    st.subheader("🎵 Song")
    st.success(random_row["song"])

    st.subheader("💬 Quote")
    st.info(f'"{random_row["quote"]}"')

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Emotion AI Mirror Project | Introduction to AI Lab")
