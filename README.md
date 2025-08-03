# 📚 Personal Learning Productivity Tracker with AI Insights

> A Streamlit web app built for developers and lifelong learners to log their daily learning activities, visualize progress, and receive personalized AI productivity insights.

---

## 🚀 Live Demo  
🔗 _Coming soon – deploy on Streamlit Cloud or your own hosting_

---

## ✨ Project Overview

As developers, we're often juggling between learning, building, and growing our personal brand. This app was built to help you track your daily/weekly learning progress, **stay consistent**, and receive **AI-generated feedback** on how to optimize your learning process.

Whether you’re learning Python, React, or focusing on personal branding, this tool helps you answer:

- _What did I learn this week?_
- _How much time am I dedicating to learning?_
- _What should I focus on next to grow faster and smarter?_

---

## 🔧 Features

- ✅ **Daily Learning Logs** — Capture what you learned, category, and time spent  
- ✅ **Progress Visualizations** — Weekly charts for time invested in learning  
- ✅ **AI-Powered Insights** — Personalized learning advice using OpenAI's GPT  
- ✅ **Streamlit UI** — Clean, fast, and responsive web interface  
- ✅ **CSV Storage** — Local persistent logging of your learning history  
- ✅ **Modular Codebase** — Easy to extend and customize  

---

## 🗂️ Folder Structure# 📚 Personal Learning Productivity Tracker with AI Insights

> A Streamlit web app built for developers and lifelong learners to log their daily learning activities, visualize progress, and receive personalized AI productivity insights.

---

## 🚀 Live Demo  
🔗 _Coming soon – deploy on Streamlit Cloud or your own hosting_

---

## ✨ Project Overview

As developers, we're often juggling between learning, building, and growing our personal brand. This app was built to help you track your daily/weekly learning progress, **stay consistent**, and receive **AI-generated feedback** on how to optimize your learning process.

Whether you’re learning Python, React, or focusing on personal branding, this tool helps you answer:

- _What did I learn this week?_
- _How much time am I dedicating to learning?_
- _What should I focus on next to grow faster and smarter?_

---

## 🔧 Features

- ✅ **Daily Learning Logs** — Capture what you learned, category, and time spent  
- ✅ **Progress Visualizations** — Weekly charts for time invested in learning  
- ✅ **AI-Powered Insights** — Personalized learning advice using OpenAI's GPT  
- ✅ **Streamlit UI** — Clean, fast, and responsive web interface  
- ✅ **CSV Storage** — Local persistent logging of your learning history  
- ✅ **Modular Codebase** — Easy to extend and customize  

---



## 🗂️ Folder Structure
<pre> learning_tracker_ai/ │ ├── app/ │ ├── tracker.py # Main Streamlit app │ └── data/ │ └── learning_data.csv # Logged data (auto-created) │ ├── requirements.txt # Python dependencies └── README.md # Project overview </pre>
📥 How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/KhayrJ6/learning_tracker_ai.git
cd learning_tracker_ai
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the App
bash
Copy
Edit
streamlit run app/tracker.py
🧠 Powered by OpenAI
This project uses OpenAI's API to generate personalized productivity suggestions.

To set it up:

python
Copy
Edit
# In tracker.py
import openai
openai.api_key = "your_openai_api_key"
🔐 Never expose your key in public repos. Use environment variables or secrets.toml in deployment.


