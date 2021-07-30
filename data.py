import streamlit as sl
import pandas as pd
import numpy as np

"""
    # Check out about 70 years worth of statistics around the NBA!
"""

# def load_data():
#     data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_" + {} + "_per_game.html", header = 0)
#     print(data)
year_list = list(range(1950, 2021))

year_select = sl.sidebar.selectbox("Select the starting year of the season you'd like to explore:", year_list)


data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_" + str(year_select) + "_per_game.html", header=0)

sl.dataframe(data[0])
# showing values from team column
teams_col = data[0].loc[:, "Tm"]

print(teams_col)
# showing values from team column
# team_values = np.array(teams_col.values)
# finally got unique array
teams_list = pd.unique(teams_col)
print(teams_list)

# print(team_values.unique())

sl.sidebar.header('Data Filters')

year_select = sl.sidebar.selectbox("Select the starting year of the season you'd like to explore:", year_list, key="a")

team_select = sl.sidebar.multiselect('Teams', teams_list, teams_list)

positions_array = ['PG', 'SG', 'SF', 'PF', 'C']

select_array = sl.sidebar.multiselect('Positions', positions_array, positions_array)

print(select_array)
print(year_select)