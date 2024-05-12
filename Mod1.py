from turtle import*

def main():
    draw_mod1()
 
def square():
    bgcolor('black')
    color('white')
    speed(0)
    hideturtle()
    for i in range(4):
        forward(200)
        right(90) #this 1 square
def draw_mod1():
    speed(0)
    for j in range(72):
        square()
        right(5)
        square()
    clear()
#72 squares each moving 5 degrees to the right


 

if __name__ == "__main__":
    main()

