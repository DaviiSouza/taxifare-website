import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front-end
'''

st.markdown('''
Davi Souza Predictions
''')



with st.form('Parameters for prediction'):
    dt, tm = st.columns(2)

    with dt:
        date = st.date_input('Date', value=datetime.date(2026, 8, 21))
    with tm:
        time = st.time_input('Time', value=datetime.time(11, 0))

    col1, col2 = st.columns(2)

    with col1:
        pickup_latitude = st.number_input('Pickup latitude', min_value=-90.0, max_value=90.0, value=0.0, step=0.01, format='%0.5f')
    with col2:
        pickup_longitude = st.number_input('Pickup longitude', min_value=-180.0, max_value=180.0, value=0.0, step=0.01, format='%0.5f')

    col3, col4 = st.columns(2)

    with col3:
        dropoff_latitude = st.number_input('Dropoff latitude', min_value=-90.0, max_value=90.0, value=0.0, step=0.01, format='%0.5f')
    with col4:
        dropoff_longitude = st.number_input('Dropoff longitude', min_value=-180.0, max_value=180.0, value=0.0, step=0.01, format='%0.5f')

    passager_count = st.slider('Passager count', 1, 20, 1)

    submit = st.form_submit_button('Submit')


url = 'https://taxifare-api-956743013501.europe-west1.run.app/predict'
pickup_datetime = f"{date} {time}"

if url == 'https://taxifare-api-956743013501.europe-west1.run.app/predict':

    if submit:
        params = {
            'pickup_datetime': pickup_datetime,
            'pickup_longitude': pickup_longitude,
            'pickup_latitude': pickup_latitude,
            'dropoff_longitude': dropoff_longitude,
            'dropoff_latitude': dropoff_latitude,
            'passenger_count': passager_count
        }

        response = requests.get(url, params=params)
        prediction = response.json()

        st.write(prediction)
