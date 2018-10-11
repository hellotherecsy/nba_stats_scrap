import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

stats_index = ['PLAYER','GP','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV','EFF']
lst = [['1', '72', '35.4', '30.4', '9.0', '20.1', '44.9', '3.7', '10.0', '36.7', '8.7', '10.1', '85.8', '0.6', '4.8', '5.4', '8.8', '1.8', '0.7', '4.4', '30.1']]


print(type(lst))

ss1 = pd.DataFrame( columns=stats_index)
ss2 = pd.DataFrame(lst , columns=stats_index)


ss1 = ss1.append(ss2)

print(ss1)