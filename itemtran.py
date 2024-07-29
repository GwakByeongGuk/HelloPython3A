import requests

item_data_url = "https://ddragon.leagueoflegends.com/cdn/13.15.1/data/en_US/item.json"

def fetch_item_data():
    response = requests.get(item_data_url)
    response.raise_for_status()
    return response.json()

def get_item_name(item_id, item_data):
    return item_data['data'].get(str(item_id), {}).get('name', 'Unknown Item')

item_data = fetch_item_data()

item_ids = [3158,2055,4632,3137,4628,6655,3364]

item_names = [get_item_name(item_id, item_data) for item_id in item_ids]

print(item_names)
