import json

import pytest

from src.json_helpers import JsonReader, JsonWriter


@pytest.fixture
def temp_json_file_path(tmpdir):
    # Create a temporary file
    temp_file_path = tmpdir.join("temp_test_file.json")
    with open(temp_file_path, "w") as temp_file:
        json.dump({"key1": "value1", "key2": "value2"}, temp_file)

    return temp_file_path


def test_json_reader_read_valid_file(temp_json_file_path: str):
    json_reader = JsonReader(temp_json_file_path)
    result = json_reader.read()
    assert isinstance(result, dict)
    assert result == {"key1": "value1", "key2": "value2"}


def test_json_reader_read_nonexistent_file():
    non_existent_path = "non_existent.json"
    json_reader = JsonReader(non_existent_path)
    with pytest.raises(FileNotFoundError):
        json_reader.read()


def test_json_writer_write_json(temp_json_file_path: str):
    json_data = {"key1": "value1", "key2": "value2"}
    json_writer = JsonWriter(temp_json_file_path)
    json_writer.write(json_data)

    with open(temp_json_file_path, "r") as temp_file:
        result = json.load(temp_file)

    assert isinstance(result, dict)
    assert result == json_data
