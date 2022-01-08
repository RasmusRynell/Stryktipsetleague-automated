import requests
import json
import unidecode

API_URL = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'

def get_games():
    print("Reading from svenskaspel...", flush=True)
    with requests.get(API_URL) as get_api:
        games = get_api.json()

    if games['draws']:
        # Print games found in API in green
        print("\033[92mFound {} games\033[0m".format(len(games['draws'][0]['drawEvents'])), flush=True)
        games = games['draws'][0]['drawEvents']
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
    else:
        # Print no games found in red text
        print("\033[91mNo games found...\033[0m", flush=True)
        raise SystemExit
        
    return games

def games_are_open():
    with requests.get(API_URL) as get_api:
        api_data = get_api.json()
    return api_data is not []