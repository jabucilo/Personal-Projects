################################################################################
# Python assignment: Typing game
#
# Name: Matej Haas
# Matriculation number: 00872249
################################################################################

import time
import random

# List of Strings containing all available words
WORDS = ["if", "[", "]"]

# List of Floats containing the progress of each word in percentages (0-100)
# Items of this list share the same indexes with the WORDS list
WORDS_PROGRESS = [0.0, 0.0, 0.0]

# List of Floats containing the number of seconds the user needed to type a specific word
# Items of this list share the same indexes with the WORDS list
WORDS_SECONDS = [0.0, 0.0, 0.0]

# Represents the number of wrong user inputs 
MISTAKES_MADE = 0

# Represents the number of characters typed by the user 
CHARACTERS_TYPED_BY_USER = 0

# Represents the characters per seconds 
CPS = 0.0

# Dictionary containing all possible word combinations for a given word (with corresponding word as key)
WORDS_COMBINATIONS = {"if": [], "[": ["]", "if"], "]": ["["]}


# CONSTANTS

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
GAME_BOARD_COLUMNS = 80
PERCENTAGE_PER_SUCCESSFUL_INPUT = 100 / 4
HIGH_SCORE_SEPARATOR = " - "
TIME_PROGRAM_STARTED = time.time()

# Represents the current seconds passed since program start (automatically updated)
SECONDS_PASSED = 0

# FRAMEWORK

def timed_input(prompt):
    # Reads the user input while updating SECONDS_PASSED and printing prompt to standard output.
    global SECONDS_PASSED
    user_input = input(prompt)
    time_current = time.time()
    SECONDS_PASSED = time_current - TIME_PROGRAM_STARTED
    return user_input


def find_row_letter(word):
    # Finds associated row letter (e.g., A, B, C, ...) in the game board and returns this letter.
    # If the word was not found in `WORDS`, then None is returned.
    if word in WORDS:
      return ALPHABET[WORDS.index(word)]
    else:
      return None


def is_word_complete(word):
    # Returns True in case a given word has 100 percent progress, False otherwise.
    index = WORDS.index(word)
    if int(WORDS_PROGRESS[index]) == 100:
      return True
    else:
      return False


def increment_progress(word):
    # Updates the progress of a given word by adding PERCENTAGE_PER_SUCCESSFUL_INPUT to the appropriate entry in WORDS_PROGRESS.
    # In case a word is complete, adds SECONDS_PASSED to the appropriate entry in WORDS_SECONDS.
    global WORDS_PROGRESS, WORDS_SECONDS
    index = WORDS.index(word)
    WORDS_PROGRESS[index] += PERCENTAGE_PER_SUCCESSFUL_INPUT
    if is_word_complete(word):
      WORDS_SECONDS[index] += SECONDS_PASSED


def reset_progress(word):
    # Resets the progress of a given word to 0.0.
    global WORDS_PROGRESS
    index = WORDS.index(word)
    WORDS_PROGRESS[index] = 0.0


def check_if_won():
    # Returns True if all words are completed, False otherwise.
    for word in WORDS:
      if not is_word_complete(word):
        return False
    return True


def print_board():
    # Prints the game board as described in the assignment description.
    board = []
    first_last_row = "  " + "-" * (GAME_BOARD_COLUMNS + 4)
    board.append(first_last_row)

    for word in WORDS:
      index = WORDS.index(word)
      new_row = f"{find_row_letter(word)} | "
      number_of_dots = int(WORDS_PROGRESS[index] * GAME_BOARD_COLUMNS / 100) - len(word)
      if number_of_dots < 0:
        number_of_dots = 0

      new_row += "." * number_of_dots
      new_row += word
      number_of_spaces = GAME_BOARD_COLUMNS - (number_of_dots + len(word))
      new_row += " " * number_of_spaces
      new_row += " | "
      new_row += "{:.2f}%".format(WORDS_PROGRESS[index])

      if is_word_complete(word):
        new_row += " (in {:.2f}s)".format(WORDS_SECONDS[index])

      board.append(new_row)

    board.append(first_last_row)
    for row in board:
      print(row)


def choose_random_words():
    # Returns a list of random words (String) chosen from the global WORDS list.
    incomplete_words = [word for word in WORDS if not is_word_complete(word)]
    random_word = random.choice(incomplete_words)
    random_words = add_random_word_combinations(random_word)
    return random_words


def read_input(random_words):
    # Reads a user input and updates CHARACTERS_TYPED_BY_USER and CPS based on this input.
    # The function receives a list of words (String) and returns the user input (String).
    global CHARACTERS_TYPED_BY_USER, CPS
    prompt = "Input "
    for word in random_words:
      prompt += find_row_letter(word)

    prompt += ": "
    user_input = timed_input(prompt)
    sanitized_user_input = "".join(user_input.split())
    CHARACTERS_TYPED_BY_USER += len(sanitized_user_input)
    CPS = CHARACTERS_TYPED_BY_USER / SECONDS_PASSED
    return sanitized_user_input


