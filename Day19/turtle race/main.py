from turtle import Turtle, Screen
import random

def initialise_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    interval = (120 - (-120))/len(colors) - 1
    turtles = []

    for index, color in enumerate(colors):
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        position = 120 - interval * index
        turtle.penup()
        turtle.goto(-230, position)
        turtles.append(turtle)
    return turtles    

def race(turtles):
    while(True):
        for turtle in turtles:
            turtle.forward(random.randint(1,15))
            if(turtle.xcor() >= 220):
                return turtle.color()[0]

def check_bet(winner, user_bet):
    if user_bet == winner:
        print("You won")
    else:
        print(f"you lost, {winner} won")


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()
turtles = initialise_turtles()
winner = race(turtles)
check_bet(winner=winner, user_bet=user_bet)
screen.exitonclick()