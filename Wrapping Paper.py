# May Pena
# This program generates a sample wrapping paper
# for a hypothetical wrapping paper company.

# Libraries
from graphics import *
from random import *

class Car:
    '''a definition for a car made of 2 rectangles and 2 circles'''
    def __init__( self, topLeft, width, height, color ):
        self.topLeft = topLeft   # start of car
        self.width   = width     # width of car
        self.height  = height    # height of car
        self.color   = color     # color of car
        

        # places all parts of the car in their places
        # in respect to the other shapes
        x1 = topLeft.getX() 
        y1 = topLeft.getY()
        P2 = Point( x1 + width, y1 + height )
        P3 = Point( x1+20, y1-15 )
        P4 = Point( x1+55, y1+15 )

        self.head   = Rectangle( P3, P4 )
        self.body   = Rectangle( topLeft, P2 )
        center1     = Point( x1 + 10, y1 + height )
        self.wheel1 = Circle( center1, 5 )
        center2     = Point( x1 + width - 10, y1 + height )
        self.wheel2 = Circle( center2, 5 )

        # colors the wheels and the car
        self.head.setFill( color )
        self.body.setFill( color )
        self.wheel1.setFill( "black" )
        self.wheel2.setFill( "black" )
        
    # draw all the body parts of the car when constructor is called
    def draw( self, win ):
        self.head.draw(win )
        self.body.draw( win )
        self.wheel1.draw( win )
        self.wheel2.draw( win )

'''               _       
                 (_)      
  _ __ ___   __ _ _ _ __  
 | '_ ` _ \ / _` | | '_ \ 
 | | | | | | (_| | | | | |
 |_| |_| |_|\__,_|_|_| |_|
 
'''
        
def main():
    # draws window with lightblue background
    win  = GraphWin( "Wrapping Paper", 600, 350 )
    win.setBackground( "lightblue" )

    # nested loops that draw the cars 
    for i in range( N ):
        for j in range ( N ):
            # randomizes color
            color = color_rgb( randint( 0, 255),
                           randint( 0, 255),
                           randint( 0, 255))
            
            # calls construcor and draws car
            x = i * 100
            y = j * 60
            car = Car( Point( x + 5, y+ 20 ), 75, 15, color )
            car.draw( win )
    
    # closes window when it's clicked
    win.getMouse()
    win.close()

main()
