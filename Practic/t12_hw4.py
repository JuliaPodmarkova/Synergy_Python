# Задача 4. Охота за сокровищами

import json

def explore_treasure_map(treasure_map):
    if isinstance(treasure_map, dict):
        for key, value in treasure_map.items():
            if key == "chest":
                print(value)
            else:
                explore_treasure_map(value)
    elif isinstance(treasure_map, list):
        for item in treasure_map:
            explore_treasure_map(item)

try:
    with open('treasure_map.json', 'r', encoding='utf-8') as file:
        treasure_map = json.load(file)
except FileNotFoundError:
    print("Файл treasure_map.json не найден. Убедитесь, что он находится в той же директории, что и скрипт.")
    exit()

explore_treasure_map(treasure_map)
