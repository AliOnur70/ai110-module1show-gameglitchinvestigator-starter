"""Small, testable functions for the number guessing game."""


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a difficulty."""
    ranges = {"Easy": (1, 20), "Normal": (1, 100), "Hard": (1, 200)}
    return ranges.get(difficulty, ranges["Normal"])


def parse_guess(raw: str):
    """Return (valid, integer guess, error) for a user's input."""
    if raw is None or not str(raw).strip():
        return False, None, "Enter a guess."
    try:
        # FIX: Only accept whole numbers instead of silently truncating decimals.
        value = int(str(raw).strip())
    except (TypeError, ValueError):
        return False, None, "Enter a whole number."
    return True, value, None


def check_guess(guess: int, secret: int):
    """Return a result label and a hint that agrees with the comparison."""
    # FIX: ChatGPT helped move the comparison out of the Streamlit UI.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Award points for winning; guessing incorrectly never earns points."""
    # FIX: Removed the broken even/odd scoring branch after reviewing its logic.
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * (attempt_number - 1))
    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)
    return current_score
