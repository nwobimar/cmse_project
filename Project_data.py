#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# **.Py file for data manipulation**

# %% [markdown]
# This is a .py file that contains all of the data manipulation that was done to arrange our datasets the way we needed them. For the years 2013-2019 and 2021 you will see the creating of several datasets. Each year has a dataset called: better_seed, worse_seed, final, and combined. Each of these have the respective year at the end of the variable name. Each row of the better_seed and worse_seed dataframes correspond to each other. This is because when you subtract these two dataframes the result is the final dataframe where each row is a game in the NCAA Tournament, and each column is the difference in statistics of the two teams. There is also a column added to the end of these dataframes that involve a 1 or 0 depending on the outcome of the game for the team with the better seed. The combined data frame contains statistics of both teams in the same row, as opposed to taking the difference of their statistics. Near the end of this file, you can see that the we concatenated the dataframes, so that we can use them for training in our model.

# %%
import pandas as pd
import numpy as np


# %%
def add_team(data, team, num): #function to add team to dataset multiple times
    new_data = pd.DataFrame()
    for i in range(0, num):
        new_data = pd.concat([new_data, data[data["TEAM"] == team]], axis = 0)
    return new_data


# %%
cbb13 = pd.read_csv('cbb13.csv')
cbb13 = cbb13.dropna()
cbb13 = cbb13.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
better_seed13 = add_team(cbb13, 'Louisville', 1)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Louisville', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Louisville', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Louisville', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Louisville', 1)], axis = 0) 
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Louisville', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Kansas', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Kansas', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Kansas', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Gonzaga', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Gonzaga', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Indiana', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Indiana', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Indiana', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Duke', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Duke', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Duke', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Georgetown', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Ohio St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Ohio St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Ohio St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Ohio St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Miami FL', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Miami FL', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Miami FL', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Michigan St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Michigan St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Florida', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Florida', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Florida', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Florida', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'New Mexico', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Marquette', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Marquette', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Marquette', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Saint Louis', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Saint Louis', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Michigan', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Michigan', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Kansas St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Syracuse', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Syracuse', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Syracuse', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Oklahoma St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'VCU', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Wisconsin', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'UNLV', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Memphis', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'UCLA', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Arizona', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Arizona', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Butler', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Creighton', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'San Diego St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'San Diego St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Notre Dame', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Illinois', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Colorado St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'North Carolina', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Pittsburgh', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'North Carolina St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Wichita St.', 1)], axis = 0)
better_seed13 = pd.concat([better_seed13, add_team(cbb13,  'Mississippi', 1)], axis = 0)


better_seed13 = better_seed13.reset_index()
better_seed13 = better_seed13.drop(["index"], axis = 1)

# %%
worse_seed13 = add_team(cbb13, 'North Carolina A&T', 1)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Colorado St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Oregon', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Duke', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Wichita St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Michigan', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Western Kentucky', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'North Carolina', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Michigan', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Southern', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Wichita St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'James Madison', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Temple', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Syracuse', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Albany', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Creighton', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Michigan St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Florida Gulf Coast', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Iona', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Iowa St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Arizona', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Wichita St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Pacific', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Illinois', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Marquette', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Valparaiso', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Memphis', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Northwestern St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Minnesota', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Florida Gulf Coast', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Michigan', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Harvard', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Davidson', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Butler', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Syracuse', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'New Mexico St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Oregon', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'South Dakota St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'VCU', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'La Salle', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Montana', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'California', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Michigan', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Oregon', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Akron', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Mississippi', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'California', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, "Saint Mary's", 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Minnesota', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Belmont', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Harvard', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Bucknell', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Cincinnati', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Oklahoma', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Florida Gulf Coast', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Iowa St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Colorado', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Missouri', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Villanova', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Wichita St.', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'Temple', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'La Salle', 1)], axis = 0)
worse_seed13 = pd.concat([worse_seed13, add_team(cbb13, 'La Salle', 1)], axis = 0)


worse_seed13 = worse_seed13.reset_index()
worse_seed13 = worse_seed13.drop(["index"], axis = 1)

# %%
final13 = better_seed13.drop(columns = 'TEAM').subtract(worse_seed13.drop(columns = 'TEAM'))
result = [1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,0]
final13['WIN'] = result

