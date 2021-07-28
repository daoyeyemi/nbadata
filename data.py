import streamlit as sl
import pandas as pd
import sportsipy

"""
    # Check out about 70 years worth of NBA statistics!
"""
year_list = list(range(2010, 2019))

year_select = sl.sidebar.selectbox('Season Starting Year', year_list)

positions_array = ['PG', 'SG', 'SF', 'PF', 'C']

select_array = sl.sidebar.multiselect('Positions', positions_array, positions_array)

print(select_array)
print(year_select)