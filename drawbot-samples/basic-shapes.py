# Lines staring with a # are commented so they are not interpreted as a line of code


# setting up a page
newPage(600, 600)


# draw shapes
# uncomment ### triple hastagged lines to see in effect

# rectangle
#    x    y    w    h
### rect(50, 50, 500, 500)


# oval
#    x    y    w    h
### oval(50, 50, 500, 500)
### oval(50, 50, 250, 500)


# stroke color (black, rgba)
stroke(0)
# line between two points
#    point 1      point 2
#     x    y      x    y
### line((100, 100), (500, 500))
### line((100, 500), (500, 100))


# a polygon with x points
#        point 1      point 2    point 3    point 4
#         x    y      x    y    x     y      x    y    close shape
### polygon((100, 100), (100, 500), (500, 500), (200, 100), close=True)
#        point 1      point 2    point 3    point 4    point 5
#         x    y      x    y    x     y      x    y       x    y  close shape
### polygon((100, 100), (100, 500), (500, 500), (400, 300), (200, 100),close=True)