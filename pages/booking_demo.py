import streamlit as st
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="SportSpace | Booking", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .booking-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.3);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
    }
    .qr-placeholder {
        width: 150px; height: 150px;
        background: white; margin: 20px auto;
        display: flex; align-items: center; justify-content: center;
        font-size: 50px; border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Secure Your Slot")

# --- BOOKING LOGIC ---
if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

if not st.session_state.confirmed:
    with st.container():
        st.markdown("<div class='booking-card'>", unsafe_allow_html=True)
        facility = st.selectbox("Select Facility", ["IIT Hyderabad Arena", "BITS Pilani Court", "VIT Sports Complex"])
        date = st.date_input("Select Date")
        time_slot = st.time_input("Select Time")
        
        if st.button("Proceed to Payment", use_container_width=True):
            with st.spinner("Processing payment..."):
                time.sleep(2)
                st.session_state.confirmed = True
                st.session_state.booking_id = f"SS-{random.randint(10000, 99999)}"
                st.session_state.details = {"fac": facility, "date": date, "time": time_slot}
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- CONFIRMATION SCREEN ---
    st.success("Booking Confirmed!")
    st.markdown(f"""
        <div class="booking-card" style="text-align: center;">
            <h3>Booking Reference</h3>
            <div class="qr-placeholder">📱</div>
            <h2>{st.session_state.booking_id}</h2>
            <p><strong>Facility:</strong> {st.session_state.details['fac']}</p>
            <p><strong>Date:</strong> {st.session_state.details['date']}</p>
            <p><strong>Time:</strong> {st.session_state.details['time']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Make Another Booking"):
        st.session_state.confirmed = False
        st.rerun()
        