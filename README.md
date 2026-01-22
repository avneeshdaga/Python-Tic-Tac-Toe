# Python-Tic-Tac-Toe

A classic Tic Tac Toe game built from scratch using Python and the Pygame library. This project features a custom graphical interface, win/draw detection, and an interactive "Play Again" state machine.

## Features
* **Graphical Interface:** Clean, custom-drawn game board and X/O assets.
* **Game Logic:** Complete implementation of win conditions (rows, columns, diagonals) and draw detection.
* **Interactive UI:** Includes a "Game Over" state with clickable **Play Again** and **Quit** buttons using a custom button class.
* **State Management:** Smooth transitions between the opening screen, gameplay, and game-over states without freezing the application.

## Built With
* **Language:** Python 3.12+
* **Library:** [Pygame](https://www.pygame.org/) - Used for window management, event handling, and rendering.

## How to Run

### Prerequisites
Ensure you have Python installed. This project is optimized for Python 3.12.

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/avneeshdaga/Python-Tic-Tac-Toe.git](https://github.com/avneeshdaga/Python-Tic-Tac-Toe.git)
    cd Python-Tic-Tac-Toe
    ```

2.  **Install Dependencies**
    ```bash
    pip install pygame
    ```
    *(Note: If you have multiple Python versions, use `py -3.12 -m pip install pygame`)*

3.  **Run the Game**
    ```bash
    python ttt.py
    ```

##  How to Play
1.  Launch the game to see the starting cover screen.
2.  The game board will appear. Player **X** always goes first.
3.  Click on any empty grid square to place your mark.
4.  The game automatically checks for a winner or a draw after every move.
5.  When the game ends, click **Play Again** to reset the board or **Quit** to close.

## 🔮 Future Improvements
* [ ] Implement a Minimax AI algorithm for a Single Player mode.
* [ ] Add a score tracker to persist wins across rounds.

## 👤 Author
**Avneesh**
* Student at University of San Francisco (USF)

---
*This project was created for educational purposes to demonstrate proficiency in Python and event-driven programming.*
