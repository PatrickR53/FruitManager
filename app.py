import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from fruit_manager import *

st.title("🍇 Dashboard de la plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

with st.sidebar:
    st.header(" 🛒 Vendre des Fruits")
    fruit_vendre = st.selectbox("Choisir un Fruit", list(inventaire.keys()))
    quantite_vendre = st.number_input("Quantité à vendre", min_value=1, step=1)

    if st.button("Vendre"):
        inventaire, tresorerie, message = vendre(inventaire, fruit_vendre, quantite_vendre, tresorerie, prix)
        st.success(message['text'])
        
    st.header("🌱 Récolter des Fruits")
    fruit_recolter = st.selectbox("Choisir un Fruit", list(inventaire.keys()),key="recolter")
    quantite_recolter = st.number_input("Quantité à récolter",min_value=1, step=1, key="quantite_recolter")
    
    if st.button("Récolter"):
        inventaire, message = recolter(inventaire, fruit_recolter, quantite_recolter)
        st.success(message['text'])

st.header("💰 Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("📒 Inventaire")
# inventaire sous forme de tableau
st.table(inventaire)

# inventaire sous forme de graphique
fig, ax = plt.subplots()
# Trier l'inventaire par quantite croissante
inventaire = dict(sorted(inventaire.items(), key=lambda item: item[1], reverse=True))
ax.bar(inventaire.keys(), inventaire.values(), color="salmon", edgecolor='k')
ax.set_xlabel("Fruit")
ax.set_ylabel("Quantité")
ax.set_title("Inventaire")
st.pyplot(fig)

ecrire_inventaire(inventaire)
ecrire_tresorerie(tresorerie)