# %%
combined13 = better_seed13
combined13['W_ADJOE'] = worse_seed13['ADJOE']
combined13['W_ADJDE'] = worse_seed13['ADJDE']
combined13['W_BARTHAG'] = worse_seed13['BARTHAG']
combined13['W_EFG_O'] = worse_seed13['EFG_O']
combined13['W_EFG_D'] = worse_seed13['EFG_D']
combined13['W_TOR'] = worse_seed13['TOR']
combined13['W_TORD'] = worse_seed13['TORD']
combined13['W_ORB'] = worse_seed13['ORB']
combined13['W_DRB'] = worse_seed13['DRB']
combined13['W_FTR'] = worse_seed13['FTR']
combined13['W_FTRD'] = worse_seed13['FTRD']
combined13['W_2P_O'] = worse_seed13['2P_O']
combined13['W_2P_D'] = worse_seed13['2P_D']
combined13['W_3P_O'] = worse_seed13['3P_O']
combined13['W_3P_D'] = worse_seed13['3P_D']
combined13['W_ADJ_T'] = worse_seed13['ADJ_T']
combined13['W_WAB'] = worse_seed13['WAB']
combined13['W_SEED'] = worse_seed13['SEED']
combined13 = combined13.drop(columns = ['TEAM'])
combined13['WIN'] = result

# %%
pd.set_option('display.max_rows', 68)
cbb14 = pd.read_csv('cbb14.csv')
cbb14 = cbb14.dropna()
cbb14 = cbb14.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
better_seed14 = cbb14.loc[cbb14['TEAM'] == 'Florida']
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Florida', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Florida', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Florida', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Florida', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Arizona', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Arizona', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Arizona', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Arizona', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Virginia', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Virginia', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Virginia', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wichita St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wichita St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Kansas', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Kansas', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wisconsin', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wisconsin', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wisconsin', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Wisconsin', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Villanova', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Villanova', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Syracuse', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Syracuse', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Creighton', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Creighton', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Iowa St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Iowa St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Iowa St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Duke', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'UCLA', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'UCLA', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'San Diego St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'San Diego St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Michigan St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Louisville', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Louisville', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Louisville', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'VCU', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Oklahoma', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Cincinnati', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Saint Louis', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Ohio St.', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Baylor', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'North Carolina', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Massachusetts', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'New Mexico', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Oregon', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Texas', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Colorado', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Gonzaga', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Memphis', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Stanford', 1)], axis = 0)
better_seed14 = pd.concat([better_seed14, add_team(cbb14, 'Tennessee', 1)], axis = 0)


better_seed14 = better_seed14.reset_index(drop = True)

# %%
worse_seed14 = cbb14.loc[cbb14['TEAM'] == 'Albany']
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Pittsburgh', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'UCLA', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Dayton', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Weber St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Gonzaga', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'San Diego St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Wisconsin', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Coastal Carolina', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Memphis', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Michigan St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Cal Poly', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Eastern Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Stanford', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'American', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Oregon', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Baylor', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Milwaukee', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Wofford', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Texas', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Tennessee', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Western Michigan', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Dayton', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Louisiana Lafayette', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Baylor', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'North Carolina Central', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'North Carolina', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Mercer', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Tulsa', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Stephen F. Austin', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'New Mexico St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'North Dakota St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Delaware', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Harvard', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Connecticut', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Manhattan', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Saint Louis', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Stephen F. Austin', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'North Dakota St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Harvard', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'North Carolina St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Dayton', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Nebraska', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Providence', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Tennessee', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Stanford', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'BYU', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, "Saint Joseph's", 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kentucky', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Arizona St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Pittsburgh', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Oklahoma St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'George Washington', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Kansas St.', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Dayton', 1)], axis = 0)
worse_seed14 = pd.concat([worse_seed14, add_team(cbb14, 'Mercer', 1)], axis = 0)


worse_seed14 = worse_seed14.reset_index(drop = True)

# %%
final14 = better_seed14.drop(columns = 'TEAM').subtract(worse_seed14.drop(columns = 'TEAM'))
result = [1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1]
final14['WIN'] = result

# %%
combined14 = better_seed14
combined14['W_ADJOE'] = worse_seed14['ADJOE']
combined14['W_ADJDE'] = worse_seed14['ADJDE']
combined14['W_BARTHAG'] = worse_seed14['BARTHAG']
combined14['W_EFG_O'] = worse_seed14['EFG_O']
combined14['W_EFG_D'] = worse_seed14['EFG_D']
combined14['W_TOR'] = worse_seed14['TOR']
combined14['W_TORD'] = worse_seed14['TORD']
combined14['W_ORB'] = worse_seed14['ORB']
combined14['W_DRB'] = worse_seed14['DRB']
combined14['W_FTR'] = worse_seed14['FTR']
combined14['W_FTRD'] = worse_seed14['FTRD']
combined14['W_2P_O'] = worse_seed14['2P_O']
combined14['W_2P_D'] = worse_seed14['2P_D']
combined14['W_3P_O'] = worse_seed14['3P_O']
combined14['W_3P_D'] = worse_seed14['3P_D']
combined14['W_ADJ_T'] = worse_seed14['ADJ_T']
combined14['W_WAB'] = worse_seed14['WAB']
combined14['W_SEED'] = worse_seed14['SEED']
combined14 = combined14.drop(columns = ['TEAM'])
combined14['WIN'] = result

