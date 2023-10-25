import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["bamboo", "social", "people", "computer"]
random_word = random.choice(word_list)
display = []
word_length = len(random_word)
end_game = False

lives = 6
for word in range(word_length):
    display += "_"
print(display)
print(random_word)


while not end_game:
    guess = input("Guess the word: ").lower()

    if guess in display:
        print(f"{guess} is already chose ")
    for position in range(word_length):
        letter = random_word[position]

        if letter == guess:
            display[position] = letter

    print(display)
    print(stages[lives])
    if guess not in random_word:
        print(f"you choose {guess} is incorrect, try again!")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose")

    if "_" not in display:
        end_game = True
        print("You won!")
