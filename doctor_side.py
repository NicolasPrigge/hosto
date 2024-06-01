import json

import io_json as io
import identification as login

# variable de programe
doctor_name: str = "steve simard"
pwd: str = "12345"
file_name: str = doctor_name + ".json"

def add_patien(patient: str, info: dict) -> None:
    """
    Permet d'ajouter un patien dans la db
    :param patient: nom complet du patien
    :return:
    """
    file_name: str = doctor_name + ".json"
    io.write_json(file_name, patient, info)

def add_pilule(pilule: str, patien: str) -> list:
    data: dict[str, dict[int, list, str]] = io.read_json(file_name)
    patien_info: dict[int, list, str] = data[patien]
    patien_info["pilule"].append(pilule)
    data[patien]["pilule"] = patien_info["pilule"]
    io.write_json(file_name, patien, data[patien])



def main() -> None:
    login.login(doctor_name, pwd)
    add_patien("alexandre cabana", {"numero de chambre": 33, "pilule": [], "maladie": "creatic chronique"})
    add_pilule("advil", "alexandre cabana")

if __name__ == "__main__":
    main()