# %%
cbb15 = pd.read_csv('cbb15.csv')
cbb15 = cbb15.dropna()
cbb15 = cbb15.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
better_seed15 = add_team(cbb15, "Kentucky", 5)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Villanova", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Duke", 6)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Wisconsin", 4)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Virginia", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Arizona", 3)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Gonzaga", 3)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Kansas", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Iowa St.", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Baylor", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Oklahoma", 3)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Notre Dame", 3)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "North Carolina", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Maryland", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Louisville", 4)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Georgetown", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Utah", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Arkansas", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "West Virginia", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Northern Iowa", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "SMU", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Providence", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Butler", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Xavier", 2)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Michigan St.", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Wichita St.", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Iowa", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "VCU", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Cincinnati", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "Oregon", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "North Carolina St.", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "San Diego St.", 1)], axis = 0)
better_seed15 = pd.concat([better_seed15, add_team(cbb15, "UCLA", 1)], axis = 0)

better_seed15 = better_seed15.reset_index()
better_seed15 = better_seed15.drop(["index"], axis = 1)

# %%
worse_seed15 = add_team(cbb15, "Hampton", 1)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Cincinnati", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "West Virginia", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Notre Dame", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wisconsin", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Lafayette", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "North Carolina St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Robert Morris", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "San Diego St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Utah", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Gonzaga", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Michigan St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wisconsin", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Coastal Carolina", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Oregon", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "North Carolina", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Arizona", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Belmont", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Michigan St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "San Diego St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Texas Southern", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Ohio St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Xavier", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "North Dakota St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Iowa", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "UCLA", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "New Mexico St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wichita St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "UAB", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Georgia St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Albany", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Dayton", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Michigan St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Northeastern", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Butler", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wichita St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Harvard", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Arkansas", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Valparaiso", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "West Virginia", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "UC Irvine", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Northern Iowa", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "North Carolina St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Michigan St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Eastern Washington", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Utah", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Stephen F. Austin", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wofford", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Buffalo", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Wyoming", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "UCLA", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Dayton", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Texas", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Ole Miss", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Georgia St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Georgia", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Indiana", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Davidson", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Ohio St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Purdue", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "Oklahoma St.", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "LSU", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "St. John's", 1)], axis = 0)
worse_seed15 = pd.concat([worse_seed15, add_team(cbb15, "UAB", 1)], axis = 0)

worse_seed15 = worse_seed15.reset_index()
worse_seed15 = worse_seed15.drop(["index"], axis = 1)

# %%
final15 = better_seed15.drop(columns = 'TEAM').subtract(worse_seed15.drop(columns = 'TEAM'))
result = [1,1,1,1,0,
          1,0,
          1,1,1,1,1,1,
          1,1,1,1,
          1,0,
          1,1,1,
          1,1,1,
          1,0,
          0,
          0,
          1,1,0,
          1,1,1,
          1,1,
          1,0,
          1,1,1,0,
          1,0,
          1,
          1,
          1,
          1,
          0,
          0,
          1,
          1,1,
          1,
          1,
          1,
          0,
          1,
          1,
          1,
          1,
          1]
final15['WIN'] = result

# %%
combined15 = better_seed15
combined15['W_ADJOE'] = worse_seed15['ADJOE']
combined15['W_ADJDE'] = worse_seed15['ADJDE']
combined15['W_BARTHAG'] = worse_seed15['BARTHAG']
combined15['W_EFG_O'] = worse_seed15['EFG_O']
combined15['W_EFG_D'] = worse_seed15['EFG_D']
combined15['W_TOR'] = worse_seed15['TOR']
combined15['W_TORD'] = worse_seed15['TORD']
combined15['W_ORB'] = worse_seed15['ORB']
combined15['W_DRB'] = worse_seed15['DRB']
combined15['W_FTR'] = worse_seed15['FTR']
combined15['W_FTRD'] = worse_seed15['FTRD']
combined15['W_2P_O'] = worse_seed15['2P_O']
combined15['W_2P_D'] = worse_seed15['2P_D']
combined15['W_3P_O'] = worse_seed15['3P_O']
combined15['W_3P_D'] = worse_seed15['3P_D']
combined15['W_ADJ_T'] = worse_seed15['ADJ_T']
combined15['W_WAB'] = worse_seed15['WAB']
combined15['W_SEED'] = worse_seed15['SEED']
combined15 = combined15.drop(columns = ['TEAM'])
combined15['WIN'] = result

