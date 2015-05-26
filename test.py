from kgraphics import *

win = GraphWin(height = 500, width = 500)

while True:
    p, button = win.getMouse2()
    print(p.getX(), p.getY(), button)
