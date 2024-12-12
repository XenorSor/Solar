import pickle
import numpy as np
import streamlit as st
import pandas as pd

loaded_model = pickle.load(open('solar_pred.sav', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def solar_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    input_data_as_numpy_array = scaler.transform(input_data_as_numpy_array)
    prediction = loaded_model.predict(input_data_reshaped)

    return prediction

def main():
    st.title('Solar Prediction Web App')
    
    Date = st.date_input('Date of measurement')
    Time = st.time_input('Time of measurement')
    Temperature = st.number_input('Temperature (°F)', step=1., min_value=-459., max_value=10000., value=20., format='%.2f')
    Pressure = st.number_input('Barometric pressure (Hg)2', step=0.01, min_value=29., max_value=31., value=30., format='%.2f')
    Humidity = st.number_input('Humidity percent', step=1., min_value=0., max_value=120., value=30., format='%.2f')
    WindDirection = st.number_input('Wind direction (Degrees)', step=1., min_value=0., max_value=360., value=180., format='%.2f')
    Speed = st.number_input('Wind speed (miles per hour)', step=1., min_value=0., max_value=300., value=5., format='%.2f')
    TimeSunRise = st.time_input('Sunrise (Hawaii time)')
    TimeSunSet = st.time_input('Sunset (Hawaii time)')

    if 'prediction' not in st.session_state:
        st.session_state['prediction'] = ''
    
    W_D = Date.weekday(Date)
    D_Y = Date.year
    D_M = Date.month
    D_D = Date.day
    if D_M in [12, 1, 2]:
        Season = 1
    elif D_M in [3, 4, 5]:
        Season = 2
    elif D_M in [6, 7, 8]:
        Season = 3
    else:
        Season = 0
    T_H = Time.hour
    T_M = Time.minute
    T_S = Time.second
    R_H = TimeSunRise.hour
    R_M = TimeSunRise.minute
    R_S = TimeSunRise.second
    S_H = TimeSunSet.hour
    S_M = TimeSunSet.minute
    S_S = TimeSunSet.second
    
    input_features = [
        Temperature, Pressure, Humidity, WindDirection, Speed, T_H, T_M, T_S, D_M, D_D, R_M, S_H, S_M, W_D, Season
    ]
    st.write(Temperature)
    st.write(Pressure)
    st.write(Humidity)
    st.write(WindDirection)
    st.write(Speed)
    st.write(T_H)
    st.write(T_M)
    st.write(T_S)
    st.write(D_M)
    st.write(D_D)
    st.write(R_M)
    st.write(S_H)
    st.write(S_M)
    st.write(W_D)
    st.write(Season)
    if st.button('Solar Prediction Result'):
        columns = [
            'Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)', 'Speed', 'T_H', 'T_M', 'T_S', 'D_M', 'D_D', 'R_M', 'S_H', 'S_M', 'W_D', 'Season'
        ]
        input = pd.DataFrame([input_features], columns=columns)
        input = scaler.transform(input)
        input_data = input.drop(['Speed', 'T_S', 'D_M', 'S_H', 'W_D', 'Season'], axis=1)
        st.session_state['prediction'] = solar_prediction(input_data)
        st.success(f"Prediction result: {st.session_state['prediction']}")

if __name__ == '__main__':
    main()