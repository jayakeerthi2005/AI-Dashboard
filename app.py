import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Titanic AI Dashboard")

df = pd.read_csv("titanic.csv")

st.header("Dataset Overview")
st.dataframe(df.head())

df["Age"] = df["Age"].fillna(df["Age"].mean())

st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", len(df))
col2.metric("Survival Rate (%)", round(df["Survived"].mean()*100, 2))
col3.metric("Average Age", round(df["Age"].mean(), 2))

st.sidebar.header("Filters")

gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["Sex"].unique())
)

filtered_df = df

if gender != "All":
    filtered_df = df[df["Sex"] == gender]

fig1 = px.histogram(filtered_df, x="Survived")
st.plotly_chart(fig1)

fig2 = px.histogram(filtered_df, x="Sex")
st.plotly_chart(fig2)

fig3 = px.histogram(filtered_df, x="Age")
st.plotly_chart(fig3)

fig4 = px.histogram(filtered_df, x="Pclass")
st.plotly_chart(fig4)

fig5 = px.histogram(filtered_df, x="Fare")
st.plotly_chart(fig5)