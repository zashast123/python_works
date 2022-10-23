#Виды ошибок

#Деление на ноль
# x = 15/0

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# x = 15 + "a"

# IndexError: list index out of range
# lst = [10,5,3]
# print(lst[3])

# Коды завершения
# 0-все хорошо
# 1-ошибка
# -1- прерывание

# SyntaxError: unterminated string literal (detected at line 18)
# x = "Hello world.

# SyntaxError: expected ':'
# if 5 > 0

# ValueError: invalid literal for int() with base 10: 'A'
# x = int("A")


# assert
# def summa(number: list[int]):
#     return sum(number)
#  assert summa([1,3]) == 4 #ошибки нет
# assert summa([1,3]) == 5 #ошибка AssertionError

# try:
#     x = 5/0
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# print("Пока")
# #try - попытаться
# #except -ожтдать ошибки