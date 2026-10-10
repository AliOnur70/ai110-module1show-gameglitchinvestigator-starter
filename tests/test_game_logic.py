"""Tests for the game logic without starting the Streamlit interface."""
import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_guess_too_high():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


@pytest.mark.parametrize("difficulty,expected", [
    ("Easy", (1, 20)), ("Normal", (1, 100)), ("Hard", (1, 200))
])
def test_difficulty_ranges(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize("raw", ["", " ", "hello", "1.7", None])
def test_invalid_guess(raw):
    ok, number, error = parse_guess(raw)
    assert not ok and number is None and error


def test_valid_guess():
    assert parse_guess(" 50 ") == (True, 50, None)


def test_wrong_guesses_do_not_increase_score():
    assert update_score(20, "Too High", 2) == 15
    assert update_score(0, "Too Low", 1) == 0


def test_win_score_is_positive():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 20) == 10


def test_unknown_outcome_preserves_score():
    assert update_score(25, "Other", 3) == 25
