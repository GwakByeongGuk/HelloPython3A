import requests
import json

api_key = "RGAPI-b01bf1cf-d992-449c-bea5-bf2fe8092529"
headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Riot-Token": api_key
}

def fetch_game_info(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def extract_item_builds(game_info):
    item_builds = []
    for participant in game_info['info']['participants']:
        player_build = {
            "summonerName": participant['summonerName'],
            "championName": participant['championName'],
            "items": [
                participant['item0'],
                participant['item1'],
                participant['item2'],
                participant['item3'],
                participant['item4'],
                participant['item5'],
                participant['item6']
            ]
        }
        item_builds.append(player_build)
    return item_builds

match_id = "KR_7170336982"
game_info = fetch_game_info(match_id)
item_builds = extract_item_builds(game_info)

print(json.dumps(item_builds, indent=2))


