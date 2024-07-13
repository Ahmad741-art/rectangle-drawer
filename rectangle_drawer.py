import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        drawer.forward(width)
        drawer.right(90)
        drawer.forward(height)
        drawer.right(90)

# Draw a rectangle with width 150 and height 100
draw_rectangle(150, 100)

# Hide the turtle and display the window
drawer.hideturtle()
wn.mainloop()
