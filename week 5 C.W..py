
import turtle



hp = turtle.Turtle()
hp.shape('turtle')
hp.color('red')
hp.left(20)
hp.forward(80)
hp.right(120)
hp.forward(80)
hp.right(120)
hp.forward(80)
dell = turtle.Turtle()
dell.shape('turtle')
dell.color('blue')

dell.penup()
dell.forward(80)
dell.right(90)
dell.forward(200)
dell.write('1 done, 4 to go')
dell.forward(20)

hp.left(20)
hp.forward(80)
hp.right(120)
hp.forward(80)
hp.right(120)
hp.forward(80) 
dell.write('2 done, 3 to go')
dell.forward(20)

hp.left(20)
hp.forward(80)
hp.right(120)
hp.forward(80)
hp.right(120)
hp.forward(80) 
dell.write('3 done, 2 to go')
dell.forward(20)

hp.left(10)
hp.left(20)
hp.forward(80)
hp.right(120)
hp.forward(80)
hp.right(120)
hp.forward(80)
dell.write('4 done, 1 to go')
dell.forward(20)

hp.left(20)
hp.forward(80)
hp.right(120)
hp.forward(80)
hp.right(120)
hp.forward(80) 
dell.write('5 done, 0 to go')
dell.forward(20)
dell.write('great job Hp')

hp.penup()
hp.forward(100)
hp.color('green')
hp.write('thanks!', '19 pt')



