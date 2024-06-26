
from turtle import *
import colorsys

def main():
    draw_flower()


def draw_flower():
    speed(0)
    bgcolor("black")
    hideturtle()
    h = 0
    for i in range(16):
        for j in range(18):
            c = colorsys.hsv_to_rgb(h,1,1)
            color(c)
            h+= 0.005
            rt(90)
            circle(150 - j*6,90)
            lt(90)
            circle(150 - j*6,90)
            rt(180)
        circle(40,24)
    clear()


if __name__ == "__main__":
    main()
  
