
import turtle
import math
import colorsys

def main():
# Draw the sunflower
    draw_sunflower()
    #turtle.done()

# Function to draw a single sunflower seed with changing color
def draw_seed():
    # Calculate color based on hue component
    global hue
    hue += 0.01
    if hue > 1:
        hue = 0
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()

# Function to draw the sunflower
def draw_sunflower():
    turtle.speed(0)
    turtle.bgcolor("black")  # Set background color to black
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.hideturtle()
    # Define parameters for the sunflower pattern
    c = 4  # constant for the spiral
    phi = (1 + math.sqrt(5)) / 2  # golden ratio
    
    for i in range(500):
        angle = i * math.pi * 2 / phi
        radius = c * math.sqrt(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_seed()
    turtle.clear()

# Initialize hue for color cycling
hue = 0


if __name__ == "__main__":
    main()

