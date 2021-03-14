import random
from typing import List
from Pachet import Pachet

class Jucator:

    """This class creates a blackjack player"""

    def __init__(self,x):
        self.nume = x[0] + ' ' + x[1]
        self.varsta = x[2]
        self.nationalitate = x[3]
        self.suma_totala = int(x[4])
        self.scor = 0
        self.hand = []
        self.suma_pariata = 0


    def Primeste_2_carti(self,pachet):

        """This method adds two cards to the player's hand"""

        new_card = pachet.trage()
        self.hand = self.hand + [new_card]
        new_card = pachet.trage()
        self.hand = self.hand + [new_card]

        print('Your hand:', end=' ')
        for card in self.hand:
            print(card.tip, end='; ')

        self.calculeaza_scor()


    def hit(self,pachet):

        """This method adds the drawn card to the player's hand"""

        new_card = pachet.trage()
        self.hand = self.hand + [new_card]
        print('You drew: ',new_card.tip, '  Your hand: ',end='')
        for card in self.hand:
            print(card.tip, end='; ')

    def pariaza(self, suma_pariata):

        """This method is used for betting"""

        suma_pariata = int(suma_pariata)
        if suma_pariata > self.suma_totala:
            self.suma_pariata = self.suma_totala
        else:
            self.suma_pariata = suma_pariata

        print('Your bet is: ',self.suma_pariata,' tokens!')

    def calculeaza_scor(self):

         """This method calculates player's score"""

         self.scor = 0

         for carte in self.hand:

             if carte.val>11:
                 carte.val = 10

             self.scor = self.scor + carte.val

         if self.scor>21:
             for carte in self.hand:
                 if carte.val == 11:
                    carte.val -= 10
                    self.scor -= 10
         print('Your score is: ',self.scor)





