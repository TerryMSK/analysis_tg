import json
from pathlib import Path
import sys

folder = Path("data/")
all_data = []

for file_path in folder.glob('**.json'):
    with file_path.open('r', encoding="utf-8") as file:
        data = json.load(file)
        all_data.append(file_path.name)

if not all_data:
    print("Файлов нет в папке data")
    sys.exit(1)
else:
    print(f"Загружены файлы: {", ".join(all_data)}\n")


def numereid_word(data):
    choose = input(f'       Выбирите действие       \n1. Анализ сообщений 1 человека\n2. Анализ всех участников чата\n')
    if choose == '1':
        name_uzer = input('Введите ваш ник: ')

    bassicle_used_word = {}
    trash_word = ['@', 'link', 'document_id', 'custom_emoji', 'type']
    trash = '"#&?!~()<>,/.^*+=:;'
    trash_table = str.maketrans("", "", trash)
    for all_msg in data["messages"]:
        if all_msg.get("from") == name_uzer:
            raw_text = all_msg.get("text")
            words = str(raw_text).translate(trash_table)
            
            if any(bad in words for bad in trash_word):
                continue

            for word in words.split():
                if word.lower() not in bassicle_used_word:
                    bassicle_used_word[word.lower()] = 1

                else:
                    bassicle_used_word[word.lower()] += 1

    sorted_words = sorted(bassicle_used_word.items(), key=lambda x: x[1], reverse=False)

    for word, count in sorted_words:
        print(f"{word}: {count}")
    return 

choose = input(f'       Выбирите действие       \n1. Счётчик слов\n2. Выход\n\n')
if choose == '1':
    numereid_word(data)
