import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT * FROM `bigquery-public-data.bbc_news.fulltext` LIMIT 10")

st.header("BBC Top 10 news")
for row in rows:
    with st.expander(row["title"]):
        st.write(row["body"])
