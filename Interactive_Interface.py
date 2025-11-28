import streamlit as st
import pandas as pd
import plotly.express as px

################ SLIDER INPUT ################

#Einkommen


#Ausgaben


################# Calculations #################

#Bilanz


################# Output #################
st.header("Jahres Bilanz")
col1, col2 = st.columns(2)
with col1:
    Gesamtes_Einkommen = st.slider("Gesamtes Einkommen", 0, 7000, 2000)
    
    st.metric("Gesamtes Einkommen", Gesamtes_Einkommen)

with col2:
    Projekte = st.slider("Projektausgaben", 0, 2000, 800)
    Verwaltung = st.slider("Verwaltungsausgaben", 0, 1000, 350)
    Werbung = st.slider("Werbungsausgaben", 0, 500, 60)
    
    Gesamte_Ausgaben = Projekte + Verwaltung + Werbung
    st.metric("Gesamte Ausgaben", Gesamte_Ausgaben)
    
Ersparnisse = Gesamtes_Einkommen - Gesamte_Ausgaben
df = pd.DataFrame({
    "Category": ["Projekte", "Verwaltung", "Werbung", "Ersparnisse"],
    "Amount": [Projekte, Verwaltung, Werbung, Ersparnisse]
})
fig = px.pie(df, names='Category', values='Amount', title="Jahres Bilanz Verteilung")
st.plotly_chart(fig)