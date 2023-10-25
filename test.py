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

word_list = ["apple", "banana", "mango"]
display = []
# word_blank = ""

random_word = random.choice(word_list)
word_length = len(random_word)

end_game = False
life = 6

for blank in range(word_length):
    display += "_"
print(display)
# print(random_word)


while not end_game:

    guess = input("Guess the letter: ").lower()

    if guess in display:
        print("You already guessed this word")

    for position in range(word_length):
        letter = random_word[position]

        if guess == letter:

            display[position] = letter
    print(stages[life])

    if guess not in random_word:

        life -= 1
        print(stages[life])
        if life == 0:
            end_game = True
            print("Sorry you die")
    print(display)
