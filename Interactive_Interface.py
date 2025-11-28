import streamlit as st
import pandas as pd
import plotly.express as px

################ SLIDER INPUT ################

#Einkommen
Gesamtes_Einkommen = st.slider("Gesamtes Einkommen", 0, 7000, 2000)

#Ausgaben
Projekte = st.slider("Projektausgaben", 0, 2000, 800)
Verwaltung = st.slider("Verwaltungsausgaben", 0, 1000, 350)
Werbung = st.slider("Werbungsausgaben", 0, 500, 60)
Gesamte_Ausgaben = Projekte + Verwaltung + Werbung

################# Calculations #################

#Bilanz
Ersparnisse = Gesamtes_Einkommen - Gesamte_Ausgaben

################# Output #################
st.header("Jahres Bilanz")
st.metric("Gesamte Ausgaben", Gesamte_Ausgaben) #st.metric gives as a nice formatted output of Label and Value
#st.metric("Ersparnisse", Ersparnisse)

df = pd.DataFrame({
    "Category": ["Projekte", "Verwaltung", "Werbung", "Ersparnisse"],
    "Amount": [Projekte, Verwaltung, Werbung, Ersparnisse]
})
fig = px.pie(df, names='Category', values='Amount', title="Jahres Bilanz Verteilung")
st.plotly_chart(fig)