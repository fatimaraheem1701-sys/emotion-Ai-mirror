import streamlit as st
import pandas as pd
import random
import os

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
    # 1. Resolve the absolute path to the CSV file
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "emotionaimirror.csv")
    
    # 2. Add a check to provide a helpful error message if file is missing
    if not os.path.exists(file_path):
os.path.join(base_path, "emotionaimirror.csv")
st.stop()
        
    return pd.read_csv(file_path)

data = load_data()

# ---------------- EMOTION SELECTION ----------------
st.subheader("Select Your Emotion")
# Use index=None or placeholder to prevent immediate loading if desired
emotion = st.selectbox(
    "Choose an emotion:",
    data["emotion"].unique()
)

# ---------------- DISPLAY RESULT ----------------
# Use a filter to get rows for the selected emotion
filtered_data = data[data["emotion"] == emotion]

if not filtered_data.empty:
    selected = filtered_data.iloc[0]

    st.markdown("---")

    st.subheader("🎵 Suggested Song")
    st.success(selected["song"])

    st.subheader("💬 Motivational Quote")
    st.info(f'"{selected["quote"]}"')
else:
    st.warning("No recommendations found for this emotion.")

# ---------------- RANDOM RECOMMENDATION ----------------
st.markdown("---")
if st.button("🎲 Surprise Me"):
    random_row = data.sample(1).iloc[0]

    st.subheader(f"😊 You got: {random_row['emotion']}")
    
    st.write("**🎵 Song:**")
    st.success(random_row["song"])

    st.write("**💬 Quote:**")
    st.info(f'"{random_row["quote"]}"')

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Emotion AI Mirror Project | Introduction to AI Lab")
