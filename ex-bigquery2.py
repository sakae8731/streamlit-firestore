import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

credentials = service_account.credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

@st.cache_data(ttl=600)
def run_query(query):
    result = client.query(query).to_dataframe()
    return result

df = run_query(""""SELECT date, deaths, countries_and_territories as country FROM `bigquery-public data.covid19_ecdc.covid_19_geographic_distribution_worldwide`""")
country = st.sidebar.selectbox("country", ["Japan", "Australia", "Brazil", "China", "United_States_of_America"])
df = df[df["country"] == country]
df = df.reset_index(drop=True)

st.header("COVID-19 numbers")
st.subheader(country)
st.line_chart(df, x="data", y="deaths")
