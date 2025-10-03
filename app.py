<<<<<<< Updated upstream
<<<<<<< Updated upstream
import pandas as pd
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
import streamlit as st
    
st.header('Lanzar una moneda')

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
=======

streamlit run app.py

>>>>>>> Stashed changes
git add .