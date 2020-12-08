"""

Module to generate a randomm book from file. Genre to be added later.
Use with "Give Me a Recommendation" button.

"""

import pandas
import random

def get_random():
    bookshelf = pandas.read_csv('data/bookshelf.csv')
    index = bookshelf.index
    total_rows = len(index)
    random_choice = random.randint(0, total_rows - 1)

    print("You should read " + bookshelf.iloc[random_choice, 0] \
          + " by " + bookshelf.iloc[random_choice, 1] )
