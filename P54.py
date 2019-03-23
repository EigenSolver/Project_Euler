def map_value(char):
    poker_vals = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    return poker_vals[char]


def get_value(hand):
    '''
    get the values of the given hand
    >>> get_value(['8C', 'TS', 'KC', '9H', '4S'])
    ('8', 'T', 'K', '9', '4')
    '''
    return tuple(map(lambda x: x[0], hand))


def get_suit(hand):
    '''
    >>> get_suit(['8C', 'TS', 'KC', '9H', '4S'])
    ('C', 'S', 'C', 'H', 'S')
    '''
    return tuple(map(lambda x: x[1], hand))


def royal_flush(hand):
    '''
    >>> royal_flush(['TC','JC','QC','KC','AC'])
    True
    >>> royal_flush(['TC','JC','QC','KC','9C'])
    False
    >>> royal_flush(['TD','JC','QC','KC','AC'])
    False
    '''
    if straight_flush(hand) and high_card(hand)[0] == 'A':
        return True
    else:
        return False


def straight_flush(hand):
    '''
    >>> straight_flush(['TC','JC','QC','KC','AC'])
    True
    >>> royal_flush(['8C','JC','QC','KC','AC'])
    False
    '''
    if straight(hand) and flush(hand):
        return True
    else:
        return False


def four_of_a_kind(hand):
    '''
    >>> four_of_a_kind(['KC', 'TC', 'KD', 'KS', 'KH'])
    True
    >>> four_of_a_kind(['KC', 'KC', '4D', 'KS', '6H'])
    False
    '''
    vals = get_value(hand)
    for val in vals:
        if vals.count(val) == 4:
            return True
    return False


def full_house(hand):
    '''
    >>> full_house(['3C', '3D', '3S', '9S', '9D'])
    True
    >>> full_house(['2C', '3D', '3S', '9S', '9D'])
    False
    '''
    if three_of_a_kind(hand) and get_pairs(hand) == 1:
        return True
    else:
        return False


def flush(hand):
    '''
    >>> flush(['2C', '3C', '4D', '5S', '6H'])
    False
    >>> flush(['2C', '3C', '4C', '5C', '6C'])
    True
    '''
    suit = get_suit(hand)
    if suit.count(suit[0]) == 5:
        return True
    else:
        return False


def straight(hand):
    '''
    >>> straight(['2C', '3C', '4D', '5S', '6H'])
    True
    >>> straight(['2C', '3C', '4D', 'KS', '6H'])
    False
    '''
    vals = list(map(map_value, get_value(hand)))
    vals.sort()
    flag = True
    for i in range(1, 5):
        if vals[i]-vals[i-1] != 1:
            flag = False
    return flag


def three_of_a_kind(hand):
    '''
    >>> three_of_a_kind(['2C', '3C', '4D', 'KS', '6H'])
    False
    >>> three_of_a_kind(['KC', 'KC', '4D', 'KS', '6H'])
    True
    '''
    vals = get_value(hand)
    for val in vals:
        if vals.count(val) == 3:
            return True
    return False


def get_pairs(hand):
    '''
    >>> get_pairs(['2C', '3C', '4D', 'KS', '6H'])
    0
    >>> get_pairs(['2C', '4C', '4D', 'KS', 'KH'])
    2
    '''
    n_pairs = 0
    vals = list(get_value(hand))
    for val in vals:
        if vals.count(val) == 2:
            vals.remove(val)
            n_pairs += 1
    return n_pairs


def high_card(hand):
    '''
    return the highest char of the given
    >>> high_card(['8C', 'TS', 'KC', '9H', '4S'])
    'KC'
    '''
    return max(hand, key=lambda x:map_value(x[0]))

def judge(config):
    '''
    >>> judge(['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD'])
    0
    >>> judge(['4D', '6S', '9H', 'QH', 'QC','3D', '6D', '7H', 'QD', 'QS'])
    1
    >>> judge(['5D', '8C', '9S', 'JS', 'AC','2C', '5C', '7D', '8S', 'QH'])
    1
    '''
    def compare_high(hand1,hand2):
        '''
        >>> compare_high(['4D', '6S', '9H', 'QH', 'QC'],['3D', '6D', '7H', 'QD', 'QS'])
        1
        >>> compare_high(['5D', '8C', '9S', 'JS', 'AC'],['2C', '5C', '7D', '8S', 'QH'])
        1
        '''
        card1=high_card(hand1)
        card2=high_card(hand2)
        h1=map_value(card1[0])
        h2=map_value(card2[0])
        if h1>h2:
            return 1
        elif h1<h2:
            return 0
        else:
            hand1.remove(card1)
            hand2.remove(card2)
            return compare_high(hand1,hand2)
    
    def compare_multiple(hand1,hand2,n):
        def get_counted_val(hand,n):
            '''
            >>> get_counted_val(('K','T','T','1'),2)
            'T'
            '''
            for i in hand:
                if hand.count(i)==n:
                    return i
        f=lambda x: map_value(get_counted_val(get_value(x),n))
        s=f(hand1)-f(hand2)
        if s>0:
            return 1
        elif s<0:
            return 0
        else:
            return compare_high(hand1,hand2)


    combo_rank = ('royal_flush','straight_flush','four_of_a_kind','full_house','flush','straight','three_of_a_kind')
    hand1 = config[:5]
    hand2 = config[5:] 
    for combo in combo_rank:
        p1=eval(combo+'(hand1)')
        p2=eval(combo+'(hand2)')
        if p1 and p2:
            if combo=='four_of_a_kind':
                return compare_multiple(hand1,hand2,4)
            elif combo=='full_house' or combo=='three_of_a_kind':
                return compare_multiple(hand1,hand2,3)
            else:
                return compare_high(hand1,hand2)
        elif p1 and not p2:
            return 1
        elif not p1 and p2:
            return 0
        else:
            continue

    p1= get_pairs(hand1)
    p2=get_pairs(hand2)
    if p1>p2:
        return 1
    elif p1<p2:
        return 0
    elif p1+p2>0:
        return compare_multiple(hand1,hand2,2)
    else:
        return compare_high(hand1,hand2)


def main():
    '''
    load text from file and judge every match
    '''
    result = 0

    with open('p054_poker.txt', 'r') as f:
        matchs = f.readlines()
    for hand in matchs:
        result += judge(hand.strip().split(" "))
    print('Player 1 wins: {}'.format(result))

main()