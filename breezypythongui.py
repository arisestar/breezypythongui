"""
File: breezypythongui.py
Version: 1.0
Copyright 2012 by Ken Lambert
​
Resources for easy Python GUIs.
​
LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).  Its capabilities mirror those 
of BreezyGUI and BreezySwing, open-source frameworks for writing GUIs in Java,
written by Ken Lambert and Martin Osborne.
​
PLATFORMS: The package is a wrapper around tkinter (Python 3.X) and should
run on any platform where tkinter is available.
​
INSTALLATION: Put this file where Python can see it.
​
"""
​
import tkinter
import tkinter.simpledialog
​
N = tkinter.N
S = tkinter.S
E = tkinter.E
W = tkinter.W
CENTER = tkinter.CENTER
END = tkinter.END
NORMAL = tkinter.NORMAL
DISABLED = tkinter.DISABLED
NONE = tkinter.NONE
WORD = tkinter.WORD
VERTICAL = tkinter.VERTICAL
HORIZONTAL = tkinter.HORIZONTAL
RAISED = tkinter.RAISED
SINGLE = tkinter.SINGLE
ACTIVE = tkinter.ACTIVE
​
class EasyFrame(tkinter.Frame):
    """Represents an application window."""
​
    def __init__(self, title = "", width = None, height = None,
                 background = "white", resizable = True):
        """Will shrink wrap the window around the widgets if width
        and height are not provided."""
        tkinter.Frame.__init__(self, borderwidth = 4, relief = "sunken")
        if width and height:
            self.setSize(width, height)
        self.master.title(title)
        self.grid()
        # Expand the frame within the window
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = N+S+E+W)
        # Set the background color and resizability
        self.setBackground(background)
        self.setResizable(resizable)
​
    def setBackground(self, color):
        """Resets the window's background color to color."""
        self["background"] = color
​
    def setResizable(self, state):
        """Resets the window's resizable property to True
        or False."""
        self.master.resizable(state, state)
​
    def setSize(self, width, height):
        """Resets the window's width and height in pixels."""
        self.master.geometry(str(width)+ "x" + str(height))
​
    def setTitle(self, title):
        """Resets the window's title to title."""
        self.master.title(title)
​
    # Methods to add widgets to the window.  The row and column in
    # the grid are required arguments.
​
    def addLabel(self, text, row, column,
                 columnspan = 1, rowspan = 1,
                 sticky = N+W, font = None,
                 background = "white", foreground = "black"):
        """Creates and inserts a label at the row and column,
        and returns the label."""
        label = tkinter.Label(self, text = text, font = font,
                              background = background,
                              foreground = foreground)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        label.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return label
