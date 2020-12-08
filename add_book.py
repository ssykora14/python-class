"""

Module to add book to file. Use with "add book" button.

"""

import csv  
    
def add_book():
    title = input("Enter a title: ")
    author = input("Enter a author: ")
    genre = input("Enter a genre: ")
    
    # field names
    book = {
        "Title": title,
        "Author": author,
        "Genre": genre
        }

    # writing to csv file
    with open("data/bookshelf.csv", 'a+', newline='') as bookshelf:
        # creating a csv writer object
        addbook = csv.writer(bookshelf)
        addbook.writerow(book.values())
