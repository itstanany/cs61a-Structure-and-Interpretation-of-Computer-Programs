"""Typing test implementation"""
# Ahmed Ali Mohamed Ali
# https://www.linkedin.com/in/ahmed-ali-mohamed-84a27416a/
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selectedParagraphs = []
    for paragraph in paragraphs:
        if(select(paragraph)):
            selectedParagraphs.append(paragraph)
        else:
            pass
    if (k < len(selectedParagraphs)):
        return selectedParagraphs[k]
    else:
        return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        paragraph = remove_punctuation(paragraph)
        paragraph = lower(paragraph)
        # list of all words in paragraph
        paragraph = split(paragraph)
        for word in topic:
            if (word in paragraph):
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    lenTypedWords = len(typed_words)
    # return accurcey zero if the typed words is empty string
    if(lenTypedWords == 0):
        return 0.0
    lenReferenceWords = len(reference_words)
    matchedWords = 0
    for i in range(lenTypedWords):
        # don't test after reaching the end of the reference words
        if (i >= lenReferenceWords):
            break
        if(typed_words[i] == reference_words[i]):
            matchedWords += 1
        else:
            pass
    return ((matchedWords/lenTypedWords) * 100)

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return ((len(typed)/5) * (60/elapsed))
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if (user_word in valid_words):
        return user_word
    else:
        # build a dictionary of key as iterables of valid_words list
        # and values are the difference between user word and each valid word
        d = {v: diff_function(user_word, v, limit) for v in valid_words}
        # return the word with the latest difference or the user_word if all differences is higher than limit
        return min(d, key=d.get) if min(d.values()) <= limit else user_word

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # if the diffes exceeds the limit, stop checking rest of charchaters, and increment the final return by one to be greater than limit

    if(limit < 0):
        return 1

    # return zero difference if both strings are identical
    if (start == goal):
        return 0

    absLenDiff = abs(len(goal) - len(start))

    # return abosulte length difference if it exceeds the limit or one of two strings is empty
    if ((absLenDiff) > limit or len(start) == 0 or len(goal) == 0):
        return absLenDiff

    # resolves to either 0 (False) or 1 (True)
    diff = start[0] != goal[0]

    # increse number of diff charchter by one and call the function recursively to test for rest of charachters
    #  decrease the limit by one because we have consumed one of difference limit
    return diff + shifty_shifts(start[1:], goal[1:], limit-diff)
    # END PROBLEM 6


# ANswer not completely understood
def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    # BEGIN
    #     "*** YOUR CODE HERE ***"
    if limit < 0:
        return 1
    elif start == goal:
        return 0
    elif min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))
    else:
        diff = start[0] != goal[0]
        # thought process
        # after add one letter, we need to compare start and goal[1:], and step += 1;
        # after remove one letter, we need to compare start[1:] and goal, and step += 1;
        # after substitute one letter, we need to compare start[1:] and goal[1:], and step += 1;
        addDiff = 1 + pawssible_patches(start, goal[1:], limit-1)
        removeDiff = 1 + pawssible_patches(start[1:], goal, limit-1)
        # diff either resolves to 1(True) or 0(False)
        substituteDiff = diff + \
            pawssible_patches(start[1:], goal[1:], limit-diff)

    return min(addDiff, removeDiff, substituteDiff)
    # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct = 0
    promptLen = len(prompt)
    typedLen = len(typed)
    for i in range(typedLen):
        if typed[i] == prompt[i]:
            correct += 1
        else:
            break
    ratio = correct/promptLen
    send({'id': user_id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for i in range(len(times_per_player)):
        times.append([])
    for playerIdx in range(len(times)):
        for j in range(len(times_per_player[playerIdx]) - 1):
            times[playerIdx].append(
                times_per_player[playerIdx][j+1] - times_per_player[playerIdx][j])
    return game(words, times)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game))
                           )  # contains an *index* for each player
    # contains an *index* for each word
    word_indices = range(len(all_words(game)))
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # construct a list of lists for return value
    fastestWordsList = []
    for i in player_indices:
        fastestWordsList.append([])
    # loop through all words indices
    # construct a dictionary:
    # the key is the player index
    # value is time for that word
    # use min utility to use the current player index to apped the word to it

    for j in word_indices:
        d = {p: time(game, p, j) for p in player_indices}
        fastestWordsList[min(d, key=d.get)].append(word_at(game, j))

    # returnt he list of lists
    return fastestWordsList
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
                for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@ main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
