from tqdm import tqdm
from translation import translate
import json
import time
from selenium.webdriver.common.by import By



def fill_with_odds(games, driver, username_input, password_input):
    log_in(driver, username_input, password_input)
    for game in tqdm(games):
        # Get url for game
        home_team_name = str(translate.translate_team_name(game['match']['participants'][0]['name'])).replace(' ', '%20')
        away_team_name = str(translate.translate_team_name(game['match']['participants'][1]['name'])).replace(' ', '%20')
        url = f"https://www.oddsportal.com/search/{home_team_name}%20-%20{away_team_name}/"
        
        # Go to site
        driver.get(url)
        # Wait for odds to load
        driver.implicitly_wait(1)

        if game['eventComment']:
            game['odds_info']['avr_odds'] = {
                'one': (float(game['eventComment'].split(": ")[-1].split("-")[0]))/100,
                'x': (float(game['eventComment'].split(": ")[-1].split("-")[1]))/100,
                'two': (float(game['eventComment'].split(": ")[-1].split("-")[2]))/100
            }
        else:
            # Get odds for game
            try:
                url_to_game = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/table[2]/tbody/tr[2]/td[2]/a').get_attribute('href')
                if url_to_game == 'javascript:void(0);':
                    url_to_game = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div/table[2]/tbody/tr[2]/td[2]/a[2]').get_attribute('href')
            except Exception as e:
                print(f"Could not find game for {game['match']['participants'][0]['name']} - {game['match']['participants'][1]['name']}")
                raise(e)

            game['odds'].update(get_odds_from_site(url_to_game, driver))
            game['odds_info']['avr_odds'] = get_average_odds(game['odds'])

def get_average_odds(odds):
    total_bookmakers = len(odds)
    total_odds_one = 0
    total_odds_x = 0
    total_odds_two = 0
    for key, game_odds in odds.items():
        total_odds_one += (1/float(game_odds['one'])) / ((1/float(game_odds['one'])) + (1/float(game_odds['two'])) + (1/float(game_odds['x'])))
        total_odds_x += (1/float(game_odds['x'])) / ((1/float(game_odds['one'])) + (1/float(game_odds['two'])) + (1/float(game_odds['x'])))
        total_odds_two += (1/float(game_odds['two'])) / ((1/float(game_odds['one'])) + (1/float(game_odds['two'])) + (1/float(game_odds['x'])))
    return {
        'one': total_odds_one / total_bookmakers,
        'x': total_odds_x / total_bookmakers,
        'two': total_odds_two / total_bookmakers
    }


def get_odds_from_site(url, driver):
    if url == 'NONE':
        return {}
    driver.get(url)

    # Get from id 'odds-data-table'
    odds_table = driver.find_element(By.ID, 'odds-data-table')

    # Get all element by class 'table-main detail-odds sortable
    odds_table_main = odds_table.find_elements(By.CLASS_NAME, 'detail-odds')[0]

    # Get first tbody
    odds_table_body = odds_table_main.find_elements(By.TAG_NAME, 'tbody')[0]

    odds = [
        dict(
            zip(
                ['Site', 'Home', 'Draw', 'Away'],
                [td.text for td in tr.find_elements(By.TAG_NAME, 'td')],
            )
        )
        for tr in odds_table_body.find_elements(By.TAG_NAME, 'tr')
    ]

    odds_cleaned = {}
    for odd in odds[:-1]:
        site = odd['Site'].replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')
        odds_cleaned[site] = {
            'one': float(odd['Home']),
            'x': float(odd['Draw']),
            'two': float(odd['Away'])
        }
    return odds_cleaned



def log_in(driver, username_input='', password_input=''):
    driver.get('https://www.oddsportal.com/login')

    # Check if cookies clickable and if so, accept them
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div/button[1]').click()
    except:
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/button[1]').click()
        except:
            print("Did not work...", flush=True)

    # Find and write username_input to '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/input'
    username = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[1]/div[2]/input')
    username.send_keys(username_input)

    # Find and write password_input to '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[2]/div[2]/input'
    password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[2]/div[2]/input')
    password.send_keys(password_input)

    # press login button with xpath '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[3]/button'
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[3]/button').click()

