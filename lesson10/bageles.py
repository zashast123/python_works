import random
life = 10 # Жизни
length = 3  #три символа


answer = random.randint(100, 999) #ответ
answer = str(answer)
while life:
    is_guessed = False
    print("=" * 10)

    print("Жизней:", life)
    guess =input("ПРедположения")
    if len(guess) != or not guess.isdigit():
        print("Число от 100 до 999,пожалуйста")
        continue