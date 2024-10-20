import turtle as t
from pixart import *

''' Imports everything (*) from the pixart.py '''


'''
*       *   *       *       *   *       *       *   *       *

    *   M A I N     F U N C T I O N     B E L O W   *

*       *   *       *       *   *       *       *   *       *
'''
# Fastest speed (vroooooooooooooooooooooom)
t.speed(0)

def main():
    # Goes to the top left of the screen
    t.penup()
    t.goto(-(SIZE*10), (SIZE*10))
    t.pendown()
    # Prompts the user to pick which type of grid they want to make
    pick = input("Which type of grid would you like 1-Red&Black 2-ColorFromString 3-DrawFromFile: ")
    # If the user types 1, it will draw a red and black grid
    if pick == '1':
        draw_grid()
    # If the user types 2, it will draw pixels from the line of characters
    elif pick == '2':
        #So it will continue running after going to the second line, third line, and so on...
        while True:
            line_string = input("Enter a line of characters (or 'q' to quit): ")
            if line_string.lower() == 'q':
                break
            draw_line_from_string(line_string)
    # If the user types 3, it will draw the grid based on which text file the user picks, unless it doesnt exists then yikes, big fat error
    elif pick == '3':
        file_name = input('Enter file name: ')
        draw_shape_from_file(file_name)
    # If the user types anything else, it will say "Invalid input"
    else:
        print("Invalid choice. Please choose 1, 2 or 3")
    # This just stops the window from going bye bye as soon as the program finishes running :-)
    t.Screen().exitonclick()

''' This just runs the main function, but in a complicated way for some reason'''
if __name__ == '__main__':
    main()