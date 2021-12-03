import requests
import json
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

STRYKTIPSET_URL = 'https://spela.svenskaspel.se/stryktipset'
ODDS_PORTAL_LOGIN_URL = 'https://www.oddsportal.com/login'
ODDS_PORTAL_MAIN = 'https://www.oddsportal.com/'

def scrape_games_and_odds(driver, odds_portal_username_input, odds_portal_password_input):
    
    # Open all pages needed in different tabs
    open_tabs(13, driver)

    # Get the games and svenska spels odds from the stryktipset page
    games, odds = get_games(driver)


    

def open_tabs(number_of_tabs, driver):
    driver.get(STRYKTIPSET_URL)
    driver.execute_script(f"window.open('{ODDS_PORTAL_LOGIN_URL}', '_blank');")
    for i in range(1, number_of_tabs):
        driver.execute_script(f"window.open('{ODDS_PORTAL_MAIN}');")


def get_games(driver):
    df = pd.DataFrame(columns=['game_id', 'display_name', 'home_team', 'away_team'])