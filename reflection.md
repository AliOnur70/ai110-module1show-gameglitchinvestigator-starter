# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The game looked like a normal number guessing game with difficulty settings, a score, and hints. When I examined the starter code, I found that the hints were backwards, some guesses compared a number to a string, and the score could go up after a wrong answer. I also noticed that the game started with one attempt already counted and that New Game did not reset everything. These cases were confirmed by reviewing the original code; I still need to reproduce them in the running starter app on my computer.

**Bug Reproduction Logs — starter-code cases to verify in the app**

| Input Used | Expected Behavior | Actual Behavior in Original Code | Console Error / Output |
|---|---|---|---|
| Secret = 50, guess = 60, when secret is an integer | Too High; go LOWER | Outcome was Too High, but hint said "Go HIGHER!" | None from this comparison |
| Secret = 50, guess = 40, when secret is an integer | Too Low; go HIGHER | Outcome was Too Low, but hint said "Go LOWER!" | None from this comparison |
| Secret = 9, guess = 10, on an even-numbered attempt | Too High; go LOWER | Original code changed the secret to `"9"`; comparing strings `"10"` and `"9"` returned Too Low with the wrong outcome | None in the `check_guess` fallback |
| Enter `abc` on the first turn | Show validation error; attempts unchanged | Original app incremented attempts before validating the input | "That is not a number." |
| Select New Game after scoring or winning | Score, history, status, and range reset | Original button reset only attempts and secret; score, history, and status remained | None |

## 2. How did you use AI as a teammate?

I used ChatGPT to look over the starter Python files, plan fixes, and write tests. One helpful suggestion was to move the `check_guess` and `parse_guess` functions into `logic_utils.py` so I could test them without opening Streamlit. I verified the comparison logic using tests for 40, 50, and 60 against a secret of 50. I did not keep the AI-generated starter approach that turned the secret into a string and tried to compare string values as a fallback, because number comparisons should use integers. I replaced that approach with a simple integer comparison and checked the related tests.

## 3. Debugging and testing your fixes

I checked a fix by looking at the expected outcome and writing a test that would fail if the old problem happened again. For example, `test_guess_too_high` checks that 60 against 50 returns "Too High" and tells the player to go lower. ChatGPT helped me write tests for invalid inputs, scoring, and all three difficulty ranges. I ran `python -m pytest -q` in the development environment and all 15 tests passed. I also tested the game manually using Streamlit. I played a game and correctly guessed the secret number 58 after guessing 50 and 60. The game showed a final score of 80. When I clicked New Game, I received a StreamlitAPIException because the code tried to change the guess input after the widget was created. I fixed this by replacing the assignment to `st.session_state.guess_entry` with `st.session_state.pop("guess_entry", None)`. After saving the change, I tested New Game again and the error was gone. I also ran pytest again, and all 15 tests passed.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script when the user interacts with the app, such as clicking a button. Normal variables can be recreated during a rerun, which is why `st.session_state` is helpful. It keeps values like the secret number, score, attempt count, and game status while the player is playing. I also learned that the New Game button has to reset all those values, not just the secret number.

## 5. Looking ahead: your developer habits

One habit I want to keep is writing a small test for every bug I fix. Next time I use AI to help with code, I want to give it one specific problem at a time and review the changes instead of accepting everything automatically. This project showed me that AI-generated code can look fine at first and still contain logic problems. I learned that testing and reviewing the actual code are just as important as getting an answer from AI.
