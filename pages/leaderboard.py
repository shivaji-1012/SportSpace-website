import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace | Leaderboard", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .rank-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid #333;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
    .medal { font-size: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.title("Performance Leaderboard")
st.write("Recognizing top-tier athletes, leading universities, and elite facilities.")

# --- DATA ---
top_players = pd.DataFrame({
    "Rank": [1, 2, 3],
    "Athlete": ["Arjun K.", "Sarah M.", "Vikram R."],
    "Matches Won": [45, 42, 38]
})

top_unis = pd.DataFrame({
    "University": ["IIT Hyderabad", "BITS Pilani", "NIT Trichy"],
    "Active Users": [1200, 950, 800]
})

# --- LAYOUT ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Top Athletes")
    for _, row in top_players.iterrows():
        medal = "🥇" if row['Rank'] == 1 else "🥈" if row['Rank'] == 2 else "🥉"
        st.markdown(f"""
            <div class='rank-card'>
                <span class='medal'>{medal}</span>
                <h3>{row['Athlete']}</h3>
                <p>Matches Won: {row['Matches Won']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")

with col2:
    st.subheader("Top Universities by Engagement")
    fig = px.bar(top_unis, x="University", y="Active Users", 
                 color_discrete_sequence=['#00f2ff'])
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                      font_color='white')
    st.plotly_chart(fig, use_container_width=True)

# --- TOP FACILITIES TABLE ---
st.subheader("Top Rated Facilities")
facilities_data = pd.DataFrame({
    "Facility": ["Central Arena", "Olympic Pool", "Badminton Pro Courts", "Turf 1"],
    "Rating": [4.9, 4.8, 4.7, 4.6]
})
st.dataframe(facilities_data, use_container_width=True, hide_index=True)