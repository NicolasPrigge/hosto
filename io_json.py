import json


def write_json(file_name: str, key: str,  content) -> None:
    """
    Load et ecrit dans un fichier JSON
    :param file_name: JSON file
    :param key: la clef du dictionaire
    :param content: se qui vien avec la clef
    :return:
    """
    with open(file_name, "r") as f:
        data: dict = json.load(f)

    data[key] = content

    with open(file_name, "w") as f:
        json.dump(data, f)


def read_json(file_name: str) -> dict:
    """
    Load un fichier json
    :param file_name: le nom du fichier
    :return data: le contenu du fichier
    """
    with open(file_name, "r") as f:
        data: dict = json.load(f)

    return data