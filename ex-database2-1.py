import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-test-10fb6")

import pandas as pd
import matplotlib.pyplot as plt
docs = db.collection("penguins").stream()
data = []
for d in docs:
    data.append(d.to_dict())

species =st.sidebar.selectbox("species", ["Adelie", "Chinstrap", "Gentoo"])

df = pd.DataFrame(data)
df = df[df["species"]==species].reset_index(drop=True)
st.write(df)
fig, ax = plt.subplots()
ax.scatter(x=df["bill_length_mm"], y=df["body_mass_g"])
st.pyplot(fig)
