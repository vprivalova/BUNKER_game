import time
import random
import subprocess
import sys
from PIL import Image
from urllib.request import urlopen
import game_bot as bt
import ru_local as ru
listt = bt.name
actions = ru.ALL_ACTIONS

subprocess.Popen([sys.executable, 'game_bot.py'])


def showtime():
    mytime = 120
    for x in range(mytime, 0, -1):
        print(x)
        time.sleep(1)
    print('Время вышло!')


print(ru.HELLO)


a = input(ru.A_TEXT_1)
if a == '+':
    url = "https://sun9-74.userapi.com/impg/7WGbMwaGQ9ScMwwsaFtWPsSzr6mOa76b9FCSsg/jSQ4y2ARP20.jpg?size=292x326&quality=95&sign=b903a2d82a098d44fa9bf188f2fbb688&type=album"

    image = Image.open(urlopen(url))
    image.show()
else:
    print(ru.A_TEXT_2)


b = input(ru.B_TEXT_1)

if b == '+':
    print(f'В бункере сейчас находятся: {listt}')
    print(ru.B_TEXT_2)
    q = input(ru.Q_TEXT_1)
    print(ru.TIME)
else:
    print(ru.REM)

showtime()

c = input(ru.KIK)

if c in listt:
    listt.remove(c)
    print(f'игрок {c} изгнан из бункера')
else:
    z = (random.sample(listt, 1))[0]
    listt.remove(z)
    print((random.sample(actions, 1))[0], z)

print(ru.HOB)
d = input(ru.D_TEXT_1)


if d == '+':
    print(ru.D_TEXT_2)

    q = input(ru.Q_TEXT_1)
    print(ru.TIME)
    showtime()
    e = input(ru.KIK)
    if e in listt:
        listt.remove(e)
        print(f'игрок {e} изгнан из бункера»')
    else:
        z = (random.sample(listt, 1))[0]
        listt.remove(z)
        print((random.sample(actions, 1))[0], z)
else:
    print(ru.REM)

print(ru.F_TEXT_1)
f = input(ru.F_TEXT_2)


if f == '+':
    print(ru.F_TEXT_3)

    q = input(ru.Q_TEXT_1)
    print(ru.TIME)
    showtime()
    g = input(ru.KIK)
    if g in listt:
        listt.remove(g)
        print(f'игрок {g} изгнан из бункера»')
    else:
        z = (random.sample(listt, 1))[0]
        listt.remove(z)
        print((random.sample(actions, 1))[0], z)
else:
    print(ru.REM)


print(ru.H_TEXT_1)
h = input(ru.H_TEXT_2)


if h == '+':
    print(ru.H_TEXT_3)

    q = input(ru.Q_TEXT_1)
    print(ru.TIME)
    showtime()
    j = input(ru.KIK)
    if j in listt:
        listt.remove(j)
        print(f'игрок {j} изгнан из бункера')
    else:
        z = (random.sample(listt, 1))[0]
        listt.remove(z)
        print((random.sample(actions, 1))[0], z)


print(ru.M_TEXT_1)
m = input(ru.M_TEXT_2)


if m == '+':
    print(ru.M_TEXT_3)
    q = input(ru.Q_TEXT_1)
    print(ru.TIME)
    showtime()
    p = input(ru.KIK)
    if p in listt:
        listt.remove(p)
        print(f'игрок {p} изгнан из бункера')
        print(ru.END_1)
    else:
        z = (random.sample(listt, 1))[0]
        listt.remove(z)
        print((random.sample(actions, 1))[0], z)
        print(ru.END_2)
else:
    print(ru.REM)

print(listt)
print(ru.THANK)
