# Импортируем json
import json


def read_files(file_name: str) -> list:
    """Функция читает json файлы"""
    with open(file_name, 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
    return content


def get_model_all(model_name):
    """Функция выходит все данные"""
    model = model_name.query.all()
    return model


def get_model_for_id(model_name, id):
    """Функция выводить данные по id"""
    model_element = model_name.query.get(id)
    return model_element
