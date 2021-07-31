import streamlit as sl
import pandas as pd
import numpy as np
import base64

"""
    # Check out about 70 years worth of statistics around the NBA!
"""

year_list = list(range(1950, 2021))

sl.sidebar.header('Data Filters')

year_select = sl.sidebar.selectbox("Select the starting year of the season you'd like to explore:", year_list, key="a")

data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_" + str(year_select) + "_per_game.html", header=0)
data = data[0].drop(['Rk'], axis=1)

# showing values from team column
teams_col = data.loc[:, "Tm"]
print(teams_col)
# finally got unique array
teams_list = pd.unique(teams_col)

print(teams_list)

teams_selected = sl.sidebar.multiselect('Teams', teams_list, teams_list)

positions_array = ['PG', 'SG', 'SF', 'PF', 'C']

positions_selected = sl.sidebar.multiselect('Positions', positions_array, positions_array)


req1 = data["Tm"].isin(teams_selected)
req2 = data["Pos"].isin(positions_selected)

data = data[req1 & req2]
# got rid of repeating headers in dataframe
data = data[data['Player'] != 'Player']
# filtering data that has the TOT for the team
data = data[data['Tm'] != 'TOT']

sl.dataframe(data)

print(teams_col)
# showing values from team column
# team_values = np.array(teams_col.values)

def download_csv_file(data):
    file = data.to_csv(index=False)
    b64 = base64.b64encode(file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download file</a>'
    return href

sl.markdown(download_csv_file(data), unsafe_allow_html=True)

# df = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])

# sl.vega_lite_chart(df, {
#     'mark': {'type': 'circle', 'tooltip': True},
#     'encoding': {
#         'x': {'field': 'a', 'type': 'quantitative'},
#         'y': {'field': 'b', 'type': 'quantitative'},
#         'size': {'field': 'c', 'type': 'quantitative'},
#         'color': {'field': 'c', 'type': 'quantitative'},
#     },
# })

"""
    # Top 100 NBA Player Data in Points Per Game (PPG)
"""
def get_top_100(data):
    # data.PTS = pd.to_numeric(data.PTS, errors='coerce')
    data['PTS'] = data['PTS'].astype(float)
    top100data = data.sort_values(by=['PTS'], ascending=False) 
    top100data['PTS'] = data['PTS'].astype(str)
    top100data = top100data.head(100)
    sl.dataframe(top100data)

get_top_100(data)