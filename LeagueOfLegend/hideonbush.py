import requests
import json
from urllib import parse # 한글

api_key = "RGAPI-b01bf1cf-d992-449c-bea5-bf2fe8092529" # 새로 발급받은 api_key
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
# Riot Game Name 검색은 현 닉네임
# Smmunor Name 검색은 생성할 때 쓴 닉네임..
userNickname="상병 박의진"

encodedName = parse.quote(userNickname)
url = f"https://asia.api.riotgames.com/lol/summoner/v4/summoners/by-name/{encodedName}"

player = requests.get(url, headers=REQUEST_HEADERS).json()
player

# {'status': {'message': 'Forbidden', 'status_code': 403}}
# --> 지금은 사용 불가한 API 같음..
userNickname="96년생 티모장인"
tagLine="9202"
encodedName = parse.quote(userNickname)
print(encodedName)
url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encodedName}/{tagLine}"

player_id = requests.get(url, headers=REQUEST_HEADERS).json()

# player_id
# {'puuid': 'MSAtTIHSUgLee-eSOBqa9kzg--UHKgi083trROsPHVGRRYtGRqGGpyXnE-akvJC2HGDsCMcW6bIGEA',
#  'gameName': '96년생 티모장인',
#  'tagLine': '9202'}
puuid = player_id['puuid']
url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
player = requests.get(url, headers=REQUEST_HEADERS).json()

# player
# {'id': 'UUc0mk0pk8Uu-bwls-nzJVB_k90XqMm9H_LsuYTkXjdC764',
#  'accountId': 'Msu1Z9GXgXi9r4l7Q42STeo0owpTmSnQN-1A70O-o2YZ6sE',
#  'puuid': 'MSAtTIHSUgLee-eSOBqa9kzg--UHKgi083trROsPHVGRRYtGRqGGpyXnE-akvJC2HGDsCMcW6bIGEA',
#  'profileIconId': 6637,
#  'revisionDate': 1718379690572,
#  'summonerLevel': 380}
playerInfo = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+player['id'], headers = REQUEST_HEADERS).json();

# playerInfo
# [{'leagueId': '64de9d2d-89e0-3698-a7cd-a9b7e04ef3b6',
#   'queueType': 'RANKED_SOLO_5x5',
#   'tier': 'MASTER',
#   'rank': 'I',
#   'summonerId': 'UUc0mk0pk8Uu-bwls-nzJVB_k90XqMm9H_LsuYTkXjdC764',
#   'leaguePoints': 307,
#   'wins': 120,
#   'losses': 108,
#   'veteran': True,
#   'inactive': False,
#   'freshBlood': False,
#   'hotStreak': False}]

n_wins = playerInfo[0]['wins']
n_losses = playerInfo[0]['losses']
n_total = n_wins + n_losses;
print(n_wins); print(n_losses); print(n_total)

r = n_total // 100
other = n_total % 100

all_gamesID = []
for i in range(r+1):
    start = i*100
    if i != r :
        tmp_gamesID = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{player['puuid']}/ids?type=ranked&start={start}&count={100}", headers = REQUEST_HEADERS).json();
    else :
        tmp_gamesID = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{player['puuid']}/ids?type=ranked&start={start}&count={other}", headers = REQUEST_HEADERS).json();

    all_gamesID.extend(tmp_gamesID)

gameInfo =  requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/"+all_gamesID[0], headers = REQUEST_HEADERS).json();

print(gameInfo)
