# Blackjack Basic Strategy Simulation

This project simulates playing blackjack using basic strategy over a large number of rounds to determine the average win rate.

![Convergence of win rate](/screenshots/ss1.png)


## Overview

Blackjack, also known as 21, is one of the most popular casino games worldwide. The objective is to beat the dealer's hand without going over 21. While the game is simple to understand, mastering blackjack requires knowledge of basic strategy, which dictates the best action (hit, stand, double down, split) based on the player's hand and the dealer's up card.

This simulation uses a shoe consisting of 6 decks, reshuffled when half of the cards have been dealt, to mimic standard casino conditions. Each round of the simulation represents one hand of blackjack where the player follows basic strategy rules.

## Key Findings

- **Average Win Rate**: Across multiple simulations, the average win rate using basic strategy is approximately **43.8%**, which aligns with the theoretical **42.2%**. 
- **Variability and Risk**: The simulation also demonstrates the inherent variability in short-term results. If you run it with ``roundsToSim = 100``, your results will bounce around between 40% and 50%.

## Simulation Details

- **Number of Decks**: 6
- **Shuffle Point**: Halfway through the shoe
- **Strategy**: Basic strategy, with decisions on when to hit or stand on the player's hand and the dealer's up card. *(No splitting or double down)*
- **Rounds Simulated**: 100,000 *But can be adjusted*

## How to run

To run the simulation, simply run:

```
python blackjack_simulation.py
```