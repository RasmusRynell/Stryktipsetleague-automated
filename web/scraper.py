import json
import os
from threading import Thread
from tqdm import tqdm


def get_odds(urls, driver):
    result = []

    log_in(driver)
    for url in tqdm(urls):
        result.append(get_odds_from_site(url, driver))

    driver.quit()
    return result


def get_odds_from_site(url, driver):
    driver.get(url)

    # Get from id 'odds-data-table'
    odds_table = driver.find_element_by_id('odds-data-table')

    # Get all element by class 'table-main detail-odds sortable
    odds_table_main = odds_table.find_elements_by_class_name('detail-odds')[0]

    # Get first tbody
    odds_table_body = odds_table_main.find_elements_by_tag_name('tbody')[0]
    odds = []
    # loop trought all tr and add a dict to odds
    for tr in odds_table_body.find_elements_by_tag_name('tr'):
        odds.append(dict(zip(['Site', 'Home', 'Draw', 'Away'], [td.text for td in tr.find_elements_by_tag_name('td')])))

    odds_cleaned = {}
    for odd in odds[:-1]:
        site = odd['Site'].replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')
        odds_cleaned[site] = {
            'Home': float(odd['Home']),
            'Draw': float(odd['Draw']),
            'Away': float(odd['Away'])
        }
    return odds_cleaned

def log_in(driver):
    driver.get('https://www.oddsportal.com/login')

    # press login button with xpath '/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[3]/button'
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[6]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/form/div[3]/button').click()
