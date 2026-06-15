import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace | Community", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .community-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .community-card:hover { border: 1px solid #00f2ff; }
    .tag { color: #00f2ff; font-size: 0.8rem; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("Community Hub")
st.write("Find teammates, join matches, and connect with local athletes.")

# --- CREATE POST SECTION ---
with st.expander("➕ Create a New Post"):
    title = st.text_input("Post Title")
    category = st.selectbox("Category", ["Match Request", "Tournament", "Group Discussion"])
    desc = st.text_area("Description")
    if st.button("Post to Community"):
        st.success("Post live!")

st.markdown("---")

# --- SAMPLE POSTS DATA ---
posts = [
    {"title": "Need 2 badminton players", "tag": "MATCH REQUEST", "desc": "Intermediate level, playing at IIT Hyderabad courts tomorrow at 6 PM."},
    {"title": "Weekend football game", "tag": "MATCH REQUEST", "desc": "Gathering a group for a 5v5 friendly match this Saturday."},
    {"title": "Box cricket tournament", "tag": "TOURNAMENT", "desc": "Register your team for the Inter-college Box Cricket League."}
]

# --- DISPLAY POSTS ---
for post in posts:
    st.markdown(f"""
        <div class="community-card">
            <div class="tag">{post['tag']}</div>
            <h3>{post['title']}</h3>
            <p>{post['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Join Match", key=post['title']):
            st.toast(f"You've joined: {post['title']}")

# --- CREATE GROUPS SECTION ---
st.markdown("## Popular Groups")
cols = st.columns(3)
groups = ["Cricket Fanatics", "Swimming Enthusiasts", "Pickleball Pros"]
for i, group in enumerate(groups):
    with cols[i]:
        st.markdown(f"<div class='community-card' style='text-align:center'>{group}<br><button>View</button></div>", unsafe_allow_html=True)