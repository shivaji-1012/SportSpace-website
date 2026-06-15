import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace | Owner Dashboard", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .dashboard-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid #333;
        padding: 20px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Facility Management Dashboard")
st.write("Real-time analytics for your sports infrastructure.")

# --- SAMPLE DATA ---
revenue_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12000, 15000, 14000, 18000, 22000, 25000]
})

# --- KPI SECTION ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly Revenue", "$25,000", "+12%")
col2.metric("Active Bookings", "142", "-5%")
col3.metric("Utilization", "88%", "+2%")
col4.metric("Avg. Rating", "4.8/5.0", "0.0")

st.markdown("---")

# --- CHARTS ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Revenue Trend")
    fig = px.area(revenue_data, x="Month", y="Revenue", 
                  color_discrete_sequence=['#00f2ff'])
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                      font_color='white', xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Court Utilization")
    labels = ['Basketball', 'Badminton', 'Tennis', 'Swimming']
    values = [45, 25, 20, 10]
    fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                          font_color='white', showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- FACILITY RATINGS TABLE ---
st.subheader("Recent Facility Ratings")
ratings_data = pd.DataFrame({
    "Facility": ["Main Arena", "Pool Complex", "Tennis Courts", "Badminton Halls"],
    "Score": [4.9, 4.7, 4.5, 4.8],
    "Status": ["Active", "Maintenance", "Active", "Active"]
})
st.table(ratings_data)