import random
suits=['S','H','C','D']
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getValue(self):
        return values[self.rank]

    def __str__(self):
        rankstr=self.rank
        suitstr=self.suit
        if self.rank == 'J':
            rankstr='Jack'
        elif self.rank =='Q':
            rankstr='Queen'
        elif self.rank =='K':
            rankstr='King'
        elif self.rank =='A':
            rankstr='Ace'
        if self.suit == 'S':
            suitstr='Spades'
        elif self.suit == 'H':
            suitstr='Hearts'
        elif self.suit == 'C':
            suitstr='Clubs'
        elif self.suit == 'D':
            suitstr='Diamonds'
        return "{x} of {y}".format(x=rankstr,y=suitstr)

class Deck():

    def __init__(self):
        self.cards=[]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def __str__(self):
        for card in self.cards:
            print(card)
        return ''

    def __len__(self):
        return len(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand():

    def __init__(self,playername):
        self.mycards=[]
        self.playername = playername

    def __str__(self):
        for card in self.mycards:
            print card
        return ''

    def __len__(self):
        return len(self.mycards)

    def add_card(self,card):
        self.mycards.append(card)

def playcards(hand1, hand2, warcards=[]):
    card1=hand1.mycards.pop()
    card2=hand2.mycards.pop()

    print("{a}: {b}".format(a=player1name, b=card1))
    print("{c}: {d}".format(c=player2name, d=card2))

    print('')

    if card1.getValue() == card2.getValue():
        print('WAR!!!')
        print('')
        war(hand1, hand2, card1, card2)
    elif card1.getValue() > card2.getValue():
        print("{a} wins!".format(a=player1name))
        hand1.mycards.insert(0,card1)
        hand1.mycards.insert(0,card2)
        for card in warcards:
            hand1.mycards.insert(0,card)
    else:
        print("{b} wins!".format(b=player2name))
        hand2.mycards.insert(0,card1)
        hand2.mycards.insert(0,card2)
        for card in warcards:
            hand2.mycards.insert(0,card)

def war(hand1, hand2, card1, card2):
    warcards1=[card1]
    warcards2=[card2]
    i=3
    while i>0:
        warcards1.append(hand1.mycards.pop())
        warcards2.append(hand2.mycards.pop())
        i=i-1
    print("Player 1 Cards:")
    for card in warcards1:
        print(card)
    print('')
    print("Player 2 Cards:")
    for card in warcards2:
        print(card)
    print('')
    playcards(hand1, hand2, warcards1 + warcards2)


#START GAME

maindeck=Deck()

player1name=raw_input('Player One, enter your name')
if player1name == '':
    player1name='Player 1'
hand1=Hand(player1name)

player2name=raw_input('Player Two, enter your name')
if player2name == '':
    player2name = 'Player 2'
hand2=Hand(player2name)

print('')

while len(maindeck)>0:
    hand1.add_card(maindeck.deal_card())
    hand2.add_card(maindeck.deal_card())

while len(hand1)>0 and len(hand2)>0:
    print("Time for another round")
    print(player1name+" has "+str(len(hand1.mycards)))
    print(player2name+" has "+str(len(hand2.mycards)))
    print('')
    playcards(hand1, hand2)

    print('')

    keepplaying=raw_input('Type Q to Quit.  Otherwise, press Enter to Continue  ').upper()
    if keepplaying == 'Q':
        break
    print('')

# print(hand1)
# print(len(hand1))
# print(hand2)
# print(len(hand2))
# print(hand2.mycards.pop())
