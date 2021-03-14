from Pachet import Pachet
from Jucator import Jucator

class Dealer:

    def __init__(self):
        self.scor = 0
        self.hand = []


    def hit(self, pachet):
        """This method adds the drawn card to the player's hand"""

        new_card = pachet.trage()
        self.hand = self.hand + [new_card]
        print('The dealer drew: ', new_card.tip, '  Dealer\'s hand: ', end='')
        for card in self.hand:
            print(card.tip, end='; ')


    def calculeaza_scor(self):

         """This method calculates player's score"""

         self.scor = int(0)

         for carte in self.hand:

             if carte.val>11:
                 carte.val = 10

             self.scor += int(carte.val)

         if self.scor > 21:
             for carte in self.hand:
                 if carte.val == 11:
                    carte.val -= 10
                    self.scor -= 10
         print(f"The dealer's score is: {self.scor}")