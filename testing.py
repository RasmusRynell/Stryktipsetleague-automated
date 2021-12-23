

def get_average_odds(odds):
    total_bookmakers = len(odds)
    total_odds_one = 0
    total_odds_x = 0
    total_odds_two = 0
    for key, game_odds in odds.items():
        total_odds_one += (game_odds['one']) / ((game_odds['one']) + (game_odds['two']) + (game_odds['x']))
        total_odds_x += (game_odds['x']) / ((game_odds['one']) + (game_odds['two']) + (game_odds['x']))
        total_odds_two += (game_odds['two']) / ((game_odds['one']) + (game_odds['two']) + (game_odds['x']))
    return {
        'one': total_odds_one / total_bookmakers,
        'x': total_odds_x / total_bookmakers,
        'two': total_odds_two / total_bookmakers
    }

odds = {
    "svenskaSpel/BetRadar": {
        "one": 3.12,
        "x": 3.25,
        "two": 2.39
    },
    "Betsensation": {
        "one": 3.2,
        "x": 3.52,
        "two": 2.36
    },
    "10x10bet": {
        "one": 3.17,
        "x": 3.47,
        "two": 2.34
    },
    "Asianodds": {
        "one": 3.15,
        "x": 3.3,
        "two": 2.42
    },
    "Lasbet": {
        "one": 3.15,
        "x": 3.45,
        "two": 2.33
    },
    "Unibet": {
        "one": 3.2,
        "x": 3.15,
        "two": 2.45
    },
    "Marathonbet": {
        "one": 3.02,
        "x": 3.4,
        "two": 2.42
    },
    "Curebet": {
        "one": 3.12,
        "x": 3.41,
        "two": 2.31
    },
    "GGBET": {
        "one": 2.97,
        "x": 3.36,
        "two": 2.41
    },
    "Betway": {
        "one": 3.1,
        "x": 3.4,
        "two": 2.3
    },
    "Ditobet": {
        "one": 3.06,
        "x": 3.35,
        "two": 2.27
    },
    "WilliamHill": {
        "one": 3.0,
        "x": 3.2,
        "two": 2.38
    },
    "Pinnacle": {
        "one": 3.19,
        "x": 3.22,
        "two": 2.44
    },
    "N1Bet": {
        "one": 2.93,
        "x": 3.28,
        "two": 2.36
    },
    "Coolbet": {
        "one": 3.15,
        "x": 3.2,
        "two": 2.5
    },
    "bwin": {
        "one": 2.95,
        "x": 3.3,
        "two": 2.4
    },
    "Bettilt": {
        "one": 3.1,
        "x": 3.6,
        "two": 2.48
    },
    "Betsson": {
        "one": 3.1,
        "x": 3.4,
        "two": 2.35
    },
    "Betsafe": {
        "one": 3.1,
        "x": 3.4,
        "two": 2.35
    },
    "Betfair": {
        "one": 3.0,
        "x": 3.3,
        "two": 2.3
    },
    "bet365": {
        "one": 3.1,
        "x": 3.4,
        "two": 2.3
    },
    "bet-at-one": {
        "one": 2.9,
        "x": 3.25,
        "two": 2.34
    },
    "1xBet": {
        "one": 3.01,
        "x": 3.4,
        "two": 2.44
    }
}

print(get_average_odds(odds))