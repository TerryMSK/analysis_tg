import json
from pathlib import Path
import sys

folder = Path("data/")
all_data = []
for file_path in folder.glob('**.json'):
    with file_path.open('r', encoding="utf-8") as file:
        data = json.load(file)
        all_data.append(PendingDeprecationWarning)

if not all_data:
    print("Файлов нет в папке data")
else:
    print(f"Загружены файлы: {all_data}")

name_uzer = input('введите имя пользователя:')
search_json = Path("data/result.json")
print('result pihi')

with open(".json", "r", encoding="utf=8") as file:
    data = json.load(file)
    print(data)