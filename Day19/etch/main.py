from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def turn_left():
    arrow.left(10)

def turn_right():
    arrow.right(10)

def move_foreward():
    arrow.forward(10)

def move_backward():
    arrow.backward(10)

def clear_screen():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()

screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=move_foreward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_screen)


screen.listen()  
screen.exitonclick()
