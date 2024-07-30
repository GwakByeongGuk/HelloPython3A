import requests
import mysql.connector
from mysql.connector import Error
from urllib import parse
from datetime import datetime, timezone

api_key = "RGAPI-b01bf1cf-d992-449c-bea5-bf2fe8092529"
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

db_config = {
    'host': '3.35.133.116',
    'database': 'clouds2024',
    'user': 'clouds2024',
    'password': 'clouds2024'
}

def unix_to_readable(timestamp):
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def get_game_ids(puuid, start=0, count=50):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start={start}&count={count}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    response.raise_for_status()
    return response.json()

def get_game_info(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=REQUEST_HEADERS)
    response.raise_for_status()
    return response.json()

def save_matches_to_db(cursor, matches):
    query = '''
    INSERT INTO matches (id, gameCreation, gameDuration, gameEndTimestamp, gameMode, gameVersion, mapId, participantId, championId, championName, kills, deaths, assists, totalDamageDealt, totalDamageTaken, win)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        gameCreation = VALUES(gameCreation),
        gameDuration = VALUES(gameDuration),
        gameEndTimestamp = VALUES(gameEndTimestamp),
        gameMode = VALUES(gameMode),
        gameVersion = VALUES(gameVersion),
        mapId = VALUES(mapId),
        participantId = VALUES(participantId),
        championId = VALUES(championId),
        championName = VALUES(championName),
        kills = VALUES(kills),
        deaths = VALUES(deaths),
        assists = VALUES(assists),
        totalDamageDealt = VALUES(totalDamageDealt),
        totalDamageTaken = VALUES(totalDamageTaken),
        win = VALUES(win);
    '''

    for match in matches:
        match_info = match['info']
        participants = match_info['participants']

        for participant in participants:
            values = (
                match['metadata']['matchId'],
                match_info['gameCreation'],
                match_info['gameDuration'],
                match_info['gameEndTimestamp'],
                match_info['gameMode'],
                match_info['gameVersion'],
                match_info['mapId'],
                participant['participantId'],
                participant['championId'],
                participant['championName'],
                participant['kills'],
                participant['deaths'],
                participant['assists'],
                participant['totalDamageDealt'],
                participant['totalDamageTaken'],
                participant['win']
            )
            cursor.execute(query, values)

def save_match_ids_to_file(match_ids, filename):
    with open(filename, 'w') as f:
        for match_id in match_ids:
            f.write(f"{match_id}\n")

def main():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        userNickname = "96년생 티모장인"
        tagLine = "9202"
        encodedName = parse.quote(userNickname)
        url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encodedName}/{tagLine}"
        player_id = requests.get(url, headers=REQUEST_HEADERS).json()

        puuid = player_id['puuid']

        game_ids = get_game_ids(puuid, start=0, count=50)

        # 매치 ID를 파일에 저장
        save_match_ids_to_file(game_ids, "match_ids.txt")

        matches = [get_game_info(game_id) for game_id in game_ids]

        save_matches_to_db(cursor, matches)
        connection.commit()
        print("게임 정보가 데이터베이스에 저장되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main()
