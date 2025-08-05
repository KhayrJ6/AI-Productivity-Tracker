# tracker.py
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_utils import save_entry, load_data
import streamlit as st
import pandas as pd
from datetime import datetime
import calendar
from utils.ai_insights import get_ai_feedback

# --------------- Styling -------------------
with open("app\styles\darkmode.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------- Page Config ------------------
st.set_page_config(page_title="Learning Tracker", layout="wide", initial_sidebar_state="expanded")

# ----------- Session State Setup ----------
if "learning_log" not in st.session_state:
    st.session_state.learning_log = []

# ------------- Sidebar ---------------------
with st.sidebar:
    st.title("📅 Calendar")
    today = datetime.today()
    st.markdown(f"### {calendar.month_name[today.month]} {today.year}")
    cal = calendar.monthcalendar(today.year, today.month)
    st.write("Mon Tue Wed Thu Fri Sat Sun")
    for week in cal:
        st.write(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
    
    st.markdown("---")
    st.markdown("**💡 Tip:** Stay consistent with small learning efforts daily!")

# ------------ Main App ---------------------
st.title("📚 Developer Learning Productivity Tracker")

with st.form("log_form"):
    st.subheader("📥 Log your learning activity")

    topic = st.text_input("What did you learn today?", placeholder="e.g. Python decorators")
    duration = st.slider("How many hours?", 0.0, 10.0, step=0.5)
    notes = st.text_area("Brief notes", placeholder="Optional summary of what you learned")

    submitted = st.form_submit_button("➕ Add Entry")
    if submitted and topic and duration:
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "topic": topic,
            "duration": duration,
            "notes": notes
        }
        st.session_state.learning_log.append(entry)
        st.success("Learning entry added!")

# ------------ Dataframe Display -------------
if st.session_state.learning_log:
    df = pd.DataFrame(st.session_state.learning_log)
    st.subheader("📈 Your Learning Logs")
    st.dataframe(df)

    # --------- AI Feedback Section ---------
    st.markdown("---")
    st.subheader("🧠 AI Productivity Insight")
    feedback = get_ai_feedback(df)
    st.markdown(feedback)

# ----------- Habit Card Component -----------
st.markdown("---")
st.subheader("🔁 Weekly Habit Tracker")

st.markdown("""
<div class='habit-card'>
    <div class='habit-header'>🔥 Daily Study Habit</div>
    <div class='habit-body'>
        <p>✅ Aim: Learn at least 1 hour per day</p>
        <ul>
            <li>Track your streak</li>
            <li>Break down big goals</li>
            <li>Use this app every evening</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)