​
    def addButton(self, text, row, column,
                  columnspan = 1, rowspan = 1,
                  command = lambda: None,
                  state = NORMAL):
        """Creates and inserts a button at the row and column,
        and returns the button."""
        button = tkinter.Button(self, text = text,
                                command = command, state = state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        button.grid(row = row, column = column,
                    columnspan = columnspan, rowspan = rowspan,
                    padx = 5, pady = 5)
        return button
​
    def addFloatField(self, value, row, column,
                      columnspan = 1, rowspan = 1,
                      width = 20, precision = None,
                      sticky = N+E, state = NORMAL):
        """Creates and inserts a float field at the row and column,
        and returns the float field."""
        field = FloatField(self, value, width, precision, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field
​
    def addIntegerField(self, value, row, column,
                        columnspan = 1, rowspan = 1,
                        width = 10, sticky = N+E, state = NORMAL):
        """Creates and inserts an integer field at the row and column,
        and returns the integer field."""
        field = IntegerField(self, value, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field
​
    def addTextField(self, text, row, column,
                     columnspan = 1, rowspan = 1,
                     width = 20, sticky = N+E, state = NORMAL):
        """Creates and inserts a text field at the row and column,
        and returns the text field."""
        field = TextField(self, text, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field
​
    def addTextArea(self, text, row, column, rowspan = 1, columnspan = 1,
                    width = 80, height = 5, wrap = NONE):
        """Creates and inserts a multiline text area at the row and column,
        and returns the text area.  Vertical and horizontal scrollbars are
        provided."""
        frame = tkinter.Frame(self)
        frame.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        xScroll = tkinter.Scrollbar(frame, orient = HORIZONTAL)
        xScroll.grid(row = 1, column = 0, sticky = E+W)
        yScroll = tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        area = TextArea(frame, text, width, height,
                        xScroll.set, yScroll.set, wrap)
        area.grid(row = 0, column = 0,
                  padx = 5, pady = 5, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        xScroll["command"] = area.xview
        yScroll["command"] = area.yview
        return area
​
    def addListbox(self, row, column, rowspan = 1, columnspan = 1,
                   width = 10, height = 5, listItemSelected = lambda index: index):
        """Creates and inserts a scrolling list box at the row and column, with a
        width and height in lines and columns of text, and a default item selection
        method, and returns the list box."""
        frame = tkinter.Frame(self)
        frame.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        yScroll = tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        listBox = EasyListbox(frame, width, height, yScroll.set, listItemSelected)
        listBox.grid(row = 0, column = 0, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        yScroll["command"] = listBox.yview
        return listBox
​
    def addCanvas(self, canvas = None, row = 0, column = 0,
                  rowspan = 1, columnspan = 1, width = 200, height = 100,
                  background = "white"):
        """Creates and inserts a canvas at the row and column,
        and returns the canvas."""
        if not canvas:
            canvas = EasyCanvas(self, width = width, height = height,
                                background = background)
        canvas.grid(row = row, column = column,
                    rowspan = rowspan, columnspan = columnspan,
                    sticky = W+E+N+S)
        self.columnconfigure(column, weight = 10)
        self.rowconfigure(row, weight = 10)
        return canvas
​
    def addScale(self, row, column, rowspan = 1, columnspan = 1,
                 command = lambda value: value, from_ = 0, to = 0,
                 label = "", length = 100, orient = HORIZONTAL,
                 resolution = 1, tickinterval = 0):
        """Creates and inserts a scale at the row and column,
        and returns the scale."""
        scale = tkinter.Scale(self, command = command, from_ = from_, to = to,
                              label = label, length = length,
                              orient = orient, resolution = resolution,
                              tickinterval = tickinterval, relief = "sunken",
                              borderwidth = 4)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        scale.grid(row = row, column = column, columnspan = columnspan,
                   rowspan = rowspan, sticky = N+S+E+W)
        return scale
​
    def addMenuBar(self, row, column, rowspan = 1, columnspan = 1,
                   orient = "horizontal"):
        """Creates and inserts a menu bar at the row and column,
        and returns the menu bar."""
        if not orient in ("horizontal", "vertical"):
            raise ValueError("orient must be horizontal or vertical")
        menuBar = EasyMenuBar(self, orient)
        menuBar.grid(row = row, column = column,
                     rowspan = rowspan, columnspan = columnspan,
                     sticky = N+W)
        return menuBar
​
    def addCheckbutton(self, text, row, column,
                       rowspan = 1, columnspan = 1,
                       sticky = N+S+E+W, command = lambda : 0):
        """Creates and inserts check button at the row and column,
        and returns the check button."""
        cb = EasyCheckbutton(self, text, command)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        cb.grid(row = row, column = column,
                columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return cb
​
    def addRadiobuttonGroup(self, row, column,
                            rowspan = 1, columnspan = 1, orient = VERTICAL):
        """Creates and returns a radio button group."""
        return EasyRadiobuttonGroup(self, row, column, rowspan, columnspan, orient)
​
    # Added 12-18-2012
    def addPanel(self, row, column,
                 rowspan = 1, columnspan = 1, background = "white"):
        """Creates and returns a panel."""
        return EasyPanel(self, row, column, rowspan, columnspan, background)
​
    # Method to pop up a message box from this window.
​
    def messageBox(self, title = "", message = "", width = 25, height = 5):
        """Creates and pops up a message box, with the given title,
        message, and width and height in rows and columns of text."""
        dlg = MessageBox(self, title, message, width, height)
        return dlg.modified()
​
    # Method to pop up a prompter box from this window.
​
    def prompterBox(self, title = "", promptString = "", inputText = "", fieldWidth = 20):
        ""&...
Collapse
