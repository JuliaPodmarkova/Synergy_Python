# Задача 3. Вывод загадочных данных

import json

def print_pairs(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (str, int, float, list)):
                print(f"{key}: {value}")
            elif isinstance(value, dict):
                print(f"{key}: {{", end = '')
                keys = list(value.keys())
                for i, sub_key in enumerate(keys):
                    if i == len(keys) - 1:
                        print(f"'{sub_key}': {value[sub_key]}", end='')
                    else:
                        print(f"'{sub_key}': {value[sub_key]},", end = '')
                print("}")

with open('mysterious_data.json', mode='r', encoding='utf-8') as file:
    mysterious_data = json.load(file)
print_pairs(mysterious_data)
