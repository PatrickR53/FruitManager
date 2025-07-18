import streamlit as st
from fruit_manager import *

st.title("🍇 Fruit Manager")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

st.header("💰 Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header(" Inventaire")
st.table(inventaire)
