"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    #makea boolean var to hold the state of returning one in a role
    outOne = False
    #initilize variable to hold the sum of rolls
    total = 0
    #intilize variable to track number of apllied rolls
    k = 0
    #loop num_rolls to build the sum
    while k < num_rolls:
        current_dice = dice()
        #make returning one in out put true
        if current_dice == 1:
            outOne = True
        total = total + current_dice
        k += 1
    #test for output one
    #if true, return one
    #otherise return the total sum
    if outOne:
        return 1
    else:
        return total
        
    # END PROBLEM 1

# print("roll_dice(3)", roll_dice(3))
def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    #cubed score
    cubed_score = pow(score , 3)
    #variable to make the sum alternating difference of the digits, if it's even make it difference
    #if it's odd make it addition
    k = 0
    #initilize varibale to hold accumulated sum of alternating difference of the digits
    sum = 0
    #loop that extract each digit per iteration
    #then reduces the number one digit by removing extracteed digit
    #inspired from MIT 6.0001 algorithm of extracting digits from number of base 10
    while cubed_score > 1:
        #if the current iteratio is even, perform a subtraction 
        if k%2 == 0:
            sum = sum - cubed_score%10
        else: 
            sum = sum + cubed_score%10
        #remove the trailing digit
        cubed_score = cubed_score//10
        #change parity 
        k += 1
    #the return is equal to one more than the absolute alternating difference of the digits of the opponent's score cubed.
    return abs(sum) + 1
    # END PROBLEM 2

# print("free_bacon(4)", free_bacon(4))
# print("free_bacon()", free_bacon(1))
# print("free_bacon()", free_bacon(20))
# print("free_bacon()", free_bacon(45))
def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    #test for num rolls == 0
    #if true, return function of free bacon
    #otherwise return roll dice function
    if num_rolls == 0:
        #return call of free bacon with oppenent score
        return free_bacon(opponent_score)
    else:
        #here we call function roll_dice and argumetnts are evaluated from take_turn parameters
        return roll_dice(num_rolls, dice)

    # END PROBLEM 3

# print("take_turn(0, 51, six_sided)", take_turn(0, 51, six_sided))
def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    #raise three to the power of players' score sum
    powered_three = pow(3, (player_score + opponent_score))
    ##test for equality of firat and list digit
        #if true, return true
        #otherwise return false
    if str(powered_three)[0] == str(powered_three)[-1]:
        return True
    else:
        return False
    # END PROBLEM 4
