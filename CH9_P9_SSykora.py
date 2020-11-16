"""

Author: Sally S. and Zachary R.
Date: 11/15/20
Program Name: GUI Card Program
Description: GUI program that will shuffle and display a
deck of playing card

"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from cards import Deck, Card

class GUI_Cards(EasyFrame):
   
    def __init__(self):
        """Creates the dice, and sets up the Images and labels
        for the two dice to be displayed, the state label,
        and the two command buttons."""
        EasyFrame.__init__(self, title = "GUI Cards")
        self.setSize(220, 200)
        self.deck = Deck()
        self.deck.shuffle()
        card = ""
        self.cardLabel = self.addLabel("", row = 0,
                                       column = 1,
                                       sticky = "NSEW")
        self.stateLabel = self.addLabel("", row = 1, column = 0,
                                        sticky = "NSEW",
                                        columnspan = 2)
        self.addButton(row = 2, column = 0,
                       text = "Deal",
                       command = self.deal)
        self.addButton(row = 2, column = 1,
                       text = "Shuffle",
                       command = self.shuffle)

        self.addButton(row = 2, column = 2,
                       text = "New deck",
                       command = self.newDeck)
        self.refreshImages(card)

    def deal(self):
        """Rools the dice and updates the view with
        the results."""
        card = self.deck.deal()
        self.stateLabel["text"] = card
        self.refreshImages(card)

    def shuffle(self):
        """Rools the dice and updates the view with
        the results."""
        self.deck.shuffle()
        self.stateLabel["text"] = ""
        card = ""
        self.refreshImages(card)

    def newDeck(self):
        """Create a new craps game and updates the view."""
        self.deck = Deck()
        self.deck.shuffle()
        self.stateLabel["text"] = ""
        card = ""
        self.refreshImages(card)
        
    def refreshImages(self, card):
        """Updates the images in the window."""
        try:
            fileName = "DECK/" + str(card.rank) + str((card.suit[0]).lower()) + ".gif"
            self.image = PhotoImage(file = fileName)
            self.cardLabel["image"] = self.image
        except Exception:
            fileName = "DECK/b.gif"
            self.image = PhotoImage(file = fileName)
            self.cardLabel["image"] = self.image
            
def main():
    GUI_Cards().mainloop()

if __name__ == "__main__":
    main()
