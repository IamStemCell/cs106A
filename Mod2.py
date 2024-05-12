
from turtle import*

def main():
    polygon(5,150)

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

 
if __name__ == "__main__":
    main()
 

