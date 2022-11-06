# lst = ["Антон","Вова","гриша","Олег","ЯН"]
# for element in lst:
#     print(element)
# for i in range(0,10):
#     print(i)
# #while
# is_game = True
# while is_game:
#     if input("Да/нет") == "нет":
#
#         is_game = False
#
#     print("sue")

# word = input("Введите слово:")
# while word:
#     print(word, end=" ")
#     word = word[:-1]
# z = int(input("Введите число:"))
# while z:
#     z -= 1
#     if z % 2 == 0:
#         print(z, end=" ")



x = int(input("Введите число"))
step = 0
while x != 1:
    step += 1
    if x % 2 == 0:
        x = x // 2
        print(f"{step})",end=" ")
        print(x, "/ 2 =",end=" ")
    else:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = 3 * x + 1
    print(x)
print("Шагов:",step)