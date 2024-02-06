import json


class JsonReader:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> dict:
        with open(self.path, "r") as file:
            return json.load(file)


class JsonWriter:
    DEFAULT_INDENT_SIZE = 2

    def __init__(self, path: str, indent_size: int = DEFAULT_INDENT_SIZE) -> None:
        self.path = path
        self.indent_size = indent_size

    def write(self, content: dict) -> None:
        with open(self.path, "w") as file:
            json.dump(content, file, indent=self.indent_size, default=str)
