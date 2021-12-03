import requests
import json
import unidecode
from google_trans_new import google_translator

API_URL = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'

def get_games_and_odds():
    games = []
    with requests.get(API_URL) as get_api:
        api_data = get_api.json()

    translator = google_translator()
    print(translator.translate("Hola Mundo", dest="ar"))

    for match_id in range(0, 13):
        games.append({
            'Event' : unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['eventDescription'])

            # 'HomeCountryName ' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][0]['countryName']), lang_tgt='en'),
            # 'HomeMediumName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][0]['mediumName']), lang_tgt='en'),
            # 'HomeName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][0]['name']), lang_tgt='en'),
            # 'HomeShortName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][0]['shortName']), lang_tgt='en'),
            # 'AwayCountryName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][1]['countryName']), lang_tgt='en'),
            # 'AwayMediumName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][1]['mediumName']), lang_tgt='en'),
            # 'AwayName' : translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][1]['name']), lang_tgt='en'),
            # 'AwayShortName' :  translator.translate(unidecode.unidecode(api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][1]['shortName']), lang_tgt='en') if \
            #     'shortName' in api_data['draws'][0]['drawEvents'][match_id]['match']['participants'][1] else '',
            
            # 'HomeOdds' : api_data['draws'][0]['drawEvents'][match_id]['odds']['one'],
            # 'DrawOdds' : api_data['draws'][0]['drawEvents'][match_id]['odds']['x'],
            # 'AwayOdds' : api_data['draws'][0]['drawEvents'][match_id]['odds']['two'],

            # 'HomeFolket' : api_data['draws'][0]['drawEvents'][match_id]['svenskaFolket']['one'],
            # 'DrawFolket' : api_data['draws'][0]['drawEvents'][match_id]['svenskaFolket']['x'],
            # 'AwayFolket' : api_data['draws'][0]['drawEvents'][match_id]['svenskaFolket']['two'],
            # 'HomeTidningar' : api_data['draws'][0]['drawEvents'][match_id]['tioTidningarsTips']['one'],
            # 'DrawTidningar' : api_data['draws'][0]['drawEvents'][match_id]['tioTidningarsTips']['x'],
            # 'AwayTidningar' : api_data['draws'][0]['drawEvents'][match_id]['tioTidningarsTips']['two']
        })

    print(json.dumps(games, indent=4, sort_keys=True))

def get_odds():
    with requests.get(API_URL) as get_api:
        api_data = get_api.json()

        # Pritty print the data
        print(json.dumps(api_data, indent=4, sort_keys=True))

    def get_match_data(match_id, data_type):
        try:
            return {
                "Home" : api_data['draws'][0]['drawEvents'][match_id][data_type]['one'].replace(',', '.'),
                "Draw" : api_data['draws'][0]['drawEvents'][match_id][data_type]['x'].replace(',', '.'),
                "Away" : api_data['draws'][0]['drawEvents'][match_id][data_type]['two'].replace(',', '.')
            }
        except:
            return {
                "Home" : 0,
                "Draw" : 0,
                "Away" : 0 
            }

    result = {'Odds': {}, 'Folket': {}, 'Tidningar': {}}
    for match_id in range(0, 13):
        result['Odds'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'odds')
        result['Folket'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'svenskaFolket')
        result['Tidningar'][api_data['draws'][0]['drawEvents'][match_id]['eventDescription']] = get_match_data(match_id, 'tioTidningar')


    return result