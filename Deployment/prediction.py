import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

with open('model_rf.pkl', 'rb') as file_1: 
    model_rf = pickle.load(file_1)


def run():
    with st.form(key='Form Parameters'):
        Name = st.text_input('Name', value='')
        Gender = st.selectbox('Sex', ('Male', 'Female'), index=1)
        Height = st.number_input('Height', min_value=120, max_value=210, step=1, help='Tinggi Badan (Cm)')
        Weight = st.number_input('Weight', min_value=10, max_value=120, step=1, help='Berat Badan (Kg)')
        BMI = st.number_input('Body Mass Index', min_value=3.9, max_value=37.2, step=0.1, help='Cara Menghitung Index Massa Tubuh [berat badan (kg) : (tinggi badan (m) x tinggi badan (m))]')
        Age = st.number_input('Age', min_value=11, max_value=112, step=1, help='Umur (Yo)')
        st.markdown('---')
        submitted = st.form_submit_button('Predict')


    data_inf = {'Age': int(Age),
 'Gender': Gender,
 'Height': int(Height),
 'Weight': int(Weight),
 'BMI': BMI}

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
            
            # predict result
            y_predict_inf = model_rf.predict(data_inf)# predict result

            st.write('# Kategori', str(y_predict_inf))

if __name__ == '__main___':
    run()
