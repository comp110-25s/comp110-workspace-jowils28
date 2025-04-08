"""Let's test our dictionaries!"""

__author__: str = "730774862"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len
import pytest


def test_invert_edge():
    """Tests invert returns KeyError when there are duplicate values in og dictionary"""
    original: dict[str, str] = {"a": "x", "b": "x"}
    with pytest.raises(KeyError):
        invert(original)


def test_invert_use1():
    """Test that inverts original dictionary"""
    original: dict[str, str] = {"a": "c", "b": "d"}
    inverted = invert(original)
    assert inverted == {"c": "a", "d": "b"}


def test_invert_use2():
    """Test that inverts original dictionary"""
    original: dict[str, str] = {"UNC": "Chapel Hill", "Tar": "Heels"}
    inverted = invert(original)
    assert inverted["Heels"] == "Tar"


def test_count_edge():
    """tests if empty dict is returned when empty list entered"""
    original: list[str] = []
    assert count(original) == []


def test_count_use1():
    """tests to see if values correctly counted and inputted to dict"""
    original: list[str] = ["UNC", "Duke", "UNC", "NCSU", "UNC"]
    assert count(original) == {"UNC": 3, "Duke": 1, "NCSU": 1}


def test_count_use2():
    """tests to see if counted to correct key"""
    original: list[str] = ["UNC", "Duke", "UNC", "NCSU", "UNC"]
    count_dict = count(original)
    assert count_dict["UNC"] == 3


def test_favorite_color_edge():
    """tests for a tie"""
    colors: dict[str, str] = {
        "Jolee": "Blue",
        "Lily": "Blue",
        "Parker": "Orange",
        "Katie": "Pink",
        "Teni": "Orange",
    }
    assert favorite_color(colors) == "Blue"


def test_fanorite_color_use1():
    """tests for correct color return"""
    colors: dict[str, str] = {
        "Jolee": "Blue",
        "Lily": "Blue",
        "Parker": "Orange",
        "Katie": "Pink",
    }
    assert favorite_color(colors) == "Blue"


def test_favorite_color_use2():
    """tests for correct color return"""
    colors: dict[str, str] = {
        "Jace": "Red",
        "Remi": "Blue",
        "Nelli": "Yellow",
        "Joe": "Red",
    }
    assert favorite_color(colors) == "Red"


def test_bin_len_edge():
    """tests for repeated lengths"""
    original: list[str] = ["cat", "hat", "happy"]
    assert bin_len(original) == {3: {"cat", "hat"}, 5: {"happy"}}


def test_bin_len_use1():
    "tests for correct list values"
    original: list[str] = ["cat", "hat", "happy"]
    bins = bin_len(original)
    assert bins[3] == {"cat", "hat"}


def test_bin_len_used2():
    """test for length of string"""
    original: list[str] = ["cat", "hat", "happy"]
    bins = bin_len(original)
    assert len(bins[3]) == 2
