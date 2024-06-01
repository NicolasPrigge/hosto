import io_json as io

def get_prescription(patien: str, docteur_responsable: str) -> list[str]:
    file_name: str = docteur_responsable + ".json"
    data: dict[str, dict[int, list, str]] = io.read_json(file_name)
    return data[patien]["pilule"]

if __name__ == "__main__":
    print(get_prescription("alexandre cabana", "steve simard"))
    