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
    Temperature = st.number_input('Temperature (°F)', step=1., min_value=-459, max_value=10000, value=20, format='%.2f')
    Pressure_f = st.number_input('Barometric pressure (Hg)', step=0.01, format='%.2f'#, min_value=29, max_value=31, value=30, format='%.2f'
                                 )
    Humidity = st.number_input('Humidity percent', step=1., min_value=0, max_value=120, value=30, format='%.2f')
    WindDirection = st.number_input('Wind direction (Degrees)', step=1., min_value=0, max_value=360, value=180, format='%.2f')
    Speed = st.number_input('Wind speed (miles per hour)', step=1., min_value=0, max_value=300, value=5, format='%.2f')
    TimeSunRise = st.time_input('Sunrise (Hawaii time)')
    TimeSunSet = st.time_input('Sunset (Hawaii time)')

    float_value = st.number_input(
        "Number",
        step=0.01,
    )
    int_value = round(float_value * 100)
    st.write(int_value, float_value)

    prediction = ''

    if st.button('Solar Prediction Result'):
        prediction = solar_prediction([Date, Time, Temperature, Pressure_f, Humidity, WindDirection, Speed, TimeSunRise, TimeSunSet])

    st.success(prediction)

if __name__ == '__main__':
    main()