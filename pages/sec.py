import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="SEC Tickers", layout="wide", page_icon="🏛️")

@st.cache_data(ttl=86400)
def load_sec_data():
    url = "https://www.sec.gov/files/company_tickers.json"
    headers = {"User-Agent": "MyStreamlitApp (your.email@domain.com)"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    df = pd.DataFrame.from_dict(response.json(), orient='index')
    df = df.rename(columns={"cik_str": "CIK", "ticker": "Ticker", "title": "Company Name"})
    return df

st.title("🏛️ SEC Company Tickers")

df = load_sec_data()
st.metric(label="Total Listed Companies", value=f"{len(df):,}")

col1, col2 = st.columns(2)
with col1:
    search_ticker = st.text_input("Search by Ticker (e.g., AAPL)")
with col2:
    search_name = st.text_input("Search by Company Name (e.g., Apple)")

filtered_df = df.copy()
if search_ticker:
    filtered_df = filtered_df[filtered_df['Ticker'].str.contains(search_ticker, case=False, na=False)]
if search_name:
    filtered_df = filtered_df[filtered_df['Company Name'].str.contains(search_name, case=False, na=False)]

st.dataframe(filtered_df, use_container_width=True, hide_index=True)
