from web import scraper
from web import ss
from web import stl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json
import os
import subprocess

# Read config file
with open('config.cfg') as json_data_file:
    config = json.load(json_data_file)

URLS = 'urls.txt'
OUT_FILE = 'out.txt'


options = Options()
options.headless = config['headless']
driver = webdriver.Chrome(config['chrome_driver_path'], options=options)




# # Read data from data.txt
# with open(URLS, 'r') as f:
#     data = f.readlines()

# urls = [obj.replace("\n", "") for obj in data]

# results = scraper.get_odds(urls, driver)


# results_sp = ss.get_odds()
# keys = list(results_sp['Odds'].keys())

# dfs = []
# for index, result in enumerate(results):
#     # create df from json but switch columns and rows
#     df = pd.DataFrame(result)
#     df = df.transpose()

#     df2 = pd.DataFrame(columns = ['Home', 'Draw', 'Away'], index = ['SvenskaSpel', 'Folket', 'Tidningar'])
#     df2.loc['SvenskaSpel'] = list(results_sp['Odds'][keys[index]].values())
#     df2.loc['Folket'] = list(results_sp['Folket'][keys[index]].values())
#     df2.loc['Folket'] = 1/(df2.loc['Folket'].astype(float) / 100)
#     df2.loc['Tidningar'] = list(results_sp['Tidningar'][keys[index]].values())

#     # Add a new row to df with df2
#     df = df.append(df2)
#     dfs.append(df)


# out = []
# for i, df in enumerate(dfs):
#     df_adj = df.copy()
#     df_adj['HomeAdj'] = (1/(df['Home'].astype(float))) / ((1/(df['Home'].astype(float))) + (1/(df['Draw'].astype(float))) + (1/(df['Away'].astype(float))))
#     df_adj['DrawAdj'] = (1/(df['Draw'].astype(float))) / ((1/(df['Draw'].astype(float))) + (1/(df['Away'].astype(float))) + (1/(df['Home'].astype(float))))
#     df_adj['AwayAdj'] = (1/(df['Away'].astype(float))) / ((1/(df['Away'].astype(float))) + (1/(df['Home'].astype(float))) + (1/(df['Draw'].astype(float))))
#     # Drop where id == 'Folket' or 'Tidningar'
#     df_adj = df_adj.drop(df_adj.index[df_adj.index == 'Folket'])
#     df_adj = df_adj.drop(df_adj.index[df_adj.index == 'Tidningar'])

#     out.append(4)
#     out.append(i+1)
#     out.append(df_adj['HomeAdj'].mean())
#     out.append(df_adj['DrawAdj'].mean())
#     out.append(df_adj['AwayAdj'].mean())



# with open(OUT_FILE, 'w') as f:
#     for obj in out:
#         f.write(str(obj))
#         f.write('\n')


# proc = subprocess.Popen(["./a.exe"])
# proc.wait()

# Read out.txt
with open(OUT_FILE, 'r') as f:
    bets = f.readlines()

bets = [bet.replace('\n', '') for bet in bets]

result = {}
for bet in bets:
    key, value = bet.split(':')
    result[key] = value

bets = result

# Pretty print json
print(json.dumps(bets, indent=4))

stl.write_bets(bets, driver, config['login']['email'], config['login']['password'])