# print("false", is_swap(2, 4))
# print("false", is_swap(11, 1))
# print("true", is_swap(1, 0))
# print("true", is_swap(23, 4))

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    feral_hogs: A boolean indicating whether the feral hogs rule should be active.
    """
    #after several testing, it appeared that
    #the function prints on the terminal all past history of all turns in that game each time turn is played
    #one turn is ended only if the function "strategey of the other player is called"
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    #variable to hold the scores of the first and second player respectively
    #to assert their values to be nonengative at the beginning of each turn
    #also they are built incremently at each turn
    score0 = score0
    score1 = score1
    #var for holding last score to be used in printing last score in both0 function
    #at the end of each turn
    last_score0 = 0
    last_score1 = 0

    #initilize bith function to get callable object "both0" that takes last score of 
    #of player 0 and player one and print the last score of each and announce the lead change
    #throughout the game
    both0 = both(say_scores, announce_lead_changes())
    #commentary function to announce highest score for each player,
    #  whenever the player croses the latest highest score
    say = both(announce_highest(0), announce_highest(1))
    #players alternate turns rolling dice until one of the players reaches the goal score.
    while not (score0 >= 100 or score1 >= 100):
        #any turn is ended if and only if there is a call to the other strategy function
        if who == 0:
            first_dice_num = strategy0(score0, score1)
        elif who == 1:
            scnd_dice_num = strategy1(score1, score0)
        #var valued three only if feral_hogs is true, zero otherwise its value is zero
        feral3 = 0
        #test for validity of scores
        assert score0 >= 0, 'score of first player must be nonnegative integer'
        assert score1 >= 0, 'score of the second player must be nonnegative integer'  
        #determine which user is playing this turn   
        # the first user   
        if who == 0:
            assert first_dice_num >= 0, 'strategy0 must return nonnegative integer'
            #enabling feral_hogs if true
            if abs(first_dice_num - last_score0) == 2 and feral_hogs:
                feral3 = 3
            #play the turn and add the result to the previous one
            last_score0 = take_turn(first_dice_num, score1, dice)
            score0 += (last_score0 + feral3)
        
        #the second user
        elif who == 1:
            assert scnd_dice_num >= 0, 'strategy0 must return nonnegative integer'
            if abs(scnd_dice_num - last_score1) == 2 and feral_hogs:
                feral3 = 3
            last_score1 = take_turn(scnd_dice_num, score0, dice)
            score1 += (last_score1 + feral3)
        #change the user to the other player
        who = other(who)
        #in case of swap, interchange the scores
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        # END PROBLEM 5
        # BEGIN PROBLEM 6
        #print the score of each player and if there is lead change, announce it!
        both0 = both0(last_score0, last_score1)
        #aannounce the highest score if the latest highest is crossed
        say = say(score0, score1)
        # END PROBLEM 6
    
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    
    return score0, score1


#######################
# Phase 2: Commentary #
#######################

# this function returns itself each time is called,
# so if it appears in expression place of assignment statement, it will bind
#this name with this function
#as a result, this name will be callable with two arguments
def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


#this function takes the previous leader as its only single argument
#it retuens a local defined function
# so, any time that local defined function is called,
# it has access to the atgiment prev_leader from its parent function announce_lead_changes
# also note that, when "say" function is called, its return expression is 
#call invocation of its parent function announce_lead_changes, and this parent
#return expression is the function object "say"
def announce_lead_changes(prev_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != prev_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 6)
    Player 0 now has 10 and Player 1 now has 6
    >>> h3 = h2(6, 17)
    Player 0 now has 6 and Player 1 now has 17
    Player 1 takes the lead by 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, prev_high=0, prev_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 point(s)! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 point(s)! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 47) # Player 1 gets 12 points; not enough for a new high
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 point(s)! That's the biggest gain yet for Player 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 point(s)! That's the biggest gain yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    #define a function that takes the current scores of both player
    #test for who, in both case, if there is highest, return new call of the announce_highest withthe new args
    #for zero compare with first argument
    #for who ==1 cpmpare with the seond argument
    #if there is no new high, return announce_highest with the same args
    def say_highest(score0, score1):
        if who == 0:
            diff = score0 - prev_score
            if (diff) > prev_high:
                print(diff, "point(s)! That's the biggest gain yet for Player 0")
                return announce_highest(0, diff, score0)
            else:
                return announce_highest(0, prev_high, score0)
        elif who == 1:
            diff = score1 - prev_score
            if diff > prev_high:
                print(diff, "point(s)! That's the biggest gain yet for Player 1")
                return announce_highest(1, diff, score1)
            else:
                return announce_highest(1, prev_high, score1)
    return say_highest
        
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(g, num_samples=1000):
    """Return a function that returns the average value of G when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    #define a function to taking *args arguments
    def calc_sum(*args):
        #counter to loop num_smples times
        counter = 0
        #built incremently each time "g" is called
        sum = 0
        #loop num_smaples times and in each iteration, call "g" and add the result to sum 
        #to build the sum incremently
        while counter < num_samples:
            sum += g(*args)
            counter += 1
        #return the average of calling "g" num_samples times
        average = sum/num_samples
        return average
    return calc_sum
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if False:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    return 6  # Replace this statement
    # END PROBLEM 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and does not trigger a
    non-beneficial swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    return 6  # Replace this statement
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Replace this statement
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()