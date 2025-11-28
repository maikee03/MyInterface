import streamlit as st
import pandas as pd
import plotly.express as px

income = st.slider("Monthly Income", 0, 7000, 2000) #changed 5000 to 6000
rent = st.slider("Projekte", 0, 2000, 800)
groceries = st.slider("Verwaltung", 0, 1000, 350)
transport = st.slider("Werbung", 0, 500, 60)

expenses = rent + groceries + transport
savings = income - expenses

st.metric("Ausgaben", expenses)
st.metric("Ersparnisse", savings)

df = pd.DataFrame({
    "Category": ["Projekte", "Verwaltung", "Werbung", "Ersparnisse"],
    "Amount": [rent, groceries, transport, savings]
})
fig = px.pie(df, names='Category', values='Amount', title="Monthly Budget")
st.plotly_chart(fig)