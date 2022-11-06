import json


def read_files(file_name):
    """
    Читает файл file_name
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
    return content


def get_model_all(model_name):
    model = model_name.query.all()
    return model


def get_model_for_id(model_name, id):
    model_element = model_name.query.get(id)
    return model_element
