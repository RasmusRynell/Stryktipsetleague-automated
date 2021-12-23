from web import scraper
from web import oddsPortal
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

# Get games
games = ss.get_games()

# Request odds for all games
oddsPortal.fill_with_odds(games, driver, config['login_op']['username'], config['login_op']['password'])

with open(OUT_FILE, 'w') as f:
    for i, game in enumerate(games):
        f.write(str(4))
        f.write('\n')
        f.write(str(i+1))
        f.write('\n')
        f.write(str(game['odds_info']['avr_odds']['one']))
        f.write('\n')
        f.write(str(game['odds_info']['avr_odds']['x']))
        f.write('\n')
        f.write(str(game['odds_info']['avr_odds']['two']))
        f.write('\n')


proc = subprocess.Popen(["./a.exe"])
proc.wait()

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

stl.write_bets(bets, driver, config['login_stl']['email'], config['login_stl']['password'])

driver.quit()