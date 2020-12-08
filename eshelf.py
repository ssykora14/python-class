"""

Author: Sally S.
Program Name: eShelf.py
Description: An update of the ATM program that will display
a warning that the police will be called after 3 unsuccessful
attempts and disable the login button.

"""

from breezypythongui import EasyFrame
import pandas
import random
 
 
class eShelf(EasyFrame):
 
    def __init__(self):
        EasyFrame.__init__(self, "Sally's eShelf Project")
        dataPanel = self.addPanel(row = 0, column = 0,
                                  background = "gray")

        # Initialize inputs for books
        dataPanel.addLabel(text = "Title", row = 0, column = 0,
                           background = "gray")
        dataPanel.addTextField(text = "Add Title", row = 0, column = 1)
        dataPanel.addLabel(text = "Author", row = 1, column = 0,
                           background = "gray")
        dataPanel.addTextField(text = "Add Author", row = 1, column = 1,)
        dataPanel.addLabel(text = "Genre", row = 2, column = 0,
                           background = "gray")

        # Initialize genre drop down menu
        menuBar = dataPanel.addMenuBar(row = 2, column = 1)
        fileMenu = menuBar.addMenu("Genre")
##        fileMenu.addMenuItem("Action", command?)

        # Create the nested frame for the button panel
        buttonPanel = self.addPanel(row = 1, column = 0,
                                    background = "black")

        # Create and add buttons to the button panel
        buttonPanel.addButton(text = "Add Book", row = 0, column = 0)
        buttonPanel.addButton(text = "Remove Book", row = 0, column = 1)
        buttonPanel.addButton(text = "Give Me a Recommendation", row = 0, column = 2)

def main():
    """Instantiate and pop up the window."""
    eShelf().mainloop()

if __name__ == "__main__":
    main()

