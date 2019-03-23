def map_value(char):
    poker_vals=["2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14]
    return poker_vals[char]

def royal_flush(hand):
    pass
def straight_flush(hand):
    pass

def four_of_a_kind(hand):
    pass

def full_house(hand):
    pass

def flush(hand):
    suit=get_suit(hand)
    if suit.count(suit[0])==5:
        return True
    else:
        return False

def straight(hand):
    vals=list(map(map_value,get_value(hand)))
    vals.sort()
    flag=True
    for i in range(1,5):
        if vals[i]-vals[i-1]!=1:
            flag=False
    return flag

def three_of_a_kind(hand):
    vals=get_value(hand):
    for val in vals: 
        if vals.count(val)==3:
            return True
    return False



def get_pairs(hand):
    n_pairs=0
    pairs=[]
    vals=get_value(hand):
    for val in vals: 
        if vals.count(val)==2:
            n_pairs+=1
            pairs.append(val)
    if n_pairs:
        return (n_pairs,pairs)
    else:
        return n_pairs

def remove_card(char):


def high_card(hand):
    '''
    return the highest char of the given
    >>> high_card(['8C', 'TS', 'KC', '9H', '4S'])
    'K'
    '''
    return max(get_value(hand),key=map_value)

def get_value(hand):
    '''
    get the values of the given hand
    >>> get_value(['8C', 'TS', 'KC', '9H', '4S'])
    ('8','T','K','9','4')
    '''
    return tuple(map(lambda x: x[0],hand))

def get_suit(hand):
    '''
    >>> get_value(['8C', 'TS', 'KC', '9H', '4S'])
    ('C','S','C','H','S')
    '''
    return tuple(map(lambda x: x[1],hand))

def judge(hand):
    player1=hand[:5]
    player2=hand[5:]


def main():
    '''
    load text from file and judge every match
    '''
    result=0

    with open('p054_poker.txt','r') as f:
        matchs=f.readlines()
    for hand in matchs:
        result+=judge(hand.strip().split(" "))
    print('Player 1 wins: {}'.format(result))

main()