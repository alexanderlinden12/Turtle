import turtle

myPen = turtle.Turtle()
screen = turtle.Screen()
screen.setworldcoordinates(-100, -100, 100, 100)
myPen.speed(0)

def drawAxis():
    myPen.penup()
    myPen.goto(-100,0)
    myPen.pendown()
    myPen.goto(100,0)

    myPen.penup()
    myPen.goto(0, -100)
    myPen.pendown()
    myPen.goto(0, 100)

def first(a, b):
    myPen.penup()
    for x in range(-10, 11):
        y = a * x*a+b
        myPen.goto(x, y)
        myPen.pendown()


drawAxis()
myPen.color('purple')
for i in range(10000):
    first((10*i), 0,)


