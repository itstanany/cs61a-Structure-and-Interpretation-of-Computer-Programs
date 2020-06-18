
## HOG  Game

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

Pig Out. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

  
  
  

## There are 3 rules (stratigies) for playing this game

  

1- Free Bacon. A player who chooses to roll zero dice scores points equal to one more than the absolute alternating difference of the digits of the opponent's score cubed.

* Example : The opponent has 45 points, and the current player chooses to roll zero dice. 45*45*45 = 91125, so the current player gets 1 + |9 - 1 + 1 - 2 + 5| = 13 points.

  
  

2- Feral Hogs. If the number of dice you roll is exactly 2 away (absolute difference) from the number of points you scored on the previous turn, you get 3 extra points for the turn. Treat the turn before the first turn as scoring 0 points.

* Example:

* Both players start out at 0. (0, 0)

* Player 0 rolls 3 dice and gets 7 points. (7, 0)

* Player 1 rolls 1 dice and gets 4 points. (7, 4)

* Player 0 rolls 5 dice and gets 10 points. 5 is 2 away from 7, so player 0 gets a bonus of 3. (20, 4)

* Player 1 rolls 2 dice and gets 8 points. 2 is 2 away from 4, so player 1 gets a bonus of 3. (20, 15)

* Player 0 rolls 8 dice and gets 20 points. 8 is 2 away from 10, so player 0 gets a bonus of 3. (43, 15)

* Player 1 rolls 6 dice and gets 1 point. 6 is 2 away from 8, so player 1 gets a bonus of 3. (43, 19)

  

3- Swine Swap. The excitement of the game is three(3) to the power of the sum of the players' scores. After points for the turn are added to the current player's score, if the excitement's first digit and last digit are the same, the scores should be swapped.

* Example: At the end of a turn, the players have scores of 23 and 4; 323 + 4 = 7625597484987, and 7 == 7, the scores are swapped.

  
  

### To run the game run in terminal-
python3 hog_gui.py