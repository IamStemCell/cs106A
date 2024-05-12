import turtle

def main():
   
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.title("Koch Snowflake for Code In Place 2024 by Svitlana P")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.hideturtle()
    
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    koch_snowflake(t, 4, 300)

    screen.mainloop()

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    t.hideturtle()

if __name__ == "__main__":
    main()
  
