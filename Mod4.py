import turtle
import colorsys


def draw_mod4():
    t = turtle.Turtle()
    turtle.Screen().bgcolor("black")
    t.speed(0)
    t.hideturtle()
    n = 100
    h = 0
    max_iterations = 76

    for i in range(360):
        if i>= max_iterations:
            break
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1 / n
        t.color(c)
        for j in range(2):
            t.left(250)
            t.forward(i * 3)
            for k in range(3):
                t.left(20)
                t.forward(22)
 #   turtle.done()
    t.clear()
 

def main():
    draw_mod4()


if __name__ == "__main__":
    main()
  
