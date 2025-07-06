import os
import csv
import json
import hashlib
import pandas as pd
from datetime import datetime
import streamlit as st

from processor.clean_stream import clean_text
from processor.emotion_detect import detect_emotions
from processor.sidekick import get_tip

# ========================
# 🔐 USER AUTHENTICATION
# ========================

USERS_FILE = "users.json"

# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load user database
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save user database
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Session state init
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# Login/Signup page
def login_signup():
    st.title("🔐 Welcome to StreamToSense")
    option = st.radio("Choose an option:", ["Login", "Sign Up"])

    users = load_users()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Login":
        if st.button("Login"):
            if username in users and users[username] == hash_password(password):
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
    else:
        if st.button("Create Account"):
            if username in users:
                st.warning("Username already exists.")
            elif username.strip() == "" or password.strip() == "":
                st.warning("Username and password cannot be empty.")
            else:
                users[username] = hash_password(password)
                save_users(users)
                st.success("Account created! You can now log in.")

# Show login/signup if not authenticated
if not st.session_state.authenticated:
    login_signup()
    st.stop()

# ========================
# MAIN APP CONFIGURATION
# ========================
st.set_page_config(page_title="StreamToSense", page_icon="🧠", layout="centered")

# Navigation
page = st.sidebar.selectbox("📚 Choose a page", ["📝 Journal", "📘 Emotion Log"])
if st.sidebar.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.session_state.current_user = ""
    st.experimental_rerun()

# ========================
# 📝 JOURNAL PAGE
# ========================
if page == "📝 Journal":
    st.markdown("<h1 style='text-align: center;'>🧠 StreamToSense</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size:18px;'>Hello, <b>{st.session_state.current_user}</b>. Let your thoughts flow. Let your mind be understood.</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### ✍️ What's on your mind today?")
    user_input = st.text_area("Start journaling below...", height=200, placeholder="Type freely, like you're writing in your diary...")

    if st.button("🪞 Reflect Now"):
        if user_input.strip() == "":
            st.warning("Please write something to reflect on. Even a few words can help.")
        else:
            with st.spinner("🧠 Reflecting on your thoughts..."):
                organized = clean_text(user_input)
                emotion = detect_emotions(user_input)
                tip = get_tip(emotion)

            # Save to user-specific CSV log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file = f"{st.session_state.current_user}_emotion_log.csv"
            file_exists = os.path.isfile(log_file)
            with open(log_file, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["timestamp", "text", "emotion", "summary"])
                writer.writerow([timestamp, user_input, emotion, organized])

            # Output display
            st.divider()
            col1, col2 = st.columns([1, 2])

            with col1:
                st.markdown("### 🧠 Emotion")
                st.markdown(f"<h2>{emotion}</h2>", unsafe_allow_html=True)

            with col2:
                st.markdown("### 💡 Suggestion")
                st.info(tip)

            st.markdown("### 🧾 Organized Summary")
            st.success(organized)

            st.markdown("<small>Generated using T5 model + TextBlob sentiment engine.</small>", unsafe_allow_html=True)

# ========================
# 📘 EMOTION LOG PAGE
# ========================
elif page == "📘 Emotion Log":
    st.markdown("## 📘 Your Emotion History")

    log_file = f"{st.session_state.current_user}_emotion_log.csv"
    try:
        df = pd.read_csv(log_file)
        st.dataframe(df.tail(10), use_container_width=True)

        with st.expander("📊 Emotion Frequency"):
            emotion_counts = df['emotion'].value_counts()
            st.bar_chart(emotion_counts)

        with st.expander("📅 Filter by Emotion"):
            unique_emotions = df['emotion'].unique()
            emotion_filter = st.multiselect("Filter by Emotion", options=unique_emotions)
            if emotion_filter:
                filtered_df = df[df['emotion'].isin(emotion_filter)]
                st.dataframe(filtered_df, use_container_width=True)

    except FileNotFoundError:
        st.warning("No entries found yet. Start journaling to build your emotion log.")
