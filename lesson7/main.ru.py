# try:
#     int("x")
#     x = 5/0 # первая ошибка будет обработанна
#     except ZeroDivisionError
#     print("деление на ноль")
# except Exception:  # обработает любые ошибки
#     print("Я оюрабатываю все")
# try:
#     x = int(input("Введи число:"))
# except ValueError:
#     print("Э, уважаемый, хочу цифры!")
# else: # мы не наткнулись на ошибку
#     print("Ура, победа. Ты не глуп.")
# finally: #сработает всегда
#     print("Я отработал.")
# name = input("Введите имя:")
# if name == "Антон":
#     raise Exception("Антона нельзя") #вызвать собственную ошибку
# except Exception as error_message:
#       print("Одна ошибка и ты ошибся")
#       print("Ошибка-то фатальная:", error_message)
# try:
#     x = 5/0
# except:ZeroDivisionError
#        pass
#
# if 5 > 3: #если придумали условие
#     pass # но не пртдумали что делать
# temperature = 50 #typo
# print() #weak warning
# x / / 5 #красное-фатальное