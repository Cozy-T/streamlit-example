from collections import namedtuple
import streamlit as st

"""
# Medizin-Tagebuch
"""

with st.echo(code_location='below'):
    st.header("Dosis Information")

    dose = st.number_input("Dosis", min_value=1, max_value=4, value=1, step=1)
    time = st.time_input("Uhrzeit")
    quantity = st.number_input("Anzahl Menge", min_value=1, value=1, step=1)
    milligram = st.number_input("Milligram", min_value=1, value=1, step=1)

    st.header("Symptom Information")

    symptom_rating = st.selectbox("Bewertung", ["Negativ", "Leicht Negativ", "Neutral", "Leicht Positiv", "Positiv"])
    symptom_time = st.time_input("Symptom Zeitstempel")
    symptom_description = st.text_input("Symptombeschreibung")
    mood = st.text_input("Stimmung")

    if st.button("Einreichen"):
        st.write("Dosis: ", dose)
        st.write("Uhrzeit: ", time)
        st.write("Anzahl Menge: ", quantity)
        st.write("Milligram: ", milligram)
        st.write("Bewertung: ", symptom_rating)
        st.write("Symptom Zeitstempel: ", symptom_time)
        st.write("Symptombeschreibung: ", symptom_description)
        st.write("Stimmung: ", mood)
