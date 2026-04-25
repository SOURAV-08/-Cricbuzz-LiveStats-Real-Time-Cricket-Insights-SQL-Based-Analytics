import streamlit as st
import pandas as pd
from db_helper import get_db_connection

st.title("🔍 SQL Analytics Module")
st.write("Execute mandatory practice queries for the Cricbuzz LiveStats project.")

# 1. Expanded List of Queries (Adding more to reach your 25-query goal)
query_dict = {
    "1. All Indian Players": "SELECT name, role, batting_style FROM players WHERE country='India';",
    "2. Matches in last 30 days": "SELECT venue, team_1, team_2, match_date FROM matches WHERE match_date > CURRENT_DATE - INTERVAL '30 days';",
    "3. Top 10 Run Scorers": "SELECT name, runs FROM players ORDER BY runs DESC LIMIT 10;",
    "4. High Margin Wins (>50 runs)": "SELECT venue, winner, margin_value FROM matches WHERE margin_value > 50 AND margin_type = 'runs';",
    "5. List of All-rounders": "SELECT name, country FROM players WHERE role='All-rounder';",
    "6. Matches won by Wickets": "SELECT * FROM matches WHERE margin_type = 'wickets';",
    "7. Total Runs Scored by All Players": "SELECT SUM(runs) as total_tournament_runs FROM players;",
    "8. List of Venues": "SELECT DISTINCT venue FROM matches;",
    "9. Count of Players by Role": "SELECT role, COUNT(*) FROM players GROUP BY role;",
    "10. Specific Player Search (Virat Kohli)": "SELECT * FROM players WHERE name = 'Virat Kohli';"
}

# 2. Dropdown to select the query
selected_label = st.selectbox("Choose a Practice Question:", list(query_dict.keys()))

# 3. Execution Logic
if st.button("Execute Query"):
    try:
        conn = get_db_connection()
        if conn:
            # Get the SQL string from the dictionary based on the selection
            sql_query = query_dict[selected_label]
            
            # Use pandas to run the query and show the result
            df = pd.read_sql(sql_query, conn)
            
            if df.empty:
                st.warning("Query executed successfully, but no data was found.")
            else:
                st.success(f"Showing results for: {selected_label}")
                st.dataframe(df) # st.dataframe is better for scrolling large lists
            
            conn.close()
        else:
            st.error("Could not connect to the database. Is PostgreSQL running?")
    except Exception as e:
        st.error(f"SQL Error: {e}")
        