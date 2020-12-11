"""

Author: Sally S.
Program Name: eShelf.py
Description: A GUI eShelf program. The program can add books to a csv, remove books, and
reccommend a random book or by genre.

"""

from breezypythongui import EasyFrame
##import tkinter as tk
from tkinter import ttk
import pandas
import random
import csv

class eShelf(EasyFrame):
 
    def __init__(self):
        EasyFrame.__init__(self, "Sally's eShelf Project")
        dataPanel = self.addPanel(row = 0, column = 0,
                                  background = "gray")

        # Initialize inputs for title and author
        dataPanel.addLabel(text = "Title", row = 0, column = 0,
                           background = "gray")
        self.title = dataPanel.addTextField(text = "Add Title", row = 0, column = 1, width = 35)
        dataPanel.addLabel(text = "Author", row = 1, column = 0,
                           background = "gray")
        self.author = dataPanel.addTextField(text = "Add Author", row = 1, column = 1, width = 35)
        dataPanel.addLabel(text = "Genre", row = 2, column = 0,
                           background = "gray")

        # Initialize genre drop down menu
        self.genrechoosen = ttk.Combobox(dataPanel, width = 30, state="readonly")
        self.genrechoosen['values'] = ('Choose a genre:',
                                       'Anthology',
                                       'Classic',
                                       'Fantasy',
                                       'Fiction',
                                       'Graphic Novel',
                                       'Historical Fiction',
                                       'Horror',
                                       'Non-fiction',
                                       'Poetry',
                                       'Romance',
                                       'Sci Fi',
                                       'Thriller',
                                       )
        self.genrechoosen.grid(row = 2, column = 1)
        self.genrechoosen.current(0)
        

        # Create the nested frame for the button panel
        buttonPanel = self.addPanel(row = 1, column = 0,
                                    background = "black")
        buttonPanel.addButton(text = "Add Book", row = 0, column = 0, command = self.add_book)
        buttonPanel.addButton(text = "Remove Book", row = 0, column = 1, command = self.remove_book)
        buttonPanel.addButton(text = "Give Me a Recommendation", row = 0, column = 2, command = self.get_random)
        buttonPanel.addButton(text = "Help", row = 0, column = 4, command = self.help)

    def add_book(self):
        title = self.title.getText()
        author = self.author.getText()
        genre = self.genrechoosen.get()

        # field names
        book = {
            "Title": title,
            "Author": author,
            "Genre": genre
            }

        if title == "Add Title" or genre == "Choose a genre:":
            text = self.messageBox(title = "Error", message = "You must enter a title and choose a genre to add a book." )

        else:
            # writing to csv file
            try:
                with open("data/bookshelf.csv", 'a+', newline='') as bookshelf:
                    addbook = csv.writer(bookshelf)
                    addbook.writerow(book.values())

                text = self.messageBox(title = "Book Added", message = "Your book has been added.")
            except:
                text = self.messageBox(title = "Error", message = "You must have a csv named 'bookshelf.csv' in the data folder." )

    def remove_book(self):
        
        removedBook = self.title.getText()
        if removedBook == "Add Title":
            text = self.messageBox(title = "Error", message = "You must enter a title to remove a book." )
        else:
            try:
                bookshelf = pandas.read_csv('data/bookshelf.csv')
                removeRow = bookshelf[bookshelf['Title'] == removedBook].index.values
                if len(removeRow) == 0:
                    text = self.messageBox(title = "Error", message = "That title wasn't found on the list." )
                else:
                    bookshelf = bookshelf.drop(removeRow)
                    bookshelf.to_csv('data/bookshelf.csv', index = False, sep=',')
                    text = self.messageBox(title = "Book Removed", message = "Your book has been removed." )
            except:
                text = self.messageBox(title = "Error", message = "You must have a csv named 'bookshelf.csv' in the data folder." )

    def get_random(self):
        try:
            bookshelf = pandas.read_csv('data/bookshelf.csv')
            index = bookshelf.index
            genre = self.genrechoosen.get()
            genreList = bookshelf['Genre'].to_list()
            if genre == "Choose a genre:":
                total_rows = len(index)
                random_choice = random.randint(0, total_rows - 1)
                shelfRec = "You should read " + bookshelf.iloc[random_choice, 0] \
                      + " by " + bookshelf.iloc[random_choice, 1] + "."
                text = self.messageBox(title = "Your Recommendation", message = shelfRec )
            elif any(bookGenre == genre for bookGenre in genreList):
                total_rows = len(index)
                random_choice = random.randint(0, total_rows - 1)
                genreMatch = False
                print(bookshelf.iloc[random_choice, 2])
                while genreMatch == False:
                    if bookshelf.iloc[random_choice, 2] == genre:
                        genreMatch = True
                    else:
                        random_choice = random.randint(0, total_rows - 1)
                shelfRec = "You should read " + bookshelf.iloc[random_choice, 0] \
                      + " by " + bookshelf.iloc[random_choice, 1] + "."
                text = self.messageBox(title = "Your Recommendation", message = shelfRec )
            else:
                text = self.messageBox(title = "Error", message = "There are no books of that genre on the shelf.")
        except:
                text = self.messageBox(title = "Error", message = "You must have a csv named 'bookshelf.csv' in the data folder." )

    def help(self):
        HELP_MESSAGE = """
Thank you for using my eShelf Program!

To add a book: Enter a title and author name into the input boxes and select the correct
genre from the drop down menu. A title is required. A pop-up will indicate if it was
successfully added, and the book will be added to the bottom of the csv document.

To remove a book: Enter a title into the input box. Author and genre aren't used for this
and don't need to be populated. A pop-up will indicate if the book was successfully removed.

To generate a random suggestion: All that is required is to press the button and a random
suggestion will be generated. You can also select a genre and if there are any books of that
genre on the shelf, one will be selected. If there are none of that genre, a pop-up will be
generated to inform the user.

"""
        text = self.messageBox(title = "Help", message = HELP_MESSAGE, width = 50, height = 25 )

def main():
    """Instantiate and pop up the window."""
    eShelf().mainloop()

if __name__ == "__main__":
    main()

