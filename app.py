import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
)
# pass count
pass_count = st.number_input('How many cars do you need?', step=1, min_value=1, max_value=40)
st.write(pass_count)

# date and time of the ride
d = str(st.date_input(
    "When's your taxi ride?",
    datetime.date(2019, 7, 6)))
st.write('Your ride is on:', d)

t = str(st.time_input('Time of your ride', datetime.time(8, 45)))
st.write("You're taking a taxi at the following time:", t)

date_and_time = d + ' ' + t

date_and_time = datetime.datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')

st.write(date_and_time)


# - pickup longitude
# - pickup latitude
pi_long = st.number_input('Insert pickup longitude ')

st.write('The current pickup longitude is ', pi_long)

pi_lat = st.number_input('Insert pickup latitude')

st.write('The  current pickup latitude  is ', pi_lat)

# - dropoff longitude
# - dropoff latitude

drp_long = st.number_input('Insert dropoff longitude ')

st.write('The current dropoff longitude is ', drp_long)

drp_lat = st.number_input('Insert dropoff latitude')

st.write('The  current dropoff latitude  is ', drp_lat)

###################################
url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...
params = {'pickup_datetime' : date_and_time,
          'pickup_longitude' : pi_long,
          'pickup_latitude' : pi_lat,
          'dropoff_longitude' : drp_long,
          'dropoff_latitude' : drp_lat,
          'passenger_count': pass_count
          } #add other params expected by the API

# 3. Let's call our API using the `requests` package...

resposne = requests.get('https://taxifare.lewagon.ai/predict', params=params)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# Finally, we can display the prediction to the user
st.write(resposne.json())
