##
##Square colored
##import turtle
##t = turtle.Turtle()
##t.fillcolor('silver')
##t.begin_fill()
##t.forward(150)
##t.right(90)
##t.forward(150)
##t.right(90)
##t.forward(150)
##t.right(90)
##t.forward(150)
##t.right(90)
##t.end_fill()

#Hexagon colored
##import turtle
##t=turtle.Turtle()
##t.fillcolor('yellow')
##t.begin_fill()
##t.forward(125)
##t.right(60)
##t.forward(125)
##t.right(60)
##t.forward(125)
##t.right(60)
##t.forward(125)
##t.right(60)
##t.forward(125)
##t.right(60)
##t.forward(125)
##t.end_fill()          



import turtle
t = turtle.Turtle

turtle.setup(600,400)
wn = turtle.Screen()
wn.bgcolor('black')

t = turtle.Pen()
t.shape('turtle')
t.penup()

t.color('Chartreuse')
t.backward(100)
t.stamp()

t.color('pink')
t.forward(40)
t.stamp()

t.color('Crimson')
t.forward(40)
t.stamp()

t.color('maroon')
t.forward(40)
t.stamp()

t.color('green')
t.forward(40)
t.stamp()

t.color('yellow')
t.forward(40)
t.stamp()

