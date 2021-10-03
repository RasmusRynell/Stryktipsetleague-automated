import requests
import json

API_URL = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'

def get_odds():
    with requests.get(API_URL) as get_api:
        api_data = get_api.json()

    def get_match_data(match_id, data_type):
        try:
            return {
                "Home" : api_data['draws'][0]['drawEvents'][match_id][data_type]['one'].replace(',', '.'),
                "Draw" : api_data['draws'][0]['drawEvents'][match_id][data_type]['x'].replace(',', '.'),
                "Away" : api_data['draws'][0]['drawEvents'][match_id][data_type]['two'].replace(',', '.')
            }
        except:
            return {
                "Home" : -1,
                "Draw" : -1,
                "Away" : -1 
            }

    result = {'Odds': {}, 'Folket': {}, 'Tidningar': {}}
    for match_id in range(0, 13):
        result['Odds'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'odds')
        result['Folket'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'svenskaFolket')
        result['Tidningar'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'tioTidningar')


    return result