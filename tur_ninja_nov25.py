# Rebecca Pedraza
# Nov 25

import turtle as t

# Purple square code 
def ninja_donatello(): # Function assigned with corresponding ninja color and name
    t.fillcolor("purple")  # Assign color 
    t.begin_fill() # Method used to fill the color assigned above
    for i in range(4):  # Loop created to draw equal sides of square
        t.forward(100) 
        t.right(90)
    t.end_fill() # Method used to end the filling from color assigned 

# Move to another position for Michelangelo
    t.penup()
    t.right(60)
    t.forward(100)
    t.pendown()
    
# Orange regular hexagon
def ninja_michelangelo(): # Function assigned with corresponding ninja color and name 
    t.fillcolor("orange")  # Assign color 
    t.begin_fill()  # Method used to fill the color assigned above
    for i in range(6):  # Loop created to draw 6 sides of hexagon
        t.forward(100)
        t.left(60)
    t.end_fill()  # Method used to end the filling from color assigned 
    
# Blue rectangle 
def ninja_leonardo(): # Function assigned with corresponding ninja color and name 
    t.fillcolor("blue") # Assign color 
    t.begin_fill()  # Method used to fill the color assigned above
    for i in range(2):  # Loop created to draw 2 equal sides 
        t.forward(150)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()  # Method used to end the filling from color assigned 

# Red non regular hexagon
def ninja_raphael(): # Function assigned with corresponding ninja color and name 
    t.fillcolor("red") # Assign color 
    t.begin_fill()  # Method used to fill the color assigned above
    t.forward(100)  
    t.left(60)      
    t.forward(150)  
    t.left(120)   
    t.forward(100) 
    t.left(90)      
    t.forward(120)  
    t.left(150)     
    t.forward(80)   
    t.left(100)     
    t.forward(130)  
    t.left(60)
    t.end_fill()  # Method used to end the filling from color assigned 

# Function to assign shapes with the names of turtles
def draw_all_shapes():
    ninja_donatello()

    # Move to another position for Michelangelo
    t.penup()
    t.right(60)
    t.forward(100)
    t.pendown()
    
    ninja_michelangelo()

    # Move to another position for Leonardo 
    t.penup()
    t.backward(500)
    t.forward(50)
    t.right(60)
    t.pendown()

    ninja_leonardo()

    # Move to another position for Rapahel
    t.penup()
    t.forward(350)
    t.left(45)
    t.pendown()

    ninja_raphael()

# Ask function to draw all the shapes
draw_all_shapes()

# Hide turtle 
t.hideturtle()
t.done()
