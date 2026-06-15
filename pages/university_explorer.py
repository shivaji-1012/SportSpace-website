import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace | Universities", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .univ-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, border 0.3s ease;
        margin-bottom: 20px;
    }
    .univ-card:hover {
        border: 1px solid #00f2ff;
        transform: translateY(-5px);
    }
    .card-title { color: #00f2ff; font-size: 1.5rem; font-weight: bold; }
    .metric { font-size: 1.1rem; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER & FILTERS ---
st.title("Explore University Facilities")

with st.sidebar:
    st.header("Filters")
    sport = st.multiselect("Select Sport", ["Badminton", "Cricket", "Tennis", "Basketball", "Swimming"])
    dist = st.slider("Max Distance (km)", 0, 50, 10)
    price = st.slider("Price per Hour ($)", 0, 100, 25)

# --- DATA ---
universities = [
    {"name": "IIT Hyderabad", "sports": "Cricket, Badminton", "price": 15, "rating": 4.8},
    {"name": "BITS Pilani", "sports": "Tennis, Swimming", "price": 20, "rating": 4.7},
    {"name": "VIT", "sports": "Basketball, Cricket", "price": 12, "rating": 4.5},
    {"name": "SRM", "sports": "Badminton, Swimming", "price": 18, "rating": 4.6},
    {"name": "NIT Trichy", "sports": "Tennis, Basketball", "price": 14, "rating": 4.7},
]

# --- DISPLAY CARDS ---
cols = st.columns(3)
for i, univ in enumerate(universities):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="univ-card">
                <div class="card-title">{univ['name']}</div>
                <p><strong>Sports:</strong> {univ['sports']}</p>
                <div class="metric">💰 ${univ['price']}/hr</div>
                <div class="metric">⭐ {univ['rating']}/5.0</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"View {univ['name']}", key=univ['name']):
            st.info(f"Redirecting to booking for {univ['name']}...")