import random


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = 'y'
while is_game:
    computer = [random.choice(cards)]
    player =[random.choice(cards)]
    score = 0
    get_card = "y"
    while get_card == "y":
        player.append(random.choice(cards)) #- добавить в список
        if sum(player) >21 and 11 in player:
            """ если туз в руке и сумма > 21"""
            for i in range (0,len(player)):
                if player [i] == 11:
                    player[i] = 1
                    break
        score = sum(player)
        print(f"Твоя рука:{player},Очков: {score}")
        print("Первая карта компьютера:",computer[0])
        if score >21:
            get_card = "n"
        else:
            get_card = input("'y'-взять карту,n - остановиться:")


        while sum(computer) < 17:
            computer.append(random.choice(cards))
        if sum(computer) > 21 and 11 in computer:
                """ если туз в руке и сумма > 21"""
                for i in range(0, len(computer)):
                    if computer[i] == 11:
                        computer[i] = 1
                        break
        score_computer = sum(computer)
        print("=" * 10)
        print(f"Твоя итоговая рука:{player}. Очков:{score}")
        print(f"итоговая рука компьютера:{computer}. Очков:{score_computer}")


        if score >21 and score_computer >21:
            print("Перелет у обоих.Ничья.")
        elif score >21:
            print("Твой перелет ты проиграл")
        elif score_computer >21:
            print("Перелет компьютера,ты победил")
        elif score > score_computer:
            print("Победа")
        else:
            print("проиграл")
        is_game = input("Играем дальше? Y-да n- нет")