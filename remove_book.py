"""

Module to remove a book from file. Use with "remove book" button.
This will require title to avoid removing books based on author or
genre.

"""

import pandas

def remove_book():
    bookshelf = pandas.read_csv('data/bookshelf.csv')
    removedBook = input("Enter the title to be removed: ")
    removeRow = bookshelf[bookshelf['Title']==removedBook].index.values
    bookshelf = bookshelf.drop(removeRow)
    bookshelf.to_csv('data/bookshelf.csv', index = False, sep=',')
