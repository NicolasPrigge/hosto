import io_json

def login(user_name: str, password: str) -> bool:
    """
    prend un user_name et un mote de passe et permet de se connecter
    :param user_name: le nom du docteur
    :param password: le mot de passe
    :return:
    """
    db: dict[str, str] = io_json.read_json("acount_db.json")
    if password == db[user_name]:
        return True
    else:
        login(user_name, password)

if __name__ =="__main__":
    login("steve simard", "12345")