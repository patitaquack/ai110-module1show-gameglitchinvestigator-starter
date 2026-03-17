import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score, get_temperature_hint


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_guess_valid_decimal():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_guess_empty_string():
    ok, _, _ = parse_guess("")
    assert ok is False

def test_parse_guess_none():
    ok, _, _ = parse_guess(None)
    assert ok is False

def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


# --- update_score ---

def test_score_win_first_guess():
    # attempt_number=2 is the first guess (attempts starts at 1, increments before scoring)
    score = update_score(0, "Win", 2)
    assert score == 100

def test_score_win_second_guess():
    score = update_score(0, "Win", 3)
    assert score == 90

def test_score_win_floor():
    # Should never go below 10 even on very late guesses
    score = update_score(0, "Win", 20)
    assert score == 10

def test_score_too_low_deducts():
    score = update_score(50, "Too Low", 3)
    assert score == 45

def test_score_does_not_go_negative():
    score = update_score(3, "Too Low", 3)
    assert score == 0


# --- get_temperature_hint ---

def test_temperature_burning_hot():
    assert get_temperature_hint(10, 11) == "🔥 Burning hot!"

def test_temperature_getting_warmer():
    assert get_temperature_hint(10, 14) == "🌡️ Getting warmer!"

def test_temperature_lukewarm():
    assert get_temperature_hint(10, 17) == "🌤️ Lukewarm..."

def test_temperature_way_colder():
    assert get_temperature_hint(1, 20) == "🥶 Way colder!"
