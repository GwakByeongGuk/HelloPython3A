import requests
import mysql.connector
from mysql.connector import Error

db_config = {
    'host': '3.35.133.116',
    'database': 'clouds2024',
    'user': 'clouds2024',
    'password': 'clouds2024'
}

item_data_url = "https://ddragon.leagueoflegends.com/cdn/13.15.1/data/en_US/item.json"

def fetch_item_data():
    response = requests.get(item_data_url)
    response.raise_for_status()
    return response.json()

def get_item_name(item_id, item_data):
    return item_data['data'].get(str(item_id), {}).get('name', 'Unknown Item')

def fetch_item_builds_from_db(cursor):
    cursor.execute("SELECT id, item0, item1, item2, item3, item4, item5, item6 FROM item_builds")
    return cursor.fetchall()

def update_item_builds_with_names(cursor, item_builds, item_data):
    update_query = '''
    UPDATE item_builds
    SET item0_name = %s, item1_name = %s, item2_name = %s, item3_name = %s, item4_name = %s, item5_name = %s, item6_name = %s
    WHERE id = %s
    '''
    for build in item_builds:
        id, item0, item1, item2, item3, item4, item5, item6 = build
        item0_name = get_item_name(item0, item_data)
        item1_name = get_item_name(item1, item_data)
        item2_name = get_item_name(item2, item_data)
        item3_name = get_item_name(item3, item_data)
        item4_name = get_item_name(item4, item_data)
        item5_name = get_item_name(item5, item_data)
        item6_name = get_item_name(item6, item_data)
        cursor.execute(update_query, (item0_name, item1_name, item2_name, item3_name, item4_name, item5_name, item6_name, id))

def main():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        item_data = fetch_item_data()
        item_builds = fetch_item_builds_from_db(cursor)
        update_item_builds_with_names(cursor, item_builds, item_data)

        connection.commit()
        print("아이템 이름이 데이터베이스에 저장되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main()
