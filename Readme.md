# README

## Project Overview
This project fits a model to rotational transition frequency data for a CO molecule using Python. It calculates the fitted parameters `B` and `D` and plots the data alongside the fitted model.

---

## Setup and Execution

1. **Create a virtual environment:**
   ```bash
   python3 -m venv env
   ```

2. **Activate the virtual environment:**
   - On Linux/MacOS:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python3 scripts/problem_1.py
   ```

5. **Deactivate the virtual environment (optional):**
   ```bash
   deactivate
   ```

---

## Requirements

- Python 3.7 or above
- Required Python packages:
  - `numpy`
  - `scipy`
  - `matplotlib`

---

## Output

1. Fitted parameters `B` and `D` are calculated and printed.
2. A plot showing the measured frequencies and the fitted model is displayed.

