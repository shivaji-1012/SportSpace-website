import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stApp { background-color: #050505; }
    .card { 
        padding: 20px; border-radius: 15px; border: 1px solid #333; 
        background: rgba(255,255,255,0.03); transition: 0.3s;
        text-align: center; cursor: pointer;
    }
    .card:hover { border: 1px solid #00f2ff; background: rgba(0, 242, 255, 0.1); }
    .metric-val { font-size: 2rem; color: #00f2ff; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# Loading the hero.html from assets
with open("assets/hero.html", "r") as f:
    hero_html = f.read()
components.html(hero_html, height=800)

# --- PROBLEM STATEMENT ---
st.markdown("---")
st.title("The Challenge")
st.write("University sports facilities often sit idle while local athletes struggle to find premium spaces. SportSpace bridges this gap.")

# --- METRIC CARDS ---
col1, col2, col3 = st.columns(3)
with col1: st.markdown("<div class='card'><div class='metric-val'>15+</div>Universities</div>", unsafe_allow_html=True)
with col2: st.markdown("<div class='card'><div class='metric-val'>50k+</div>Active Athletes</div>", unsafe_allow_html=True)
with col3: st.markdown("<div class='card'><div class='metric-val'>98%</div>Uptime</div>", unsafe_allow_html=True)

# --- SPORTS SELECTION ---
st.markdown("## Discover Sports")
sports = ["Badminton", "Cricket", "Box Cricket", "Tennis", "Pickleball", "Basketball", "Volleyball", "Swimming", "Football"]

# Create a 3-column grid
cols = st.columns(3)
for i, sport in enumerate(sports):
    with cols[i % 3]:
        # Using a button that directs to the university explorer page
        if st.button(f"Play {sport}", key=sport, use_container_width=True):
            st.switch_page("pages/university_explorer.py")

st.markdown("<br><br>", unsafe_allow_html=True)