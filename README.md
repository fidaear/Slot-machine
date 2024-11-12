
# Slot Machine Game

This is a simple slot machine game built in Python to practice programming skills. The game simulates a slot machine where the player can place bets, spin the reels, and try to win based on matching symbols.

## How to Play
1. **Deposit Money**: The player is prompted to deposit money at the start of the game.
2. **Choose Number of Lines**: The player can choose how many lines (up to 3) they want to bet on.
3. **Place Your Bet**: The player can choose an amount to bet on each line, within the minimum and maximum bet limits.
4. **Spin the Slot Machine**: The game spins the reels, displaying random symbols, and checks for winnings based on the chosen lines and symbols.
5. **Check Winnings**: The player earns winnings if the symbols on a line match, with each symbol having a different value. The total winnings are calculated and displayed.
6. **Continue or Quit**: The player can continue playing or quit the game at any time, and the final balance is shown when they choose to quit.

## Features
- Configurable betting limits and number of lines.
- Randomized slot machine spins using Python's `random` module.
- Winnings are calculated based on matching symbols, with different values assigned to each symbol.
- The game handles user input validation for depositing money, choosing lines, and placing bets.

## Symbol Values
- **A**: 5 points
- **B**: 4 points
- **C**: 3 points
- **D**: 2 points

## Example Output
```plaintext
What would you like to deposit? $100
Enter the number of lines to bet on (1-3): 3
What would you like to bet on each line? $10
You are betting $10 on 3 lines. Total bet is equal to $30.
[A | B | C]
[A | D | A]
[C | B | A]
You WON $0.
You left with $70.
```

## Requirements
- Python 3.x

## How to Run
1. Make sure you have Python installed on your system.
2. Run the script using the command:
   ```bash
   python main.py
   ```

## Purpose
This project was built to practice Python programming skills, including:
- Working with loops and user input.
- Using Python's `random` module.
- Implementing functions and basic game mechanics.

