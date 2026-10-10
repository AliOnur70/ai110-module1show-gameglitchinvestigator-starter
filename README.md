# Game Glitch Investigator

## Project Overview

This is a number guessing game built with Python and Streamlit. The player chooses a difficulty, guesses a secret number, gets higher/lower hints, and tries to win before the attempts run out. I debugged the starter project and moved the main rules into `logic_utils.py` so they could be tested separately.

## Setup

1. Open the project folder in VS Code.
2. Install the packages: `python -m pip install -r requirements.txt`
3. Start the game: `python -m streamlit run app.py`
4. Open the local address shown in the terminal.
5. Run tests with `python -m pytest -q`.

## Bugs and Fixes

- Hints were backwards: higher guesses said to go higher. I fixed the messages in `check_guess()`.
- The secret was changed to a string on some turns. I kept it as an integer so winning works every time.
- Wrong guesses sometimes increased the score. Now a wrong guess loses 5 points (but the score will not go below zero), and a win awards points.
- Attempts started at 1, and invalid text used an attempt. Now attempts start at 0 and only valid guesses count.
- New Game did not reset the score or status and did not use the difficulty's range. Now it resets the entire game.
- Some difficulty ranges and on-screen directions were inconsistent. Now Easy is 1–20, Normal is 1–100, and Hard is 1–200.
- During manual testing, clicking New Game caused a Streamlit session-state error. I changed the reset logic to remove the `guess_entry` key instead of directly modifying the input after the widget was created. I tested the button again, and the error no longer appeared. 

## Demo Walkthrough

This example assumes the secret number is **50** in Normal mode. The real secret is random; you can check it under **Developer Debug Info** while testing.

1. Start a game on Normal difficulty; the range is 1–100 and 8 attempts are available.
2. Enter `40` and select **Submit Guess**. The game says **Go HIGHER!** and shows 7 attempts left.
3. Enter `70`. The game says **Go LOWER!** and shows 6 attempts left.
4. Enter `50`. The game reports a win and shows the final score.
5. Select **New Game**. The score, guess history, attempt counter, and win status reset.

## Document Your Experience

I used ChatGPT to review the starter code and propose the fixes, then checked the code's logic and the test results. The biggest problems were reversed hints, mixing strings and numbers, and not resetting Streamlit session state correctly. Moving functions into `logic_utils.py` made the game rules easier to understand and test. I kept the changes small instead of rebuilding the whole app.

## Automated Test Results

I ran `python -m pytest -q` on the completed game logic in the development environment:

```text
...............                                                          [100%]
15 passed in 0.05s
```

The automated tests cover winning, high/low hints, input parsing, difficulty ranges, and scoring. The Streamlit interface also needs to be checked manually on the user's computer.

## Files

- `app.py` — Streamlit user interface and game state
- `logic_utils.py` — guessing, input, scoring, and difficulty rules
- `tests/test_game_logic.py` — automated pytest tests
- `reflection.md` — bug logs and discussion of AI assistance
