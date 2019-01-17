"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Emma Lipkowski.
"""
########################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow
dude = rg.SimpleTurtle('turtle')
dude.pen = rg.Pen('aqua', 3)
dude.speed = 50

size = 150

for k in range(12):
    dude.draw_regular_polygon(10, 30)

    dude.pen_up()
    dude.backward(10)
    dude.left(45)
    dude.forward(10)
    dude.right(15)
    dude.pen_down()
    size = size - 12

gal = rg.SimpleTurtle('turtle')
gal.pen = rg.Pen('magenta', 3)
gal.speed = 50

size = 100

for k in range(8):
    gal.draw_square(150)

    gal.pen_up()
    gal.backward(50)
    gal.left(135)
    gal.forward(50)
    gal.left(90)
    gal.pen_down()
    size = size - 12
