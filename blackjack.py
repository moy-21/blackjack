import random
from tracemalloc import start

suits= ['Clubs \u2663','Hearts \u2665','Diamonds \u2666','Spades \u2660']
ranks = ['Queen','Jack','King','Ace','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two']
values = {
    'Ten': 10,
    'Nine': 9,
    'Eight': 8,
    'Seven': 7,
    'Six': 6,
    'Five': 5,
    'Four': 4,
    'Three': 3,
    'Two': 2,
    'Queen': 10,
    'King': 10,
    'Jack': 10,
    'Ace': 11
    }


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        

    def __repr__(self):
        return self.rank + ' of ' + self.suit
    


class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __repr__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        return 'The deck is:' + deck_str

    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card1 = self.deck.pop()
        return card1
        
    

class Dealer:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        self.deck1 = Deck()
    
    def show_dealer_hand(self):
        print(f'{self.hand[0]}, X')

    def add_card(self,card):
        self.hand.append(card)
        self.value += values[card.rank]

    def get_value(self):
        for card in self.hand:
            if card.rank == 'Ace':
                self.aces += 1
            self.value += values[card.rank]
        while (self.value > 21) and self.aces:
            self.value -= 10
            self.aces -= 1
        return self.value


    def stay(self):
        print('Lets compare the hands')
        print(self.hand)
        return self.value

    def bust(self):
        print("Dealer busted!")
        return self.value

    def black_jack_(self):
        if self.value == 21:
            return 'Black Jack! Sorry you lost'

    def win(self):
        print("You lost Dealer Wins")
        return self.value


class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        self.deck2 = Deck()

    def show_player_hand(self):
        print(self.hand)

    def add_card(self,card):
        self.hand.append(card)
        self.value += values[card.rank]

    def get_value(self):
        for card in self.hand:
            if card.rank == 'Ace':
                self.aces += 1
            self.value += values[card.rank]
        while (self.value > 21) and self.aces:
            self.value -= 10
            self.aces -= 1
        return self.value

    def stay(self):
        print("I stand")
        return self.value

    def black_jack_(self):
        if self.value == 21:
            return 'Black Jack! You win'
        
    def bust(self):
        print("Ooops you busted better luck next time")
        return self.value

    def win(self):
        print("You win!!!!")
        return self.value
        
        

class Game(Player,Dealer):
    def __init__(self):
        pass
        
    def play_game(self):
        playing = True
        while playing:
            while True:
                print("Welcome to Black Jack\n")
                print("----The Rules of the game are---\n--There are two players you and the dealer--\n--The dealer deals you and himself two playong cards from shuffled deck--\n--He shows only one of his card--\n--The objective to to get closest to 21 as possible without going over--")
                print("--After cards are dealt you have the choice to hit or stand--\n--Hit as many times as youll like without busting--\n--Dealer only hits if hes under 17--\n--Blackjack is only acheived from getting 21 from initial deal--\n--If both tied its considered a push and there is no loser or winner-- ")
                print("--Have fun--\n")
                response1 = input("Enter 's' to play the game!\n")

                if response1.lower() == 's':
                    break
                else:
                    print('Sorry wrong input try again')
            dealing = True
            while dealing:
                deck = Deck()
                deck.shuffle_deck()
                
            
                player = Player()
                player.hand.append(deck.deal())
                player.hand.append(deck.deal())
                player.get_value()

                dealer  = Dealer()
                dealer.hand.append(deck.deal())
                dealer.hand.append(deck.deal())
                dealer.get_value()

                print("Your Hand")
                player.show_player_hand()
                print(player.value)
                print("\n")

                print('Dealer Hand')
                dealer.show_dealer_hand()
                print("\n")
                
                
                if player.value ==21:
                    print("You win")
                    end = True
                hit = True
                while hit:
                    
                    x = input("Hit or Stay: ")
                    
                    if x.lower() == 'hit':
                        player.add_card(deck.deal())
                        print(player.value)
                        print(player.hand)
                        print("\n")
                        
                        if player.value > 21:
                            player.bust()
                            hit = False
                            dealing = False

                    elif x.lower() == 'stay':
                        player.stay()
                        print("\n")
                        hit = False


                if player.value <= 21:
                        while dealer.value < 17:
                            print("\n")
                            dealer.add_card(deck.deal())
                            dealer.show_dealer_hand()

                        print(f'The dealer hand is {dealer.hand}')
                        print(dealer.value)

                if dealer.value > 21:
                    print("\n")
                    dealer.bust()
                    break
                                                
                elif dealer.value > player.value:
                    print("\n")
                    dealer.win()
                    break

                elif dealer.value < player.value:
                    player.win()
                    print("\n")
                    break
                                            
                else:
                    print("Its a tie!")
                    break
            
            end = True
            while end:
                again = input("Would you like to play again? (y/n): ")
                if again.lower() == 'y':
                    end = False
                    playing = True
                else:
                    exit()
        

                
                

                
                    

        
run = Game()
run.play_game()
                        
                               

                    
                    


                        


                    




                    





        
    
                


