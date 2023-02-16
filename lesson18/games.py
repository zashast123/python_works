import easygui
import random

def rock_paper_scissors():
    r = "img/efefeff.png"
    p ="img/efeplokeff.png"
    s ="img/efefssffeff.png"

    vtm = s

x =  ez.buttonbox(litle="тут есть кмень смерти ",
               msg="Выбери что нибудь",
               images=["img/kamenBeskonechosti.png","img/rukasmerti.png", "img/ldfjrrokjgegjgo.png"],
                choices=("выход")
                )

   if x == s and vtm == s:
       ex.msgbox(msg="ичья")

if x == s and vtm == s:
    ex.msgbox(msg="ичья")
elif x == p and vtm == p: ex.msgbox(msg="ичья")
elif x == r and vtm == r: ex.msgbox(msg="ичья")
elif x == r and vtm == p: ex.msgbox(msg="ичья")
elif x == r and vtm == s: ex.msgbox(msg="ичья")
else:
    msg("irhfugfgfgfgfuujuuugdc")
def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')
`

games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()