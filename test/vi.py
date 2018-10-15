

import numpy as np
import pandas as pd
import re
import math
import seaborn as sns
import matplotlib.pyplot as plt

names = pd.read_csv("../data/nba_players_traditional_names.csv")
stats = pd.read_csv("../data/nba_players_traditional_stats.csv")

new = pd.concat([names, stats], axis=1)
new.to_csv("../data/nba_players_traditional_stats_new.csv", mode='w',index=False)

