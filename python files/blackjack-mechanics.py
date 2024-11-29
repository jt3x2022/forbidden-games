import random

def createdeck(x, y): #X is number fo decks, Y is number of cards ignoring suites, example for bj, x = 6, y = 13
    suites = ['a','b','c','d'] #in order a,b,c,d: diamond club heart spade
    deck = []
    for _ in range(x):
        for b in range(1, y+1):
            for c in range(4):
                b_str = str(b)
                deck.append(b_str + suites[c])
    return deck

deck = createdeck(1,13)         
random.shuffle(deck)
print(deck)