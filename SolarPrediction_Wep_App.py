import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('solar_pred.sav', 'rb'))

def solar_prediction(input_data):
    #input_data_as_numpy_array = np.asarray(input_data)
    #input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data)

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

    prediction = ''

    D_Y = Date.year
    D_M = Date.month
    D_D = Date.day
    T_H = Time.hour
    T_M = Time.minute
    T_S = Time.second
    R_H = TimeSunRise.hour
    R_M = TimeSunRise.minute
    R_S = TimeSunRise.second
    S_H = TimeSunSet.hour
    S_M = TimeSunSet.minute
    S_S = TimeSunSet.second

    if st.button('Solar Prediction Result'):
        prediction = solar_prediction([D_Y, D_M, D_D, T_H, T_M, T_S, Temperature, Pressure, Humidity, WindDirection, Speed, R_H, R_M, R_S, S_H, S_M, S_S])

    st.success(prediction)

if __name__ == '__main__':
    main()