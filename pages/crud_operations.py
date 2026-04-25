import streamlit as st
from db_helper import get_db_connection

st.title("🛠️ Player Management (CRUD)")

with st.form("add_player_form"):
    st.subheader("Add New Player")
    name = st.text_input("Name")
    country = st.text_input("Country")
    role = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
    submitted = st.form_submit_button("Save Player")

    if submitted:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO players (name, country, role) VALUES (%s, %s, %s)", (name, country, role))
        conn.commit()
        cur.close()
        conn.close()
        st.success(f"Player {name} added successfully!")