# %%
cbb16 = pd.read_csv('cbb16.csv')
cbb16 = cbb16.dropna()
cbb16 = cbb16.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
better_seed16 = add_team(cbb16, "Kansas", 4)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "North Carolina", 6)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Virginia", 4)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Oregon", 4)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Michigan St.", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Oklahoma", 4)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Villanova", 3)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Xavier", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "West Virginia", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Miami FL", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Utah", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Texas A&M", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Duke", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "California", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Kentucky", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Iowa St.", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Indiana", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Purdue", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Maryland", 2)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Baylor", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Texas", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Notre Dame", 3)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Arizona", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Seton Hall", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Wisconsin", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Dayton", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Iowa", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Oregon St.", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Texas Tech", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Colorado", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "USC", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Saint Joseph's", 1)], axis = 0)
better_seed16 = pd.concat([better_seed16, add_team(cbb16, "Syracuse", 2)], axis = 0)

better_seed16 = better_seed16.reset_index()
better_seed16 = better_seed16.drop(["index"], axis = 1)

# %%
worse_seed16 = add_team(cbb16, "Austin Peay", 1)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Connecticut", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Maryland", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Villanova", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Florida Gulf Coast", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Providence", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Indiana", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Notre Dame", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Syracuse", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Villanova", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Hampton", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Butler", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Iowa St.", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Villanova", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Syracuse", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Holy Cross", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Saint Joseph's", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Duke", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Oklahoma", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Middle Tennessee", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Cal St. Bakersfield", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "VCU", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Texas A&M", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Villanova", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "UNC Asheville", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Iowa", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Miami FL", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "VCU", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Weber St.", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Wisconsin", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Stephen F. Austin", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Fresno St.", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Gonzaga", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Green Bay", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Northern Iowa", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "UNC Wilmington", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Yale", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Hawaii", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Stony Brook", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Indiana", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Iona", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Arkansas Little Rock", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Chattanooga", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Arkansas Little Rock", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "South Dakota St.", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Hawaii", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Yale", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Northern Iowa", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Michigan", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Stephen F. Austin", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Wisconsin", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Wichita St.", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Gonzaga", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Pittsburgh", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Syracuse", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Temple", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "VCU", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Butler", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Connecticut", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Providence", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Cincinnati", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Middle Tennessee", 1)], axis = 0)
worse_seed16 = pd.concat([worse_seed16, add_team(cbb16, "Gonzaga", 1)], axis = 0)

worse_seed16 = worse_seed16.reset_index()
worse_seed16 = worse_seed16.drop(["index"], axis = 1)

# %%
final16 = better_seed16.drop(columns = 'TEAM').subtract(worse_seed16.drop(columns = 'TEAM'))
result = [1,1,1,0,
          1,1,1,1,1,0,
          1,1,1,0,
          1,1,1,0,
          0,
          1,1,1,0,
          1,1,1,
          1,0,
          0,
          1,1,
          1,0,
          1,1,
          1,1,
          0,
          1,0,
          1,1,
          1,
          0,
          1,1,
          0,
          0,
          1,1,1,
          0,
          0,
          1,
          0,
          1,
          0,
          0,
          0,
          0,
          1,
          1,
          1]
final16['WIN'] = result

# %%
combined16 = better_seed16
combined16['W_ADJOE'] = worse_seed16['ADJOE']
combined16['W_ADJDE'] = worse_seed16['ADJDE']
combined16['W_BARTHAG'] = worse_seed16['BARTHAG']
combined16['W_EFG_O'] = worse_seed16['EFG_O']
combined16['W_EFG_D'] = worse_seed16['EFG_D']
combined16['W_TOR'] = worse_seed16['TOR']
combined16['W_TORD'] = worse_seed16['TORD']
combined16['W_ORB'] = worse_seed16['ORB']
combined16['W_DRB'] = worse_seed16['DRB']
combined16['W_FTR'] = worse_seed16['FTR']
combined16['W_FTRD'] = worse_seed16['FTRD']
combined16['W_2P_O'] = worse_seed16['2P_O']
combined16['W_2P_D'] = worse_seed16['2P_D']
combined16['W_3P_O'] = worse_seed16['3P_O']
combined16['W_3P_D'] = worse_seed16['3P_D']
combined16['W_ADJ_T'] = worse_seed16['ADJ_T']
combined16['W_WAB'] = worse_seed16['WAB']
combined16['W_SEED'] = worse_seed16['SEED']
combined16 = combined16.drop(columns = ['TEAM'])
combined16['WIN'] = result

