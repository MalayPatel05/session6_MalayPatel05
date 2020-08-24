# -*- coding: utf-8 -*-
#set sacecardval has face value of each card, this is used to sort cards
facecardval={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':11,'queen':12,'king':13,'ace':14}
# list of face values, used to create deck
vals = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
#list of suits, used to create deck
suits = ['spades','clubs','hearts','diamonds']
#ranking of hands, used to indentify winner
handval={'royal_flush':10,'straight_flush':9,'four_of_a_kind':8,'full_house':7,'flush':6,'straight':5,
            'three_of_a_kind':4,'two_pair':3,'one_pair':2,'high_card':1}
#hand of royal flush, used to check royal flush
hand_royal_flush=['ace','king','queen','jack','10']

def permutation_classic(set1:'list of suits',
                        set2:'list of facevals')->'Deck of cards as list':
    '''This function returns collection of all possible outcome of selecting pair of objects from two sets.
    This function uses nested for loop'''
    _permutaions=[]
    for _objset1 in set1:
        for _objset2 in set2:
            _permutaions.append((_objset1,_objset2))
    return _permutaions

def permutation_listcmpr(set1:'list of suits',
                        set2:'list of facevals')->'Deck of cards as list':
    '''This function returns collection of all possible outcome of selecting pair of objects from two sets.
    This function uses nested for loop in list comprehension'''
    return[(_objset1,_objset2) for _objset1 in set1 for _objset2 in set2]

permutation_lambda_listcmpr = lambda set1,set2:[(_objset1,_objset2) for _objset1 in set1 for _objset2 in set2]
#This function returns collection of all possible outcome of selecting pair of objects from two sets.
#This function uses nested for loop in list comprehension in a lambda function'''

def check_same_suit(hand:'cards of player sorted in desceding order by facevals')->'returns True if cards are of same suit':
    '''Check if cards are of same suits
    Iputs:
        list of cards of a player
    Returns:
        True if all cards are same suit'''
    prev_suit = hand[0][0]   
    for facecard in hand:
        if prev_suit != facecard[0]:
            return False
        else:
            prev_suit = facecard[0]
    return True

def check_royal_flush(hand_sorted:'cards of player sorted in desceding order by facevals')->'returns True if cards are royal flush':
    '''This function returns True if cards are royal flush
    Iputs:
        cards of player sorted in desceding order by facevals
    Returns:
        True if cards are royalflush'''
    counter_harofl=0
    for facecard in hand_sorted:
        if facecard[1]!=hand_royal_flush[counter_harofl]:
            return False            
        else:
            prev_suit = facecard[0]
            counter_harofl=counter_harofl+1
    return True

def check_straight(hand_sorted:'cards of player sorted in desceding order by facevals')->'returns True if cards are straight':
    '''This function returns True if sorted hand is straight
    Iputs:
        cards of player sorted in desceding order by facevals
    Returns:
        True if cards are straight'''
    prev_facecardval = facecardval[hand_sorted[0][1]]
    for flush_counter in range(1,len(hand_sorted)):
        curr_facecardval=facecardval[hand_sorted[flush_counter][1]]
        if (prev_facecardval-curr_facecardval)!=1:
            return False
        else:
            prev_facecardval=curr_facecardval
    return True

def check_four_of_a_kind(hand_sorted:'cards of player sorted in desceding order by facevals')->'returns True if cards are four of a kind':
    '''This function returns True if sorted hand is four of a kind
    Iputs:
        cards of player sorted in desceding order by facevals
    Returns:
        True if cards are four of a kind'''
    prev_facecardval = facecardval[hand_sorted[0][1]]
    four_of_a_kind_streak=1
    for four_of_a_kind_counter in range(1,5):            
        curr_facecardval=facecardval[hand_sorted[four_of_a_kind_counter][1]]            
        if prev_facecardval!=curr_facecardval:
            if four_of_a_kind_counter>1 and four_of_a_kind_streak!=4:
                return False
        else:
            four_of_a_kind_streak=four_of_a_kind_streak+1                
        prev_facecardval=curr_facecardval
    return True

def count_number_of_a_kind(hand_sorted:'cards of player sorted in desceding order by facevals')->'returns number of pairs in cards':
    '''This function returns number of pairs in card
    Iputs:
        cards of player sorted in desceding order by facevals
    Returns:
        number of pairs in card'''
    n_of_a_kind_1=0
    n_of_a_kind_2=0
    n_of_a_kind_streak=1
    prev_facecardval = facecardval[hand_sorted[0][1]]
    for n_of_a_kind_counter in range(1,len(hand_sorted)):
        curr_facecardval=facecardval[hand_sorted[n_of_a_kind_counter][1]]        
        if prev_facecardval==curr_facecardval:
            n_of_a_kind_streak = n_of_a_kind_streak+1 
        if prev_facecardval!=curr_facecardval or n_of_a_kind_counter==(len(hand_sorted)-1):
            if n_of_a_kind_1<=1:
                n_of_a_kind_1 = n_of_a_kind_streak
            else:
                n_of_a_kind_2 = n_of_a_kind_streak
            n_of_a_kind_streak=1
        prev_facecardval=curr_facecardval
    return (n_of_a_kind_1,n_of_a_kind_2)

def check_hand(hand:'cards of player')->'returns the highest rank of plays card ie royal fulsh,straight flush etc':
    '''This function returns number of pairs in card
    Iputs:
        cards of a player
    Returns:
        the highest rank of plays card ie royal fulsh,straight flush etc'''
    hand_sorted = sorted(hand,key=lambda k:facecardval[k[1]],reverse=True)
    if check_same_suit(hand):
        # Check if royal flush
        if check_royal_flush(hand_sorted):
            return 'royal_flush' 
        #Check if Straight Flush
        elif check_straight(hand_sorted) == True:
            return 'straight_flush'
    #Check Four of a Kind
    if len(hand)==5:
        if check_four_of_a_kind(hand_sorted):
            return 'four_of_a_kind'
    #Count number of pairs
    n_of_a_kind_1,n_of_a_kind_2=count_number_of_a_kind(hand_sorted)
    #Check Full House
    if (n_of_a_kind_1 == 3 and n_of_a_kind_2 == 2) or ((n_of_a_kind_1 == 2 and n_of_a_kind_2 == 3)):
        return 'full_house'
    #Check Flush
    if check_same_suit(hand):
        return 'flush'
    #Check Straight
    if check_straight(hand_sorted) == True: 
        return 'straight'
    if (n_of_a_kind_1 == 3 or n_of_a_kind_2 == 3):
        return 'three_of_a_kind'
    if (n_of_a_kind_1 == 2 and n_of_a_kind_2 == 2):
        return 'two_pair'
    if (n_of_a_kind_1 == 2):
        return 'one_pair'
    else:
        return 'high_card'

def get_winner(hand1:'cards of player 1',hand2:'cards of player 1')->'player with winning cards':
    '''This function compares cards of two player and retruns winning player
        Iputs:
            cards of a player 1,cards of a player 2
        Returns:
            Player1 if player 1 has winnig cards,Player2 if player 2 has winnig cards, Tie if both have same rank cards'''

    if len(hand1)!=len(hand2):
        raise ValueError(f'Player1 has {len(hand1)} and Player2 has {len(hand2)}')
    p1_rank_hand=check_hand(hand1)
    p2_rank_hand=check_hand(hand2)
    if handval[p1_rank_hand]==handval[p2_rank_hand]:
        return 'Tie'
    elif handval[p1_rank_hand]>handval[p2_rank_hand]:
        return 'Player1'
    else:
        return 'Player2'