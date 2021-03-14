from Pachet import Pachet
from Jucator import Jucator
from Dealer import Dealer

def create():

    """This method creates a list of players based on the integer 'nr_total_jucatori' """

    jucator = []
    nr_jucatori = 0
    nr_total_jucatori = int(input('\nIntroduceti numarul jucatorilor:'))

    with open('ListaParticipanți.txt', mode='r') as f:
        for x in f.readlines():
            if nr_jucatori >= nr_total_jucatori:
                break
            x = x.split("\t")
            jucator.append(Jucator(x))
            print(f"{jucator[nr_jucatori].nume} just joined the room!    Have fun!")
            nr_jucatori+=1

    print()

    return jucator



def Joc(dealer, jucatori):

    """The game"""

    while True:

        P = Pachet()  # Creez pachetul

        print("The deck has been shuffled:", end=' ')
        #for x in P.pachet:
            #print(x.val, x.tip, end=';  ')
        print('\n')

        for player in jucatori:

            x = input(f"\n{player.nume}, Do you want to play? (Please type \'yes\' or \'no\'): ")
            if x != 'yes':
                print('Goodbye!')
                continue

            bet = input(f"{player.nume}, 'please bet a sum [0-{player.suma_totala}]: ")
            player.pariaza(bet)

            player.Primeste_2_carti(P)

            HitOrStand = input(f"{player.nume}, please, select an option (hit, stand): ")

            if HitOrStand == 'stand':
                player.calculeaza_scor()

            while HitOrStand == 'hit':
                player.hit(P)
                player.calculeaza_scor()

                if player.scor >= 21:
                    break

                HitOrStand = input(f"{player.nume}, please, select an option (hit, stand): ")

                if HitOrStand == 'stand':
                    player.calculeaza_scor()
                    break

        print()

        #Dealerul isi joaca mana

        scores = []

        for player in jucatori:
            if player.scor<22:
                scores += [player.scor]

        while dealer.scor < max(scores):
            if dealer.scor >= 17:
                break
            dealer.hit(P)
            dealer.calculeaza_scor()

        print('\n')

        #Urmeaza sa calculam rezultatele finale ale rundei

        for player in jucatori:

            if player.scor == 0:
                continue

            if dealer.scor < 22:

                if player.scor > dealer.scor:
                    if player.scor < 22:
                        player.suma_totala += player.suma_pariata
                        print(f"{player.nume}: You won! (score:{player.scor})     Now, you have {player.suma_totala}")
                    elif player.scor > 21:
                        player.suma_totala -= player.suma_pariata
                        print(f"{player.nume}: You lost!    (score:{player.scor})    Now, you have {player.suma_totala}")

                elif player.scor == dealer.scor:
                    print(f"{player.nume}: Draw!    (score:{player.scor})    Now, you have {player.suma_totala}")

                elif player.scor < dealer.scor:
                    player.suma_totala -= player.suma_pariata
                    print(f"{player.nume}: You lost!    (score:{player.scor})    Now, you have {player.suma_totala}")

            else:
                if player.scor < 22:
                    player.suma_totala += player.suma_pariata
                    print(f"{player.nume}: You won! (score:{player.scor}) Now, you have {player.suma_totala}")
                else:
                    print(f"{player.nume}: Draw!    (score:{player.scor})   Now, you have {player.suma_totala}")

        for player in jucatori:
            if int(player.suma_totala) == 0:
                jucatori.remove(player)


        NextRount = input("\nDo you want to play next round? (type \'no\' to stop)\n")
        if NextRount == 'no':
            print("Game over!")
            break

        for player in jucatori:
            player.hand = []
            player.scor = 0
            player.suma_pariata = 0


        dealer.hand = []
        dealer.scor = 0


        print('\n')
