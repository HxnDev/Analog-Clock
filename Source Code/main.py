import turtle
import time

screen = turtle.Screen()    # Loading Canvas
screen.bgcolor("white")     # Bg
screen.setup(width=600, height=600)
screen.title("Analog Clock")
screen.tracer(0)

t = turtle.Turtle()
#t.hideturtle() # Make the turtle invisible
t.speed(0)  # Setting the speed to 0
t.pensize(3)    # Setting the pensize to 3


def Draw_Clock(hourr, minutee, secondd, t):

    t.up()  # not ready to draw
    t.goto(0, 210)  # positioning the turtle
    t.setheading(180)   # setting the heading to 180
    t.color("red")  # setting the color of the pen to red
    t.pendown()     # starting to draw
    t.circle(210)    # a circle with the radius 210

    t.up()  # not ready to draw
    t.goto(0, 0)    # positioning the turtle
    t.setheading(90)    # same as seth(90) in newer version

    for z in range(12):     # loop
        t.fd(190)   # moving forward at 190 units
        t.pendown()     # starting to draw
        t.fd(20)    # forward at 20
        t.penup()   # not ready to draw
        t.goto(0, 0)    # positioning the turtle
        t.rt(30)    # right at an angle of 30 degrees

    hands = [("black", 80, 12), ("black", 150, 60), ("black", 110, 60)]     # the color and the hands set
    time_set = (hourr, minutee, secondd)  # setting the time

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360     # setting the angle for the clock
        t.penup()   # not ready to draw
        t.goto(0, 0)    # positioning the turtle
        t.color(hand[0])    # setting the color of the hand
        t.setheading(90)    # same as seth(90)
        t.rt(angle)     # right at an angle of "right"
        t.pendown()     # ready to draw
        t.fd(hand[1])   # forward at a unit of 1st index of the hand var


while True:
    hourr = int(time.strftime("%I"))
    minutee = int(time.strftime("%M"))
    secondd = int(time.strftime("%S"))

    Draw_Clock(hourr, minutee, secondd, t)
    screen.update()     # updating the screen
    time.sleep(1)
    t.clear()
