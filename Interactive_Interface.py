import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interaktive Finanzübersicht")


col1, col2 = st.columns(2)
############ Einnahmen ############
with col1:
    st.header("Einnahmen")
    ## Interaktive Slider für Einnahmen
    Gesamtes_Einkommen = st.slider("Gesamte Einnahmen", 0, 7000, 2000)

    st.metric("Gesamtes Einkommen", Gesamtes_Einkommen)

############ Ausgaben ############
with col2:
    st.header("Ausgaben")
    ## Interaktive Slider für Ausgaben
    Projekte = st.slider("Projektausgaben", 0, 2000, 800)
    Verwaltung = st.slider("Verwaltungsausgaben", 0, 1000, 350)
    Werbung = st.slider("Werbungsausgaben", 0, 500, 60)
    
    col1, col2 = st.columns(2)
    with col1:
        Gesamte_Ausgaben = Projekte + Verwaltung + Werbung
        st.metric("Gesamte Ausgaben", Gesamte_Ausgaben)
    with col2:
        Ersparnisse = Gesamtes_Einkommen - Gesamte_Ausgaben
        st.metric("Ersparnisse/Nicht Ausgegeben", Ersparnisse)

    ## Visualisierung der Ausgaben
    df = pd.DataFrame({
        "Category": ["Projekte", "Verwaltung", "Werbung"],
        "Amount": [Projekte, Verwaltung, Werbung]
    })
    fig = px.pie(df, names='Category', values='Amount', title="Anteile Ausgaben")
    fig.update_layout(title_font_size=24, title_font_color="black",font=dict(size=18, color="black"))
    fig.update_traces(marker=dict(colors= ['#636EFA', '#EF553B', '#00CC96'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)