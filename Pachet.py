import random
from Carte import Carte

class Pachet:

    """This class creates a deck of cards"""

    def __init__(self):
        self.pachet = self.construieste()

        self.amesteca()


    def construieste(self):

        """This method creates a deck"""

        pachet = []
        for i in range(2,10):
            pachet.append( Carte(i,str(i)) )

        pachet.append( Carte(11, 'Ace') )
        pachet.append( Carte(12, 'J') )
        pachet.append( Carte(13, 'Q') )
        pachet.append( Carte(14, 'K') )

        pachet *= 4

        return pachet

    def amesteca(self):

        """This method shuffles the deck"""

        random.shuffle(self.pachet)

    def trage(self):

        """This method draws the last card from the dack"""

        return self.pachet.pop()
