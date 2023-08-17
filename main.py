from turtle import Turtle,Screen
import pandas as pd

map = Turtle()
scn = Screen()

img = 'india_map.gif'
ifile = '28_states.csv'
ofile = 'Ramining_states.csv'

scn.title("India States Quiz")
scn.addshape(img)
map.shape(img)
guessed_states = []
game_is_on = True
c = 5

df = pd.read_csv(ifile)
all_s = df.states
all_states = all_s.to_list()

while game_is_on:
    ans_state = scn.textinput(title="Guess the State", prompt="What's the next state name?").title()
    if ans_state == 'Exit':
        for s in all_s:
            if s not in ans_state:
                with open(ofile, "a+") as rem:
                    rem.write(s+"\n")
        break
    if ans_state in all_states:
        guessed_states.append(ans_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        data = df[df.states == ans_state]
        t.goto(int(data.x), int(data.y))
        t.write(data.states.item())
    else:
        t = Turtle()
        t.hideturtle()
        t.penup()
        c = c - 1
        t.goto(150, 150)
        t.write(f"Retry Count left {c}")
        if c == 0:
           game_is_on = False