# %%
s17=pd.read_csv('cbb17.csv')
s18=pd.read_csv('cbb18.csv')
s18=s18.dropna()
s17=s17.dropna()
s17 = s17.drop(columns = ['CONF','G','W','POSTSEASON'])
s18 = s18.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
mod=pd.DataFrame(columns=s17.columns)
mod.columns=s17.columns

lis=('Gonzaga','Gonzaga','Gonzaga','Gonzaga','Gonzaga','Gonzaga','South Carolina','South Carolina','South Carolina','South Carolina',
 'South Carolina','Florida','Florida','Florida','Florida','Xavier','Xavier','Xavier','Xavier','Wisconsin','Wisconsin','Wisconsin','Baylor',
'Baylor','Baylor','West Virginia','West Virginia','West Virginia','Arizona','Arizona','Arizona','Villanova','Villanova','Virginia','Virginia'
 ,'USC','USC','Duke','Duke','Northwestern','Northwestern','Notre Dame','Notre Dame','Florida St.','Florida St.',"Saint Mary's","Saint Mary's",
 "Mount St. Mary's","Virginia Tech","UNC Wilmington","East Tennessee St.","SMU","New Mexico St.","Marquette","Troy",
 'South Dakota St.','Vanderbilt','Princeton','Bucknell','Maryland','Florida Gulf Coast','VCU','North Dakota',
 'North Carolina','North Carolina','North Carolina','North Carolina','North Carolina','North Carolina','Oregon'
 ,'Oregon','Oregon','Oregon','Oregon','Kansas','Kansas','Kansas','Kansas','Kentucky','Kentucky','Kentucky','Kentucky'
 ,'Purdue','Purdue','Purdue','Michigan','Michigan','Michigan','Butler','Butler','Butler','UCLA','UCLA','UCLA','Michigan St.','Michigan St.',
 'Iowa St.','Iowa St.','Rhode Island','Rhode Island','Louisville','Louisville','Arkansas','Arkansas','Middle Tennessee','Middle Tennessee',
 'Cincinnati','Cincinnati','Wichita St.','Wichita St.','UC Davis','Miami FL','Nevada','Vermont','Creighton','Iona','Oklahoma St.','Jacksonville St.',
 'Texas Southern','Seton Hall','Minnesota','Winthrop','Kansas St.','Kent St.','Dayton','Northern Kentucky')

# win=(1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#     1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)


#     ,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

against=('South Dakota St.','Northwestern','West Virginia','Xavier','South Carolina','North Carolina', "Marquette",
        "Duke","Baylor","Florida","Gonzaga","East Tennessee St.","Virginia","Wisconsin",'South Carolina',"Maryland",
        "Florida St.","Arizona","Gonzaga","Virginia Tech","Villanova","Florida","New Mexico St.","USC",'South Carolina',
        "Bucknell","Notre Dame","Gonzaga","North Dakota","Saint Mary's",'Xavier',"Mount St. Mary's",'Wisconsin',"UNC Wilmington",
        "Florida","SMU",'Baylor',"Troy",'South Carolina','Vanderbilt',"Gonzaga",'Princeton',"West Virginia",'Florida Gulf Coast',
        'Xavier','VCU','Arizona','Villanova','Wisconsin','Virginia','Florida','USC','Baylor','South Carolina','Duke','Gonzaga','Northwestern',
        'Notre Dame','West Virginia','Xavier','Florida St.',"Saint Mary's",'Arizona','Texas Southern','Arkansas','Butler','Kentucky',
        'Oregon','Gonzaga','Iona','Rhode Island','Michigan','Kansas','North Carolina','UC Davis','Michigan St.','Purdue','Oregon',
        'Northern Kentucky','Wichita St.','UCLA','North Carolina','Vermont','Iowa St.','Kansas','Oklahoma St.','Louisville',
        'Oregon','Winthrop','Middle Tennessee','North Carolina','Kent St.','Cincinnati','Kentucky','Miami FL','Kansas',
        'Nevada','Purdue','Creighton','Oregon','Jacksonville St.','Michigan','Seton Hall','North Carolina','Minnesota','Butler',
        'Kansas St.','UCLA','Dayton','Kentucky','Kansas','Michigan St.','Iowa St.','Purdue','Rhode Island','Oregon','Michigan',
        'Louisville','North Carolina','Arkansas','Middle Tennessee','Butler','Cincinnati','UCLA','Wichita St.','Kentucky')

mod['TEAM']= lis

# %%
a=s17.drop(columns='TEAM')

