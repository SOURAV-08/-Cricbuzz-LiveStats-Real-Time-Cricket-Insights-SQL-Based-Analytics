import streamlit as st
from api_helper import fetch_live_matches

st.title("⚡ Live Match Updates")

# Call the function with no arguments
matches = fetch_live_matches()

for match in matches:
    with st.container():
        st.subheader(match['teams'])
        st.write(f"**Score:** {match['score']}")
        st.info(f"Status: {match['status']}")
        st.divider()