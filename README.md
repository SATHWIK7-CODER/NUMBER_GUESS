# 🎮 Number Guessing Game

A Python-based interactive number guessing game where the player tries to guess a randomly generated number within a limited number of attempts.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Concepts Used](#concepts-used)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Difficulty Levels](#difficulty-levels)
- [High Scores](#high-scores)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)

---

## 📖 About the Project

This is a beginner-friendly Python project that helps improve logical thinking, user input handling, and control flow understanding. The player must guess a secret number between **1 and 100** within a limited number of attempts based on the chosen difficulty level.

---

## ✨ Features

- 🎲 Random number generation every game
- 💡 Hints after every guess (Too High / Too Low)
- 🎯 3 Difficulty levels (Easy, Medium, Hard)
- 📊 Attempt counter
- 🏆 High score saving to a file
- 🔄 Play again option
- 🛡️ Error handling for safe file operations

---

## 🧠 Concepts Used

| Concept | Usage |
|--------|-------|
| `import random` | Generate secret number |
| `int(input())` | Get user guess |
| `if/elif/else` | Give hints and check conditions |
| `while` loop | Keep the game running |
| `+=` counter | Count attempts |
| Functions | Organize code cleanly |
| File handling | Save and read high scores |
| `try/except` | Handle missing score file safely |
| f-strings | Display dynamic messages |

---

## ▶️ How to Run

### Requirements
- Python 3.x installed on your system

### Steps

1. **Download** the `guessing_game.py` file
2. **Open terminal** in the same folder
3. **Run the game:**

```bash
python guessing_game.py
```

> 💡 You can also run it online at [replit.com](https://replit.com) — no installation needed!

---

## 🕹️ How to Play

1. Enter your **name**
2. Choose a **difficulty level**
3. Start **guessing** a number between 1 and 100
4. Use the **hints** (Too High / Too Low) to narrow down your guess
5. Try to guess the number **within the allowed attempts**
6. Your score is **saved automatically** after every game
7. Choose to **play again** or exit

---

## 🎚️ Difficulty Levels

| Level | Attempts |
|-------|----------|
| 1 - Easy | 10 attempts |
| 2 - Medium | 5 attempts |
| 3 - Hard | 3 attempts |

---

## 🏆 High Scores

- Scores are saved in a file called `scores.txt`
- Every game is recorded — **win or lose**
- Scores are displayed at the **start of every game**
- Format: `PlayerName - X attempts - Won/Lost`

**Example scores.txt:**
```
Alice - 3 attempts - Won
Bob - 5 attempts - Lost
Charlie - 2 attempts - Won
```

---

## 📁 Project Structure

```
number-guessing-game/
│
├── guessing_game.py   # Main game file
├── scores.txt         # Auto-generated high scores file
└── README.md          # Project documentation
```

---

## 💻 Sample Output

```
🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮

--- HIGH SCORES ---
Alice - 3 attempts - Won
-------------------

Enter your name: Bob
Choose difficulty:
1. Easy   (10 attempts)
2. Medium (5 attempts)
3. Hard   (3 attempts)
Enter choice (1/2/3): 2

I'm thinking of a number between 1 and 100...
You have 5 attempts! Good luck! 🎯

Enter your guess: 50
Too low! 4 attempts left
Enter your guess: 75
Too high! 3 attempts left
Enter your guess: 63
You got it in 3 attempts! 🎉

Do you want to play again? (yes/no): no
Thanks for playing Bob! Goodbye! 👋
```

---

## 👨‍💻 Author

Built step by step as a beginner Python learning project.

> *"Don't just copy — understand every line!"* 💪
