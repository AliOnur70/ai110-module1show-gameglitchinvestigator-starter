"""Streamlit interface for Game Glitch Investigator."""
import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

st.set_page_config(page_title="Game Glitch Investigator", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("Guess the secret number before you run out of attempts.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)
st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


def reset_game():
    """Start over in the chosen difficulty with a fresh secret and score."""
    # FIX: Keep Streamlit state together so the New Game button resets everything.
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.last_feedback = ""
    st.session_state.game_difficulty = difficulty
    # FIX: Clear the guess input when starting a new game.
    st.session_state.pop("guess_entry", None)


if "secret" not in st.session_state or st.session_state.get("game_difficulty") != difficulty:
    reset_game()

st.subheader("Make a guess")
st.info(f"Guess a number from {low} to {high}. Attempts left: {max(0, attempt_limit - st.session_state.attempts)}")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:", key="guess_entry", disabled=st.session_state.status != "playing")
col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀", disabled=st.session_state.status != "playing")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    reset_game()
    st.rerun()

if submit:
    ok, guess_int, error = parse_guess(raw_guess)
    if not ok:
        st.error(error)
    elif not low <= guess_int <= high:
        st.error(f"Enter a number between {low} and {high}.")
    else:
        # FIX: Only valid guesses use attempts; compare integers every time.
        st.session_state.attempts += 1
        outcome, message = check_guess(guess_int, st.session_state.secret)
        st.session_state.history.append(guess_int)
        st.session_state.score = update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )
        st.session_state.last_feedback = message
        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"

if st.session_state.status == "won":
    st.success(f"You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
elif st.session_state.status == "lost":
    st.error(f"Out of attempts! The secret was {st.session_state.secret}. Score: {st.session_state.score}")
elif show_hint and st.session_state.last_feedback:
    st.warning(st.session_state.last_feedback)

st.write(f"Score: {st.session_state.score}")
st.write(f"Guesses: {st.session_state.history}")
st.divider()
st.caption("Debugged with AI assistance; checked with automated tests and human review.")
