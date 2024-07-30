import requests
import json
import mysql.connector
from mysql.connector import Error

api_key = "RGAPI-b01bf1cf-d992-449c-bea5-bf2fe8092529"
headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Riot-Token": api_key
}

db_config = {
    'host': '3.35.133.116',
    'database': 'clouds2024',
    'user': 'clouds2024',
    'password': 'clouds2024'
}

def fetch_game_info(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def extract_item_builds(game_info, match_id):
    item_builds = []
    for participant in game_info['info']['participants']:
        player_build = (
            match_id,
            participant['summonerName'],
            participant['championName'],
            participant['item0'],
            participant['item1'],
            participant['item2'],
            participant['item3'],
            participant['item4'],
            participant['item5'],
            participant['item6']
        )
        item_builds.append(player_build)
    return item_builds

def read_match_ids(filename):
    with open(filename, 'r') as f:
        match_ids = [line.strip() for line in f.readlines()]
    return match_ids

def save_item_builds_to_db(cursor, item_builds):
    query = '''
    INSERT INTO item_builds (match_id, summonerName, championName, item0, item1, item2, item3, item4, item5, item6)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    for build in item_builds:
        cursor.execute(query, build)

def main():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        match_ids = read_match_ids("match_ids.txt")

        for match_id in match_ids:
            game_info = fetch_game_info(match_id)
            item_builds = extract_item_builds(game_info, match_id)
            save_item_builds_to_db(cursor, item_builds)

        connection.commit()
        print("아이템 빌드 정보가 데이터베이스에 저장되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main()
