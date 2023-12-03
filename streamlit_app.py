import streamlit as st
import pandas as pd
from google.cloud import firestore

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# from google.oauth2 import service_account
# import json
# key_dict = json.loads(st.secrets["textkey"])
# creds = service_account.Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials=creds, project="streamlit-app-c394d")

# docs = db.collection("iris").stream()
# data = []
# for d in docs:
#     data.append(d.to_dict())

# species = st.sidebar.selectbox("species", ["setosa", "versicolor", "virginica"])

# df = pd.DataFrame(data)
# df = df[df["species"] == species].reset_index(drop=True)
# st.write(df)
# st.line_chart(df, x="sepal_length", y="sepal_width")
