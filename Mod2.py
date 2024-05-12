
from turtle import*

def polygon(sides, side_len):
    speed(0)
    bgcolor("black")
    color("white")
    hideturtle()
    for i in range(0,sides):
        forward(side_len)
        left(360/sides)
    if side_len > 0:
        left(2)
        polygon(sides, side_len-1)
    clear()

def main():
    polygon(5,150)

 
if __name__ == "__main__":
    main()
 

