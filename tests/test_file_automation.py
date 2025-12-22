import pytest
from pathlib import Path
from src import file_automation
from contextlib import nullcontext
# from unittest.mock import mock_open

"""
@pytest.mark.parametrize("directory_path, expected_result", [
    (Path("C:/Users/13605/Desktop/DL_Docs/"), )

])
"""


# def test_check_directory_is_valid(directory):


# def test_move_file(source_file: str, source_directory: Path, destination_directory: Path):


@pytest.mark.parametrize(
    "directory_path, expected_result",
    [
        (Path("C:/Users/13605/Desktop/DL_Docs/"), True),
        (Path("C:/Users/13605/Downloads/"), True),
        (Path("C:/Uuuusers"), False),
        (Path(''), False),
        (Path(), False),
    ],
)
def test_check_directory_is_valid(directory_path, expected_result):
    result = file_automation.check_directory_is_valid(directory_path)
    assert result == expected_result
