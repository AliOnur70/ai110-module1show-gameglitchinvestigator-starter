# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

From examining the original app, I found reversed hints, inconsistent number types, and incorrect attempts and reset behavior. These were code-review findings; I will verify the cases in the starter app and record the results.

**Bug Reproduction Logs — cases to check in the starter game**

| Input Used | Expected Behavior | Actual Behavior in Original Code | Console Error / Output |
|---|---|---|---|
| Secret 50, guess 60 (integer secret) | Too High; go LOWER | Message said Go HIGHER | None |
| Secret 50, guess 40 (integer secret) | Too Low; go HIGHER | Message said Go LOWER | None |
| Secret 9, guess 10 (even-numbered attempt) | Too High | String comparison returned Too Low | None |
| Submit invalid text `abc` | No attempt used | Attempt increased before validation | That is not a number. |
| Click New Game after scoring | Reset everything | Score and history were kept | None |
