import json


def add_patien(patient: str, numero_chambre: int) -> None:
    """
    Permet d'ajouter un patien dans la db
    :param patient: nom complet du patien
    :return:
    """
    db: dict[str, int] = loadDB()
    print(db)
    db[patient] = numero_chambre
    saveDB(db)


def loadDB() -> dict[str, int]:
    """
    load la db
    :return: la db
    """
    with open("db.json", "r") as f:
        data: dict[str, int] = json.load(f)
    return data


def saveDB(content: dict[str, int]) -> None:
    with open("db.json", "w") as f:
        json.dumps(content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_patien("steve simard", 69)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
