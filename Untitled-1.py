import turtle
screen = turtle.Screen()
screen.bgcolor("black") 
t = turtle.Turtle() 
t.speed(0) 
t.width(2)
colors = ["red","magenta","blue","cyan","green","yellow"] 
for i in range(200):
 t.pencolor(colors[i % 6]) 
 t.forward(i * 3/ 2)
 t.left(59) 
turtle.done() 