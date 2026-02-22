# 🎓 Week 2: Student Grade Calculator

## Project Overview

A beginner-friendly Python program that asks a student for their mark in **one subject**, validates the input, and displays a letter grade with a motivational remark. This project introduces **functions**, **conditionals**, and **input validation** in Python.

---

## 🎯 Project Goals & Objectives

- Use `input()` to collect a single numeric score from the user
- Validate input using `try/except` and a `while` loop
- Use `if/elif/else` to map the score to a letter grade
- Organise code into clean, reusable **functions**
- Display a formatted result to the terminal

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.x installed on your system
  - **Download:** https://www.python.org/downloads/
  - During installation on Windows, check **"Add Python to PATH"**
- A code editor (e.g., VS Code, Notepad++)

### Running the Program

1. **Clone or download** this repository to your local machine.
2. Open a **terminal / command prompt** and navigate to the project folder:
   ```bash
   cd path/to/Task-2
   ```
3. Run the program:
   ```bash
   python grade_calculator.py
   ```
4. Enter your subject mark (0–100) when prompted.

> **No external packages required.** This project uses only Python's built-in functions.

---

## 📁 Code Structure

```
Task-2/
├── grade_calculator.py   # Main program file
├── test_cases.txt        # Manual test cases and expected outputs
└── README.md             # Project documentation (this file)
```

---

## 💻 Technical Details

### Concepts Used

| Concept | Description | Used In |
|---|---|---|
| **Functions** | Reusable blocks of code defined with `def` | `get_score()`, `calculate_grade()`, `main()` |
| **`while` loop** | Repeats until a condition is met | Input validation inside `get_score()` |
| **`try/except`** | Handles runtime errors gracefully | Catching non-numeric input |
| **`if/elif/else`** | Conditional branching | Assigning letter grades |
| **f-strings** | Formatted string literals | Building the result display |

### Grading Scale

| Score | Letter Grade | Remark |
|---|---|---|
| 90 – 100 | **A** | 🌟 Outstanding! Excellent work! |
| 80 – 89  | **B** | 👍 Great job! Keep it up! |
| 70 – 79  | **C** | 😊 Good effort! Room to grow. |
| 60 – 69  | **D** | 📚 Keep studying — you can do better! |
| 0 – 59   | **F** | 💪 Don't give up! Seek help and try again. |

### How the Code Works (Algorithm)

1. Display a welcome banner.
2. Call `get_score()` — prompt the user for a number between 0 and 100.
   - If the input is not a valid number or out of range, show a warning and ask again.
3. Call `calculate_grade()` to get the **letter grade** and **remark**.
4. Display the result.

---

## 📊 Sample Output

```
========================================
     🎓 Student Grade Calculator
========================================
Enter your subject mark (0 - 100): 85

========================================
         📊 Result
========================================
  Mark         : 85.0
  Letter Grade : B

  👍 Great job! Keep it up!
========================================
```

---

## 🧪 Testing Evidence

| Test Case | Input | Expected Grade | Result |
|---|---|---|---|
| A-range score | 95 | A | ✅ Pass |
| B-range score | 85 | B | ✅ Pass |
| Boundary: 70 | 70 | C | ✅ Pass |
| Boundary: 60 | 60 | D | ✅ Pass |
| Failing score | 45 | F | ✅ Pass |
| Invalid: text | "hello" | Reprompts | ✅ Pass |
| Invalid: out of range | 150 | Reprompts | ✅ Pass |

See `test_cases.txt` for the full set of manual test cases.

---

## 💡 What I Learned

- How to define and call **functions** in Python
- How to use `while True` with `try/except` for **input validation**
- How `if/elif/else` chains implement a **decision table**
- How to display formatted output with **f-strings**

---

## 📚 Resources

- [Official Python Docs](https://docs.python.org/3/)
- [Python `try/except` – W3Schools](https://www.w3schools.com/python/python_try_except.asp)
- [Python Functions – python.org](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Google Colab](https://colab.research.google.com/) — Run Python in your browser, no install needed

---

*Week 2 | Python Basics | Developers Arena*
