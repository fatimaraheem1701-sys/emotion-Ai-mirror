import streamlit as st
import pandas as pd
import random
import os

# ---------------- PAGE SETTINGS ----------------
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
    csv_path = os.path.join("emotionaimirror", "emotionaimirror.csv")
    return pd.read_csv(csv_path)

data = load_data()

# ---------------- EMOTION SELECTION ----------------
st.subheader("Select Your Emotion")

emotion = st.selectbox(
    "Choose an emotion:",
    data["emotion"].unique()
)

# ---------------- DISPLAY RESULT ----------------
row = data[data["emotion"] == emotion].iloc[0]

st.markdown("---")

st.subheader("🎵 Suggested Song")
st.success(row["song"])

st.subheader("💬 Motivational Quote")
st.info(f'"{row["quote"]}"')

# ---------------- RANDOM OPTION ----------------
st.markdown("---")
if st.button("🎲 Surprise Me"):
    r = data.sample(1).iloc[0]

    st.subheader("😊 Emotion")
    st.write(r["emotion"])

    st.subheader("🎵 Song")
    st.success(r["song"])

    st.subheader("💬 Quote")
    st.info(f'"{r["quote"]}"')

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Emotion AI Mirror Project | Introduction to AI Lab")
