import random
import turtle as t


tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

tim.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph( size_of_gap ):

    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap )
        tim.pencolor(random_color())

draw_spirograph(2)
screen.exitonclick()