for i in range(len(mod)):
    
    
    
    ma=s17.dropna()['TEAM']== lis[i]

    team=a.iloc[s17.dropna()['TEAM'][ma].index[0],:]
    tot=team-a
    
    ba=s17.dropna()['TEAM']==against[i]
    mod.iloc[i,1:]=tot.iloc[s17.dropna()['TEAM'][ba].index[0],:]

# %%
tot.iloc[s17.dropna()['TEAM'][ba].index[0],:]

# %%
ma=s17.dropna()['TEAM']=='South Dakota St.'

s17.dropna()['TEAM'][ma].index[0]

# %%
win=(1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)


mod['WIN']=win

# %%
mod2=pd.DataFrame(columns=s18.columns)
mod2.columns=s18.columns

s18.index=np.arange(0,68,1)
lis2=('Michigan','Michigan','Michigan','Michigan','Michigan','Michigan','Loyola Chicago','Loyola Chicago','Loyola Chicago','Loyola Chicago',
     'Loyola Chicago','Kansas St.','Kansas St.','Kansas St.','Kansas St.','Florida St.','Florida St.','Florida St.','Florida St.',
      'Kentucky','Kentucky','Kentucky','Nevada','Nevada','Nevada','Gonzaga','Gonzaga','Gonzaga','Texas A&M','Texas A&M','Texas A&M',
      'UMBC','UMBC','Buffalo','Buffalo','Tennessee','Tennessee','Cincinnati','Cincinnati','Xavier','Xavier','Ohio St.','Ohio St.',
      'Houston','Houston','North Carolina','North Carolina','Virginia','Creighton','Davidson','Arizona','Miami FL','Wright St.',
      'Texas','Georgia St.','Texas Southern','Missouri','South Dakota St.','UNC Greensboro','San Diego St.','Montana','Providence','Lipscomb',
      'Villanova','Villanova','Villanova','Villanova','Villanova','Villanova','Kansas','Kansas','Kansas','Kansas','Kansas','Texas Tech',
      'Texas Tech','Texas Tech','Texas Tech','Duke','Duke','Duke','Duke','West Virginia','West Virginia','West Virginia',
      'Purdue','Purdue','Purdue','Clemson','Clemson','Clemson','Syracuse','Syracuse','Syracuse','Alabama','Alabama',
      'Marshall','Marshall','Florida','Florida','Butler','Butler','Seton Hall','Seton Hall','Auburn','Auburn','Michigan St.','Michigan St.',
      'Rhode Island','Rhode Island','Radford','Virginia Tech','Murray St.','Wichita St.','St. Bonaventure','Stephen F. Austin','Arkansas',
      'Cal St. Fullerton','Penn','North Carolina St.','New Mexico St.','College of Charleston','TCU','Bucknell','Oklahoma','Iona'
      )

against2=('Montana','Houston','Texas A&M','Florida St.','Loyola Chicago','Villanova','Miami FL','Tennessee','Nevada','Kansas St.',
        'Michigan','Creighton','UMBC','Kentucky','Loyola Chicago','Missouri','Xavier','Gonzaga','Michigan','Davidson','Buffalo'
        ,'Kansas St.','Texas','Cincinnati','Loyola Chicago','UNC Greensboro','Ohio St.','Florida St.','Providence','North Carolina','Michigan',
        'Virginia','Kansas St.','Arizona','Kentucky','Wright St.','Loyola Chicago','Georgia St.','Nevada','Texas Southern','Florida St.',
        'South Dakota St.','Gonzaga','San Diego St.','Houston','Lipscomb','Texas A&M','UMBC','Kansas St.','Kentucky','Buffalo',
        'Loyola Chicago','Tennessee','Nevada','Cincinnati','Xavier','Florida St.','Ohio St.','Gonzaga','Houston','Michigan',
        'Texas A&M','North Carolina','Radford','Alabama','West Virginia','Texas Tech','Kansas','Michigan','Penn','Seton Hall','Clemson','Duke','Villanova',
         'Stephen F. Austin','Florida','Purdue','Villanova','Iona','Rhode Island','Syracuse','Kansas','Murray St.','Marshall',
         'Villanova','Cal St. Fullerton','Butler','Texas Tech','New Mexico St.','Auburn','Kansas','TCU','Michigan St.','Duke',
         'Virginia Tech','Villanova','Wichita St.','West Virginia','St. Bonaventure','Texas Tech','Arkansas','Purdue','North Carolina St.',
         'Kansas','College of Charleston','Clemson','Bucknell','Michigan St.','Oklahoma','Duke','Villanova','Alabama',
         'West Virginia','Marshall','Florida','Texas Tech','Butler','Purdue','Kansas','Seton Hall','Clemson','Auburn','Syracuse',
         'Michigan St.','Rhode Island','Duke')