def handle_input(random_words):
    # Reads user input by calling read_input and checks whether this input is correct.
    # In case the input is correct, the progress is updated by calling increment_progress for each word.
    # In case the input is incorrect, the progress is reset by calling reset_progress for each word and
    # MISTAKES_MADE is incremented.
    global MISTAKES_MADE
    user_input = read_input(random_words)
    for word in random_words:
      if user_input.startswith(word):
        user_input = user_input[len(word):]
        correct_input = True

      else:
        correct_input = False
        break

    if correct_input and len(user_input) == 0:
      for word in random_words:
        increment_progress(word)

      print("Correct input!\n")

    else:
      MISTAKES_MADE += 1
      for word in WORDS:
        reset_progress(word)

      print("Wrong input. Starting again from the beginning!\n")


def add_random_word_combinations(random_word):
    # Randomly selects between 0 and the maximum amount of possible word combinations and returns a list of
    # Strings containing the random word as first item and these combinations as other items.
    word_combs = [random_word]
    incomplete_words = [word for word in WORDS_COMBINATIONS[random_word] if not is_word_complete(word)]

    max_num_of_comb = len(incomplete_words)
    if max_num_of_comb > 0:
      num_words_to_select = random.choice(range(max_num_of_comb))
      word_combs += incomplete_words[:num_words_to_select]

    return word_combs


def print_victory_message():
  # Prints victory message.
  print("\nCongratulations! You won in {:.2f} seconds with {} mistakes. \
Your typing speed is {:.3f} characters per second (CPS).".format(SECONDS_PASSED, MISTAKES_MADE, CPS))


def found_semicolon(word):
  if word.find(";")+1:
    return True
  else:
    return False


def found_colon(word):
  if word.find(":")+1:
    return True
  else:
    return False


def read_words_from_file():
    # Reads words (and their possible combinations) from the words.txt file.
    # Does nothing, in case the file doesn't exist. 
    global WORDS, WORDS_COMBINATIONS, WORDS_PROGRESS, WORDS_SECONDS
    try:
      with open("words.txt", "r") as f:
        WORDS, WORDS_COMBINATIONS, WORDS_PROGRESS, WORDS_SECONDS = [], {}, [], []
        text_file = f.readlines()

        for row in text_file:

          if found_colon(row):
            new_word = row.split(":")[0]
            rest_of_row = row.split(":")[1].strip()

            if found_semicolon(rest_of_row):
              possible_combinations = rest_of_row.split(";")

            else:
              possible_combinations = [rest_of_row]

            WORDS.append(new_word)
            WORDS_COMBINATIONS[new_word] = possible_combinations
            WORDS_PROGRESS.append(0.0)
            WORDS_SECONDS.append(0.0)

          else:
            new_word = row.strip()
            WORDS.append(new_word)
            WORDS_COMBINATIONS[new_word] = []
            WORDS_PROGRESS.append(0.0)
            WORDS_SECONDS.append(0.0)

    except OSError:
      pass


def read_high_score():
    # Reads the content of score.txt and returns a list of Strings whereas every item represents a line in the file.
    # In case the file does not exist an empty list is returned.
    try:
      with open("score.txt", "r") as f:
        text_file = f.readlines()
        new_list = []
        for row in text_file:
          new_list.append(row.strip())

      return new_list

    except IOError:
      return []


def submit_high_score(scores):
    # Asks the user for her/his name, updates scores and writes the current high scores to score.txt.
    user_name = input("\nPlease enter your name: ")
    while len(user_name) == 0:
      print("Please enter at least one character!")
      user_name = input("\nPlease enter your name: ")

    current_score = "{} - Seconds: {:.2f} - Mistakes: {} - CPS: {:.3f}".format(user_name, SECONDS_PASSED, MISTAKES_MADE, CPS)
    insert_index = len(scores)
    for row_index, row in enumerate(scores):
      seconds_column = row.split(HIGH_SCORE_SEPARATOR)[1]
      seconds = float(seconds_column.split()[1])
      if SECONDS_PASSED < seconds:
        insert_index = row_index
        break

    scores.insert(insert_index, current_score)
    try:
      with open("score.txt", "w") as f:
        new_file = ""
        for row in scores:
          new_file += row + "\n"

        f.write(new_file)

    except:
      print("Error: can not write to score.txt")


def print_high_score():
    # Prints every high score item (as it occurs in the score.txt file
    try:
      with open("score.txt") as f:
        text_file = f.readlines()
        print("\nHigh scores:\n")
        for row_index, row in enumerate(text_file):
          print(f"{row_index+1}. {row.strip()}")

        print("\n")

    except:
      print("Error: can not print High scores!\n")


def main():
    read_words_from_file()
    while not check_if_won():
      print_board()
      random_words = choose_random_words()
      handle_input(random_words)

    print_board()
    print_victory_message()
    high_score_list = read_high_score()
    submit_high_score(high_score_list)
    print_high_score()


if __name__ == '__main__':
    main()
