intro = """
   ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██                  ▓▀▓
   ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█                 ▓▌ ▐▓ 
   ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█                ▓▌▄▄▄▐▓ 
   ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█               ▓▌     ▐▓
   ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀  ▄▄▄▄▄▄▄▄▄▄  ▐█       █▌
"""


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
=========
''', '''
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


import random

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary).lower()
print(intro)
# print(word_answer)
word_display = []
for i in range(len(word_answer)):
    word_display.append("_")

counter = 0
life = 6
print(word_display)

while counter != len(word_answer) and life > 0:
    print(stages[life])

    letter = input("Буква:")
    letter_is_be = False
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != "_":
                letter_is_be = True
            else:
                word_display[i] = letter
                counter += 1
                letter_is_be = True
    if not letter_is_be:
        life = life - 1
    print(word_display)
if counter == len(word_answer):
    print("Ты победил")
else:
    print(stages[life])
    print("Ты проиграл")