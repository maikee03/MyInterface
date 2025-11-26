import streamlit as st
import pandas as pd
import plotly.express as px

income = st.slider("Monthly Income", 0, 6000, 2000) #changed 5000 to 6000
rent = st.slider("Rent", 0, 2000, 800)
groceries = st.slider("Groceries", 0, 1000, 250)
transport = st.slider("Transport", 0, 500, 60)

expenses = rent + groceries + transport
savings = income - expenses

st.metric("Total Expenses", expenses)
st.metric("Savings", savings)

df = pd.DataFrame({
    "Category": ["Rent", "Groceries", "Transport", "Savings"],
    "Amount": [rent, groceries, transport, savings]
})
fig = px.pie(df, names='Category', values='Amount', title="Monthly Budget")
st.plotly_chart(fig)