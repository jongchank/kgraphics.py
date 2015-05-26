# kgraphics.py

This is a slightly modified version from the original graphics.py
to support the right mouse click event. It adds two additional methods,
i.e., getMouse2() and checkMouse2(). They return a tuple containing the
Point object and the button name. The following is a simple usage:

--------------------------
p, button = win.getMouse2()
--------------------------

Then the variable button will contain 'Left' or 'Right' whichever you
press.
