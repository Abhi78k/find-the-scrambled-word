# 🔀 Word Unscramble Game (Shuffle & Guess)

This is a simple **word unscrambling game** built in Python. A random word is selected from a predefined list, its letters are shuffled, and the player must guess the original word within 10 attempts.

## 🎮 Game Description

* A word is randomly selected from a list.
* Its letters are shuffled randomly.
* The player is shown the scrambled word.
* You have **10 chances** to guess the original word.
* The game ends when you either guess correctly or run out of attempts.

## 📁 File Structure

```
word_unscramble.py     # Main game script
wordlist.py            # Contains a list named 'abcd' with valid words
README.md              # This file
```

## 🛠️ Requirements

- Python 3.x
- A `wordlist.py` file with a list variable `abcd` containing at least 2464 words.

**Example `wordlist.py`:**

```python
abcd = ["python", "flask", "banana", "mirror", "orange", ...]
```

## ▶️ How to Run

1. Ensure `wordlist.py` is in the same directory as your game script.
2. Open a terminal and run:

```bash
python word_unscramble.py
```


## ✅ Example Gameplay

```
Find the word! aotpyhn
Enter your guess! python
You win!
```

Or:

```
Find the word! aknaba
Enter your guess! snake
Wrong guess! Try again
9 chances left!
```


## 💡 Features

- Random word selection and scrambling
- Tracks number of remaining guesses
- Encouraging feedback on correct/incorrect attempts

## 📌 Future Enhancements

- Add difficulty levels (short/long words)
- Timer-based challenge mode
- Add hints (e.g., word definitions or first letter)
- GUI version using Tkinter or web version with Flask

## **Demo:**
- Guessing the wrongly results in losing 1 out of the 10 tries.

<img width="216" height="92" alt="image" src="https://github.com/user-attachments/assets/ee4ba6c4-4870-49cf-95d0-769187ad482e" />

- Guessing the right answer within the 10 tries results in the game ending.

<img width="215" height="66" alt="image" src="https://github.com/user-attachments/assets/aa603125-1808-433e-afbe-490359ad0971" />

## 📜 License

This project is open-source and free under the [MIT License](LICENSE).

