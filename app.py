import streamlit as st
import pandas as pd

df = pd.read_csv("data/salaries.csv")
st.title("Análise do Mercado Data Science")
st.write(df.head())

# Escolher Cargo
job = st.selectbox("Escolha um Cargo", df["job_title"].unique())
filtered = df[df["job_title"] == job]
st.write(filtered["salary_in_usd"].mean())