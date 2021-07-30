import streamlit as sl
import pandas as pd
import numpy as np

"""
    # Check out about 70 years worth of statistics around the NBA!
"""

year_list = list(range(1950, 2021))

sl.sidebar.header('Data Filters')

year_select = sl.sidebar.selectbox("Select the starting year of the season you'd like to explore:", year_list, key="a")

data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_" + str(year_select) + "_per_game.html", header=0)
data = data[0].drop(['Rk'], axis=1)
# got rid of repeating headers in dataframe
data = data[data['Player'] != 'Player']
# filtering data that has the TOT for the team
data = data[data['Tm'] != 'TOT']

sl.dataframe(data)
# showing values from team column
teams_col = data.loc[:, "Tm"]

print(teams_col)
# showing values from team column
# team_values = np.array(teams_col.values)
# finally got unique array
teams_list = pd.unique(teams_col)
print(teams_list)

# print(team_values.unique())

teams_selected = sl.sidebar.multiselect('Teams', teams_list, teams_list)

positions_array = ['PG', 'SG', 'SF', 'PF', 'C']

positions_selected = sl.sidebar.multiselect('Positions', positions_array, positions_array)

req1 = data["Tm"].isin(teams_selected)
req2 = data["Pos"].isin(positions_selected)

data = data[req1 & req2]