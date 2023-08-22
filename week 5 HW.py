
import turtle
steve = turtle.Turtle()
steve.shape('turtle')
space = turtle.Turtle()
space.shape('turtle')
space.penup()
space.right(90)

steve.pensize(5)
space.color('red')
steve.color('blue')
space.forward(250)
steve.circle(90)
steve.right(72)
space.write('1 done 4 to go!')

space.forward(20)
steve.color('yellow')
steve.circle(90)
steve.right(72)
space.write('2 done 3 to go!')

space.forward(20)
steve.color('green')
steve.circle(90)
steve.right(72)
space.write('3 done 2 to go!')

space.forward(20)
steve.color('red')
steve.circle(90)
steve.right(72)
space.write(' 4 done 1 to go!')

space.forward(20)
steve.color('pink')
steve.circle(90)
steve.right(72)
space.write('5 done 0 to go!')

space.forward(20)
space.write('Good Job,Steve')

steve.penup()
steve.forward(200)
steve.write('Thanks bro')