mod2['TEAM']= lis2

# %%
ma=s18.dropna()['TEAM']== 'Montana'

s18.dropna()['TEAM'][ma].index[0]

# %%
a=s18.drop(columns='TEAM')

for i in range(len(mod2)):
    
    
    
    ma=s18.dropna()['TEAM']== lis2[i]

    team=a.iloc[s18.dropna()['TEAM'][ma].index[0],:]
    tot=team-a
    
    ba=s18.dropna()['TEAM']==against2[i]
    mod2.iloc[i,1:]=tot.iloc[s18.dropna()['TEAM'][ba].index[0],:]

# %%
win=(1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)


mod2['WIN']=win

# %%
final1718 = mod2.drop(columns = ['TEAM'])

# %%
cbb19 = pd.read_csv('cbb19.csv')
cbb19 = cbb19.dropna()
cbb19 = cbb19.drop(columns = ['CONF','G','W','POSTSEASON'])

# %%
better_seed19 = cbb19.loc[cbb19['TEAM'] == 'Duke']
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Duke', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Duke', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Duke', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Gonzaga', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Gonzaga', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Gonzaga', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Gonzaga', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'North Carolina', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'North Carolina', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'North Carolina', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kentucky', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kentucky', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kentucky', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kentucky', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Tennessee', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Tennessee', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Tennessee', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Michigan St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'LSU', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'LSU', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Purdue', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Purdue', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Houston', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Houston', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kansas', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kansas', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Kansas St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Florida St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Florida St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia Tech', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Virginia Tech', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Auburn', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Wisconsin', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Oregon', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Marquette', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Mississippi St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Maryland', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Buffalo', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Villanova', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Iowa St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Wofford', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Utah St.', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Cincinnati', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Mississippi', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Nevada', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Syracuse', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'Louisville', 1)], axis = 0)
better_seed19 = pd.concat([better_seed19, add_team(cbb19, 'VCU', 1)], axis = 0)


better_seed19 = better_seed19.reset_index(drop = True)

# %%
worse_seed19 = cbb19.loc[cbb19['TEAM'] == 'North Dakota St.']
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'UCF', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Virginia Tech', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Michigan St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Fairleigh Dickinson', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Baylor', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Florida St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Gardner Webb', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Oklahoma', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Oregon', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Purdue', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Auburn', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Iona', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Washington', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Auburn', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Abilene Christian', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Wofford', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Houston', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Auburn', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Colgate', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Iowa', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Purdue', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Montana', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Florida', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Bradley', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Minnesota', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'LSU', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Texas Tech', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Yale', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Maryland', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Northern Kentucky', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Buffalo', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Old Dominion', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Villanova', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Georgia St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Ohio St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Northeastern', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Auburn', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'UC Irvine', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Vermont', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Murray St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Saint Louis', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Liberty', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'New Mexico St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Oregon', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'UC Irvine', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Murray St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Liberty', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Belmont', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Arizona St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, "Saint Mary's", 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Ohio St.', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Seton Hall', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Washington', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Iowa', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Oklahoma', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Florida', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Baylor', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'Minnesota', 1)], axis = 0)
worse_seed19 = pd.concat([worse_seed19, add_team(cbb19, 'UCF', 1)], axis = 0)


worse_seed19 = worse_seed19.reset_index(drop = True)

# %%
final19 = better_seed19.drop(columns = 'TEAM').subtract(worse_seed19.drop(columns = 'TEAM'))
result = [1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0]
final19["WIN"] = result

# %%
combined19 = better_seed19
combined19['W_ADJOE'] = worse_seed19['ADJOE']
combined19['W_ADJDE'] = worse_seed19['ADJDE']
combined19['W_BARTHAG'] = worse_seed19['BARTHAG']
combined19['W_EFG_O'] = worse_seed19['EFG_O']
combined19['W_EFG_D'] = worse_seed19['EFG_D']
combined19['W_TOR'] = worse_seed19['TOR']
combined19['W_TORD'] = worse_seed19['TORD']
combined19['W_ORB'] = worse_seed19['ORB']
combined19['W_DRB'] = worse_seed19['DRB']
combined19['W_FTR'] = worse_seed19['FTR']
combined19['W_FTRD'] = worse_seed19['FTRD']
combined19['W_2P_O'] = worse_seed19['2P_O']
combined19['W_2P_D'] = worse_seed19['2P_D']
combined19['W_3P_O'] = worse_seed19['3P_O']
combined19['W_3P_D'] = worse_seed19['3P_D']
combined19['W_ADJ_T'] = worse_seed19['ADJ_T']
combined19['W_WAB'] = worse_seed19['WAB']
combined19['W_SEED'] = worse_seed19['SEED']
combined19 = combined19.drop(columns = ['TEAM'])
combined19['WIN'] = result

