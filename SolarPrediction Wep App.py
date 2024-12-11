import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('solar_pred.sav', 'rb'))

def solar_prediction(input_data):
     input_data_as_numpy_array = np.asarray(input_data)
     input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

     prediction = loaded_model.predict(input_data_reshaped)

     return prediction

def main():
    st.title('Solar Prediction Web App')

    Date = st.date_input('Date of measurement')
    Time = st.time_input('Time of measurement')
    Temperature = st.number_input('Temperature (°F)', min_value=-459, max_value=10000, value=20)
    Pressure = st.number_input('Barometric pressure (Hg)', min_value=29, max_value=31, value=30)
    Humidity = st.number_input('Humidity percent', min_value=0, max_value=120, value=30)
    WindDirection = st.number_input('Wind direction (Degrees)', min_value=0, max_value=360, value=180)
    Speed = st.number_input('Wind speed (miles per hour)', min_value=0, max_value=300, value=5)
    TimeSunRise = st.time_input('Sunrise (Hawaii time)')
    TimeSunSet = st.time_input('Sunset (Hawaii time)')

    prediction = ''

    if st.button('Solar Prediction Result'):
        prediction = solar_prediction([Date, Time, Temperature, Pressure, Humidity, WindDirection, Speed, TimeSunRise, TimeSunSet])

    st.success(prediction)

if __name__ == '__main__':
    main()