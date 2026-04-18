import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rfam SQL Database", layout="wide", page_icon="🧬")

st.title("🧬 Public Database Test: Rfam")

try:
    conn = st.connection('rfam_db', type='sql')
except Exception as e:
    st.error(f"Failed to connect: {e}")
    st.stop()

@st.cache_data(ttl=3600)
def fetch_data():
    query = """
    SELECT rfam_acc, rfam_id, description, author, number_of_species
    FROM family 
    ORDER BY number_of_species DESC 
    LIMIT 100;
    """
    return conn.query(query)

with st.spinner("Executing SQL query..."):
    df = fetch_data()

st.subheader("Top 100 RNA Families by Species Count")
st.dataframe(df, use_container_width=True, hide_index=True)
