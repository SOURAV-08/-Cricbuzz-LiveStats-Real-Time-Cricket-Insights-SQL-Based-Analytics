import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cricbuzz LiveStats Dashboard",
    page_icon="🏏",
    layout="wide"
)

# Main Title
st.title("🏏 Cricbuzz LiveStats Analytics Dashboard")

st.markdown("""
### Welcome to the Full-Stack Cricket Database Project
This application integrates real-time API data with a PostgreSQL backend to provide deep insights into the world of cricket.

#### 🚀 Key Features:
* **Live Match Updates:** Real-time data fetched via RapidAPI.
* **SQL Analytics:** 25 complex queries executed directly on a PostgreSQL 18 database.
* **CRUD Operations:** A complete interface to Create, Read, Update, and Delete player records.
* **Data Visualization:** Clean, interactive tables and metrics built with Streamlit and Pandas.

#### 🛠️ Tech Stack:
* **Backend:** PostgreSQL 18
* **Language:** Python 3.14
* **Libraries:** Streamlit, Psycopg2, Requests, Pandas
""")

st.info("👈 Use the sidebar to navigate between Live Updates, SQL Analytics, and Database Management.")
