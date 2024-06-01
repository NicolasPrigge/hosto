import json

def add_account(doctor_name: str, password: str, specialyte: str) -> None:
    file_name: str = doctor_name + ".json"
    with open(file_name, "w") as f:
        f.write("{}")

    with open("acount_db.json", "r") as f:
        data: dict[str, str] = json.load(f)

    data[doctor_name] = password
    print(data)
    with open("acount_db.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    add_account("steve simard", "12345", "concierge")