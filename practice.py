import streamlit as sl
import pandas as pd
import numpy as np

"""
    # Uber pickups in NYC
"""

data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

date_col = 'date/time'
# nrows specifies number of rows desired in data
@sl.cache
def load_data(nrows):
    # obtains data from csv files
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    # inplace = True basically keeps data configuration the way it was before 
    # data name was replaced
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_col] = pd.to_datetime(data[date_col])
    # all we did was make the data easier for us to process
    return data

data_load_state = sl.text('Loading data...')
data = load_data(10000)
data_load_state.write('Done! (using st.cache)')

if sl.checkbox('Show raw data'):
    sl.subheader('Raw data')
    # can use either .write() or .dataframe() to display data
    sl.dataframe(data)

sl.subheader('Number of pickups by hour')

hist_values = np.histogram(data[date_col].dt.hour, bins=24, range=(0,24))[0]

sl.bar_chart(hist_values)

sl.subheader('Map of all pickups')

sl.map(data)

hour_to_filter = sl.slider('hour', 0, 23, 17)

filtered_data = data[data[date_col].dt.hour == hour_to_filter]

sl.subheader(f'Map of all pickups at {hour_to_filter}:00')

sl.map(filtered_data)