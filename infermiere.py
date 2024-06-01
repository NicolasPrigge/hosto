import io_json as io

def get_info(patien: str, docteur: str) -> dict[str, dict[int, list, str]]:
    file_name: str = docteur + ".json"
    return io.read_json(file_name)[patien]

if __name__ == "__main__":
    print(get_info("alexandre cabana", "steve simard"))