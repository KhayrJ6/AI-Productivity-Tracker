# app/utils/ai_insights.py
import pandas as pd

def get_ai_feedback(df: pd.DataFrame) -> str:
    # Later, you'll connect Gemini's API here
    total_hours = df['duration'].sum()
    recent_topics = ', '.join(df['topic'].tail(3).tolist())
    
    return f"""
You've studied for a total of **{total_hours:.1f} hours** recently.
Keep up the momentum! Your latest topics were: {recent_topics}.
Try to focus more on consistent, deep work over passive consumption.
"""
