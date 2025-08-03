# tracker.py
import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.ai_insights import get_ai_feedback
from utils.data_utils import save_entry, load_data


from datetime import datetime

# --- UI Settings ---
st.set_page_config(page_title="📚 Learning Productivity Tracker", layout="wide", initial_sidebar_state="expanded")
with open("app/styles/darkmode.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🔧 Settings")
mode = st.sidebar.radio("Choose view", ["Log Entry", "View Logs", "Insights"])

# --- Main ---
st.title("📘 Developer Learning Tracker with AI Insights")

if mode == "Log Entry":
    st.subheader("✍️ Log Your Learning")
    date = st.date_input("Date", value=datetime.now())
    topic = st.text_input("What did you learn?")
    duration = st.slider("How many hours?", 0.0, 8.0, 1.0, step=0.5)
    notes = st.text_area("Any reflections, struggles, or wins?")
    
    if st.button("Save Entry"):
        save_entry(date, topic, duration, notes)
        st.success("✅ Entry saved!")

elif mode == "View Logs":
    st.subheader("📊 Your Logged Sessions")
    df = load_data()
    st.dataframe(df.sort_values(by="date", ascending=False))

elif mode == "Insights":
    st.subheader("🤖 AI-Generated Insights")
    df = load_data()
    if len(df) < 3:
        st.info("Log at least 3 sessions to get insights.")
    else:
        insights = get_ai_feedback(df)
        st.markdown("### ✨ Suggestions from AI")
        st.write(insights)


# Inject Notion-style CSS
def apply_custom_style():
    with open("app\styles\darkmode.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

apply_custom_style()

