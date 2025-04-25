import streamlit as st

# Page config
st.set_page_config(page_title="Joint Petition Calculator", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 0.5em;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>💼 Joint Petition Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Easily calculate your settlement value based on agreement type.</p>", unsafe_allow_html=True)

# Input area
st.divider()
amount = st.text_input("💲 Enter the amount of the settlement:", placeholder="e.g. 15000")

# Dropdown (example for future expansion)
settlement_type = st.selectbox("Choose Settlement Type:", ["Full", "Partial", "Other"])

# Action button
if st.button("📊 Calculate"):
    if amount:
        st.success(f"✅ Your settlement amount is: **${amount}**")
    else:
        st.warning("⚠️ Please enter a dollar amount to proceed.")