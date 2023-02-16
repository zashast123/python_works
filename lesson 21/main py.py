 # f = open("8b дежкрный класс.txt", "w")
 # f.write("hello world\n")
 # f.write("volvo")
 #
 # f.close()
#  f = open("8b дежкрный класс.txt", "r" encoding = "utf-8")
# content = f.read()
# content = f.readlines()
# print(F"Первая линия:{content[0]}")
# print(content)
# for line in content
#     print(line. rstrip())
#  f.close()


# f = open("data.txt", "w", encoding = "utf-8")
# f.write("My Rodina is Novosibirsk")
# f.write("Привет\n")
# f.write("МИР\n")
# f.write("и Movavi\n")
# f.close()
# name = input("Введите имя файла:")
# text = input(">")
# f = open(f"{name}.txt", "w", encoding = "utf-8")
# while text != "":
#      f.write(text)
#      text = input(">")
# f.close()
# print("Файл записан.")
#
# f.close()
# f = open("text.txt", "r", encoding="utf-8")
# content = f.readlines()
# count =1
# for lion in content:
#     result = f"{count}) {lion}"
#     f.write(result)
#     count += 1
# print(content)
n = int(input("N ="))
f = open("text.txt", "r", encoding="utf-8")
elements = f.readlines()


f.close()
a = (elements[:n])
for element in a:
    print(element.rstrip())