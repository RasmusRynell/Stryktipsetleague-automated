import json

with open('./translation/names.txt', 'r') as f:
    team_names = json.load(f)
    # Set all team names and their translations to lowercase
    team_names = {k.lower(): v.lower() for k, v in team_names.items()}

def translate_team_name(name):
    return team_names[name.lower()] if name.lower() in team_names else name