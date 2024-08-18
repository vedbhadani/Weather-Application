import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

bodies = []


main_screen= turtle.Screen()
main_screen.title('snake game')
main_screen.bgcolor('green')
main_screen.setup(width=600,height=600)



head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.fillcolor('blue')
head.penup()
head.goto(0,0)
head.direction='stop'


food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('yellow')
food.fillcolor('white')
food.penup()
food.ht()
food.goto(0,200)
food.st()


sb = turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()
sb.ht()
food.goto(-280,250)
sb.write('score: 0 | Highestscore: 0', font=('arial',15,'bold'))


