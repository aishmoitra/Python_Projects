### The Game of Blackjack in Python 🃏

This Python script creates a simplified version of Blackjack. In this game, one player competes against the computer to achieve a higher score without going over 21. The goal is to get as close as possible to 21 or to hit a Blackjack—exactly 21 with the first two cards.

---

### Game Setup

1. **Deck**: The deck consists of the following cards: `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`.
   - `11` represents an Ace, which can also count as 1 if a total score goes over 21.
   - Tens, Jacks, Queens, and Kings are all valued at `10`.

2. **Objective**: Get a hand value as close to 21 as possible without exceeding it. A Blackjack is 21 scored with the first two cards.

---

### Game Rules

1. **Initial Deal**: Both the player and computer receive two cards.
   - If either has a score of 21 on the initial deal, they automatically win.
   - The player can see both their own cards and one of the computer’s cards.

2. **Player’s Turn**:
   - The player can choose to:
     - **Hit**: Draw another card by entering 'y'.
     - **Stand**: End the turn by typing 'n'.
   - If drawing causes the player’s score to exceed 21, they bust and lose automatically.

3. **Computer’s Turn**:
   - The computer draws until reaching at least a score of 17.
   - If the computer goes over 21, it busts, and the player wins.

---

### Scoring

- **Blackjack**: A hand with an Ace (`11`) and a 10-point card (10, Jack, Queen, or King) on the initial deal is counted as a Blackjack.
- **Bust**: A hand totaling over 21 is a bust, causing the player or computer to lose.
- **Ace Handling**: If an Ace (valued at 11) causes a score to exceed 21, its value changes from 11 to 1.

---

### Comparing Scores

At the end of the game, scores are compared to decide the winner:

- **Blackjack**: A Blackjack beats all other scores.
- **Draw**: If both player and computer have the same score, it’s a draw.
- **Bust**: Any hand over 21 automatically loses.
- **Highest Score Wins**: The closest hand to 21 without exceeding it wins if no Blackjack or bust occurs.

---

### Code Flow

1. **Initialization**: The game asks if the player wants to start a round. Typing 'y' begins the game.
2. **Player Turn**: The player’s hand is displayed, and they decide whether to draw or stand.
3. **Computer Turn**: The computer draws until reaching a score of at least 17 or busting.
4. **Final Scores and Result**: Scores are compared, and a message shows who won or if it’s a draw.

---

### Example Output

```
Your cards: [8, 10], current score: 18
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [8, 10], final score: 18
Computer's final hand: [6, 7, 10], final score: 23
Opponent went over. You win 😁
```

---

### Play Again?

The game asks if you'd like to play another round. Type 'y' to restart or 'n' to exit. Enjoy playing Blackjack!