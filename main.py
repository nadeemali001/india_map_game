from turtle import Turtle,Screen
import pandas as pd

map = Turtle()
scn = Screen()

img = 'india_map.gif'
ifile = '28_states.csv'

scn.title("India States Quiz")
scn.addshape(img)
map.shape(img)

game_is_on = True
c = 5

df = pd.read_csv(ifile)
all_s = df.states.str.lower()
all_states = all_s.to_list()

while game_is_on:
    ans_state = scn.textinput(title="Guess the State", prompt="What's the next state name?").lower()
    if ans_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        data = df[df.states.str.lower() == ans_state.lower()]
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


# while game_is_on:
#     ans_state = scn.textinput(title="Guess the State", prompt="What's the next state name?")
#     t = Turtle()
#     t.hideturtle()
#     t.penup()
#     df = pd.read_csv(ifile)
#     res = (df.loc[df['states'] == ans_state])
#     if not res.empty:
#         final = res.values.tolist()
#         x=final[0][1]
#         y=final[0][2]
#         t.goto(x, y)
#         t.write(final[0][0])
#     else:
#         c = c - 1
#         t.goto(150, 150)
#         t.write(f"Retry Count left {c}")
#         if c == 0:
#             game_is_on = False

scn.exitonclick()