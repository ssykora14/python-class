"""

Author: Sally S.
Date: 11/1/20
Program Name: GUI Election
Description: A GUI program that reads a text file of votes, tallies
the votes, displays the total votes of each candidate, and displays
the winner.

"""

from breezypythongui import EasyFrame

class GuiElection(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, "Election Results")
        
        # Create and add widgets to the window
        self.addLabel(text = "Biden",
                      row = 0, column = 0)
        self.totalBiden = self.addIntegerField(value = 0,
                                               row = 0,
                                               column = 1,
                                               width = 10)
        self.addLabel(text = "Sykora",
                      row = 1, column = 0)
        self.totalSykora = self.addIntegerField(value = 0,
                                               row = 1,
                                               column = 1,
                                               width = 10)
        self.addLabel(text = "Trump",
                      row = 2, column = 0)
        self.totalTrump = self.addIntegerField(value = 0,
                                               row = 2,
                                               column = 1,
                                               width = 10)

        # Create and add buttons to the window
        self.addButton(text = "See Results", row = 3, column = 0,
                       command = self.getResults)

        self.voteWinner = self.addTextField(text = "Who won?",
                                               row = 4,
                                               column = 1,
                                               width = 10)

    def getResults(self):
        with open("votes.txt") as rawVotes:
            listVotes = rawVotes.read().splitlines()
        totalBiden = listVotes.count("Biden")
        totalSykora = listVotes.count("Sykora")
        totalTrump = listVotes.count("Trump")
        self.totalBiden.setNumber(totalBiden)
        self.totalSykora.setNumber(totalSykora)
        self.totalTrump.setNumber(totalTrump)
        if (totalBiden >= totalSykora) and (totalBiden >= totalTrump):
            if (totalBiden == totalTrump) and (totalBiden == totalSykora):
                winner = "All tied."
            elif (totalBiden == totalTrump):
                winner = "Biden and Trump tied."
            elif (totalBiden == totalSykora):
                winner = "Biden and Sykora tied."
            else:
                winner = "Biden won."
        elif (totalSykora >= totalTrump):
            if (totalSykora == totalTrump):
                winner = "Sykora and Trump tied."
            else:
                winner = "Sykora won."
        else:
            winner = "Trump won."
        self.voteWinner.setText(winner) 

def main():
    """Instantiate and pop up the window."""
    GuiElection().mainloop()

if __name__ == "__main__":
    main()
