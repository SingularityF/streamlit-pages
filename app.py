import streamlit as st

st.set_page_config(
    page_title="Enterprise Data Portal",
    page_icon="🏢",
    layout="centered"
)

st.title("🏢 Enterprise Data Portal")
st.markdown("""
Welcome to the unified analytics portal. 

By hosting multiple applications within this single Streamlit instance, we consolidate our compute footprint into a single Databricks App.

**👈 Select a dashboard from the sidebar to begin.**
""")
