import requests
import json
import unidecode

API_URL = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'

def get_games():
    with requests.get(API_URL) as get_api:
        games = get_api.json()['draws'][0]['drawEvents']
        
    for game in games:
        game['odds'] = {
            f"svenskaSpel/{game['providerIds'][0]['provider']}": {key:float(value.replace(",", ".")) for key, value in game['odds'].items()}
        }
        game['odds_info'] = {
            'svenskaFolket': game['odds']['svenskaSpel/BetRadar'],
            'start': game['startOdds'],
            'favorite': game['favouriteOdds'],
            'tioTidningar': game['tioTidningarsTips'],
        }
        del game['svenskaFolket']
        del game['startOdds']
        del game['favouriteOdds']
        del game['tioTidningarsTips']
    return games