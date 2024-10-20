import turtle as t

SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'


def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-SIZE * COLUMNS / 2, SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)


# --------------------------- get color from number -------------------------- #
'''Fetches the color names from the file and assigns each one to an index'''
def get_color(num):
    try:
        # opens the file with the colorn names
        with open("color.txt", "r") as file:
            #splits the words by commas and arranges them into an array
            for word in file:
                color = word.split(",")
            '''Here it takes the input and decides whether it should be converted to an integer or (A)'''
            # instead of 10, the user should input A (to not confuse it with 1,0)
            if num.lower() == 'a': # a or A
                num = 10
            else:
                num = int(num)
            # takes the number and turns it into an integer to make it an index
            return color[num]
    except:
        # if the user enters a woopsie, then it will raise an exception and prevent the program from crashing
        return "Color not found"
    
# ----------------------- drawing the pixel with color ----------------------- #
'''Function which takes a color string and draws a pixel with that color'''
def draw_color_pixel(color_string):
    t.pendown()
    t.fillcolor(color_string)
    t.begin_fill()
    # drawing the pixel/square
    for i in range(4):
        t.forward(SIZE)
        t.right(90)
    t.end_fill()
    
    
# --------------------------- draw line from string -------------------------- #
'''Takes in a string and converts each charcter into a color and then draws each pixel with that character in a line'''
def draw_line_from_string(line_string):
    try:
        length = 0
        if line_string == '': # Raising a value error (go to except block)
            raise ValueError
        for char in line_string: # For each charcter
            draw_color_pixel(get_color(char))
            t.forward(SIZE)
            length +=1
        # Go back to the beginning of the line
        t.penup()
        t.backward(length*SIZE)
        t.right(90)
        t.forward(SIZE)
        t.left(90)
    #If the user enters an empty string
    except ValueError:
        print("You cannot enter an empty string")
    #If the user enters a bad color string
    except:
        print('Invalid Input')

# ------------------------------ draw from file ------------------------------ #
'''Takes in the text from the file and applies the previous function which draws each pixel by converting numbers(and A) to colors'''
def draw_shape_from_file(doc):
    try:
        with open(doc, "r") as file:
            for line in file:
                line = line.strip() # This is to prevent the program from going "oh whitespace? ok no thanks, Ill stop working"
                draw_line_from_string(line)
    # Incase the user enters the name of a file that does not exist or if they typed it wrong because human error or whatever
    except FileNotFoundError:
        print('FILE NOT FOUND') 

# -------------------------- draw red and black grid ------------------------- #
def draw_grid():
    # If statement, superrrr easyyy for me ofc, just runs this like 20 times, draws one lines, then the second then yeah!!!
    for i in range(20):
        # Honestly for this one, literally just says like if the i (the range) is even itll start with black and if its odd itll start with red
        if i % 2 == 0:
            draw_line_from_string('02020202020202020202') #blackredblackredblackred...x20
        else:
            draw_line_from_string('20202020202020202020') #redblackredblackredblack...x20
        

                 


        


