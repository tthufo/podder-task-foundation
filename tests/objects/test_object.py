from podder_task_foundation.objects import Dictionary, factory
from pathlib import Path


def test_image_create():
    _object = factory(Path(__file__).parent.joinpath("data", "image_01.png"))
    assert _object.type == "image"

    file_name = _object.get_file_name()
    assert file_name.name == "image.png"


def test_dictionary_create_with_no_name():
    _object = Dictionary({"test": "abc"})
    assert _object.type == "dictionary"

    file_name = _object.get_file_name()
    assert len(file_name.name) > 10


def test_dictionary_create_with_name():
    name = "test.yaml"
    _object = Dictionary({"test": "abc"}, name=name)
    assert _object.type == "dictionary"

    file_name = _object.get_file_name()
    assert file_name.name == name