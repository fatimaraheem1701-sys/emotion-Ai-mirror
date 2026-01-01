import streamlit as st
import pandas as pd
import random

# Page Config
st.set_page_config(page_title="Emotion AI Mirror", page_icon="😊", layout="centered")

# Title
st.title("🪞 Emotion AI Mirror")
st.write("Music & Quotes Based on Emotions")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("emotion_data.csv")

data = load_data()

# Emotion Selection
emotion = st.selectbox("Select Your Emotion:", data["emotion"].unique())

# Filter Data
emotion_row = data[data["emotion"] == emotion].iloc[0]

# Display Results
st.subheader("🎵 Suggested Song")
st.success(emotion_row["song"])

st.subheader("💬 Motivational Quote")
st.info(f'"{emotion_row["quote"]}"')

# Optional: Random Button
if st.button("🔄 Surprise Me"):
    random_row = data.sample(1).iloc[0]
    st.subheader("😊 Emotion")
    st.write(random_row["emotion"])
    st.subheader("🎵 Song")
    st.success(random_row["song"])
    st.subheader("💬 Quote")
    st.info(f'"{random_row["quote"]}"')

# Footer
st.markdown("---")
st.caption("Emotion AI Mirror Project | Fatima | Introduction to AI Lab")

