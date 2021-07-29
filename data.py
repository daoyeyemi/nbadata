import streamlit as sl
import pandas as pd

"""
    # Check out about 70 years worth of statistics around the NBA!
"""


def load_data():
    data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2021_per_game.html", header = 0)
    print(data)

data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2021_per_game.html", header=0)
sl.dataframe(data[0])

year_list = list(range(1950, 2021))

sl.sidebar.header('Data Filters')

year_select = sl.sidebar.selectbox("Select the starting year of the season you'd like to explore:", year_list)

# team_select = sl.sidebar.multiselect('Teams', )

positions_array = ['PG', 'SG', 'SF', 'PF', 'C']

select_array = sl.sidebar.multiselect('Positions', positions_array, positions_array)

print(select_array)
print(year_select)