# %%
frames = [final13, final14, final15, final16, final19]
frames2 = [combined13, combined14, combined15, combined16, combined19]
final = pd.concat(frames)
combined = pd.concat(frames2)

# %%
cbb21 = pd.read_csv('cbb21.csv')
cbb21 = cbb21.dropna()
cbb21 = cbb21.drop(columns = ['CONF','G','W'])

# %%
better_seed21 = cbb21.loc[cbb21['TEAM'] == 'Gonzaga']
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Gonzaga', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Gonzaga', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Gonzaga', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Gonzaga', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Baylor', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Michigan', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Michigan', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Michigan', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Michigan', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Illinois', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Illinois', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Iowa', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Iowa', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Ohio St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Alabama', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Alabama', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Alabama', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Houston', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Houston', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Houston', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Houston', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Kansas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Kansas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Arkansas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Arkansas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Arkansas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Texas', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'West Virginia', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'West Virginia', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Virginia', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Purdue', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Florida St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Florida St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Oklahoma St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Oklahoma St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Creighton', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Creighton', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Villanova', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Villanova', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Colorado', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Tennessee', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'USC', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'USC', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Texas Tech', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'BYU', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'San Diego St.', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Oregon', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Florida', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Florida', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Connecticut', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Clemson', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Oklahoma', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'North Carolina', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'LSU', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Loyola Chicago', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'Loyola Chicago', 1)], axis = 0)
better_seed21 = pd.concat([better_seed21, add_team(cbb21, 'UCLA', 1)], axis = 0)


better_seed21 = better_seed21.reset_index(drop = True)

# %%
worse_seed21 = cbb21.loc[cbb21['TEAM'] == 'Norfolk St.']
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oklahoma', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Creighton', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'USC', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UCLA', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Hartford', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Wisconsin', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Villanova', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Arkansas', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Houston', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Gonzaga', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Texas Southern', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'LSU', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Florida St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UCLA', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Drexel', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Loyola Chicago', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Grand Canyon', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oral Roberts', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Iona', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Maryland', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UCLA', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Cleveland St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Rutgers', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Syracuse', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Eastern Washington', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'USC', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Colgate', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Texas Tech', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oral Roberts', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Abilene Christian', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Morehead St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Syracuse', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Ohio', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'North Texas', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UNC Greensboro', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Colorado', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Liberty', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UC Santa Barbara', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Ohio', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Winthrop', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'North Texas', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Georgetown', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Drake', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Utah St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'UCLA', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Syracuse', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'VCU', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Virginia Tech', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oral Roberts', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Maryland', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Rutgers', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Missouri', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Wisconsin', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'St. Bonaventure', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Georgia Tech', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Oregon St.', 1)], axis = 0)
worse_seed21 = pd.concat([worse_seed21, add_team(cbb21, 'Abilene Christian', 1)], axis = 0)


worse_seed21 = worse_seed21.reset_index(drop = True)

# %%
final21 = better_seed21.drop(columns = 'TEAM').subtract(worse_seed21.drop(columns = 'TEAM'))
result21 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1]
#final21["WIN"] = result

# %%
combined21 = better_seed21
combined21['W_ADJOE'] = worse_seed21['ADJOE']
combined21['W_ADJDE'] = worse_seed21['ADJDE']
combined21['W_BARTHAG'] = worse_seed21['BARTHAG']
combined21['W_EFG_O'] = worse_seed21['EFG_O']
combined21['W_EFG_D'] = worse_seed21['EFG_D']
combined21['W_TOR'] = worse_seed21['TOR']
combined21['W_TORD'] = worse_seed21['TORD']
combined21['W_ORB'] = worse_seed21['ORB']
combined21['W_DRB'] = worse_seed21['DRB']
combined21['W_FTR'] = worse_seed21['FTR']
combined21['W_FTRD'] = worse_seed21['FTRD']
combined21['W_2P_O'] = worse_seed21['2P_O']
combined21['W_2P_D'] = worse_seed21['2P_D']
combined21['W_3P_O'] = worse_seed21['3P_O']
combined21['W_3P_D'] = worse_seed21['3P_D']
combined21['W_ADJ_T'] = worse_seed21['ADJ_T']
combined21['W_WAB'] = worse_seed21['WAB']
combined21['W_SEED'] = worse_seed21['SEED']
combined21 = combined21.drop(columns = ['TEAM'])
#combined21['WIN'] = result
