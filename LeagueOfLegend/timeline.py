import requests
import mysql.connector
from mysql.connector import Error
from datetime import timedelta

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

champion_data_url = "https://ddragon.leagueoflegends.com/cdn/13.15.1/data/en_US/champion.json"

def fetch_champion_data():
    response = requests.get(champion_data_url)
    response.raise_for_status()
    return response.json()

def get_champion_name(champion_id, champion_data):
    for champion in champion_data['data'].values():
        if champion['key'] == str(champion_id):
            return champion['name']
    return 'Unknown Champion'

def fetch_game_timeline(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def convert_timestamp_to_hms(timestamp):
    seconds = timestamp // 1000
    hms = str(timedelta(seconds=seconds))
    return hms

def extract_events(timeline_data, match_id, champion_data, participants):
    events = []
    for frame in timeline_data['info']['frames']:
        for event in frame['events']:
            if event['type'] in ['CHAMPION_KILL', 'BUILDING_KILL']:
                killer_name = get_champion_name(participants.get(event.get('killerId')), champion_data)
                victim_name = get_champion_name(participants.get(event.get('victimId')), champion_data)
                event_time = convert_timestamp_to_hms(event['timestamp'])
                event_data = {
                    'match_id': match_id,
                    'timestamp': event['timestamp'],
                    'event_time': event_time,
                    'event_type': event['type'],
                    'killer_id': event.get('killerId'),
                    'killer_name': killer_name,
                    'victim_id': event.get('victimId'),
                    'victim_name': victim_name,
                    'tower_type': event.get('towerType')
                }
                events.append(event_data)
    return events

def save_events_to_db(cursor, events):
    query = '''
    INSERT INTO match_events (match_id, timestamp, event_time, event_type, killer_id, killer_name, victim_id, victim_name, tower_type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    for event in events:
        cursor.execute(query, (event['match_id'], event['timestamp'], event['event_time'], event['event_type'], event['killer_id'], event['killer_name'], event['victim_id'], event['victim_name'], event['tower_type']))

def fetch_game_info(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def map_participants_by_id(game_info):
    participants = {}
    for participant in game_info['info']['participants']:
        participants[participant['participantId']] = participant['championId']
    return participants

def main():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        champion_data = fetch_champion_data()
        match_ids = ["KR_7170336982"]

        for match_id in match_ids:
            game_info = fetch_game_info(match_id)
            participants = map_participants_by_id(game_info)
            timeline_data = fetch_game_timeline(match_id)
            events = extract_events(timeline_data, match_id, champion_data, participants)
            save_events_to_db(cursor, events)

        connection.commit()
        print("이벤트 정보가 데이터베이스에 저장되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main()
