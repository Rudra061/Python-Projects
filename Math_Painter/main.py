from canvas import Canvas
from shapes import Square, Rectangle

# get canvas width and height from user
canvas_width = int(input("Enter canvas width : "))
canvas_height = int(input("Enter canvas height : "))

# make a dict of color codes and prompt for color
color = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter canvas color (black or white) : ")

# create a canvas with the user provided data
canvas = Canvas(height=canvas_height, width=canvas_width, color= color[canvas_color])

while True:
    shape_type = input("what do you like to draw? enter quit to stop. : ")

    # ask for rectangle data and create rectangle if user enteted rectangle
    if shape_type == "rectangle":
        rec_x = int(input("Enter x of the rectangle : "))
        rec_y = int(input("Enter y of the rectangle : "))
        rec_width = int(input("Enter width of the rectangle : "))
        rec_height = int(input("Enter height of the rectangle : "))
        red = int(input("How much red should the rectangle have ? : "))
        green = int(input("How much green should the rectangle have ? : "))
        blue = int(input("How much blue should the rectangle have ? : "))

        # create a rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type == "square":
        sqr_x = int(input("Enter x of the square : "))
        sqr_y = int(input("Enter y of the square : "))
        sqr_side = int(input("Enter side of the square : "))
        red = int(input("How much red should the square have ? : "))
        green = int(input("How much green should the square have ? : "))
        blue = int(input("How much blue should the square have ? : "))

        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == "quit":
        break

canvas.make('canvas.png')