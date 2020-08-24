#TestData=[(Test Data 01),(Test Data 02)....]
#(Test Data 0n) = ([hand1],[hand2],'expected result')
#handn=[('suit','val'),('suit','val')...]

ref_deck=[('spades', '2'), ('spades', '3'), ('spades', '4'), ('spades', '5'), ('spades', '6'), ('spades', '7'), ('spades', '8'),
			('spades', '9'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen'), ('spades', 'king'), ('spades', 'ace'),
			('clubs', '2'), ('clubs', '3'), ('clubs', '4'), ('clubs', '5'), ('clubs', '6'), ('clubs', '7'), ('clubs', '8'),
			('clubs', '9'), ('clubs', '10'), ('clubs', 'jack'), ('clubs', 'queen'), ('clubs', 'king'), ('clubs', 'ace'),
			('hearts', '2'), ('hearts', '3'), ('hearts', '4'), ('hearts', '5'), ('hearts', '6'), ('hearts', '7'), ('hearts', '8'),
			('hearts', '9'), ('hearts', '10'), ('hearts', 'jack'), ('hearts', 'queen'), ('hearts', 'king'), ('hearts', 'ace'),
			('diamonds', '2'), ('diamonds', '3'), ('diamonds', '4'), ('diamonds', '5'), ('diamonds', '6'), ('diamonds', '7'),
			('diamonds', '8'), ('diamonds', '9'), ('diamonds', '10'), ('diamonds', 'jack'), ('diamonds', 'queen'), ('diamonds', 'king'),
			('diamonds', 'ace')]

vals = ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
suits = ['clubs','spades','hearts','diamonds']
# Royal Flush of Clubs
hand_royal_flush_1 = [('clubs','10'),('clubs','ace'),('clubs','jack'),('clubs','king'),('clubs','queen')]
# Royal Flush of Spades
hand_royal_flush_2 = [('spades','king'),('spades','queen'),('spades','10'),('spades','ace'),('spades','jack')]
# Royal Flush Hand of 3
hand_royal_flush_3 = [('hearts','king'),('hearts','queen'),('hearts','ace')]
# Royal Flush Hand of 3
hand_royal_flush_4 = [('clubs','king'),('clubs','queen'),('clubs','ace')]
# Royal Flush Hand of 2
hand_royal_flush_5 = [('spades','king'),('spades','ace')]
# Royal Flush Hand of 2
hand_royal_flush_6 = [('diamonds','king'),('diamonds','ace')]

# Straight Flush Highest
hand_straight_flush_1 = [('clubs','10'),('clubs','9'),('clubs','jack'),('clubs','king'),('clubs','queen')]
# Straight Flush Lowest
hand_straight_flush_2 = [('hearts','6'),('hearts','4'),('hearts','3'),('hearts','5'),('hearts','2')]
# Straight Flush Hand of 3
hand_straight_flush_3 = [('diamonds','7'),('diamonds','9'),('diamonds','8')]
# Straight Flush Hand of 3
hand_straight_flush_4 = [('clubs','2'),('clubs','4'),('clubs','3')]
# Straight Flush Hand of 2
hand_straight_flush_5 = [('spades','10'),('spades','9')]
# Straight Flush Hand of 2
hand_straight_flush_6 = [('hearts','4'),('hearts','3')]

#Four of a kind Highest Value
hand_four_of_a_kind_1=[('clubs','ace'),('hearts','ace'),('clubs','king'),('diamonds','ace'),('spades','ace')]
#Four of a kind Lowest Value
hand_four_of_a_kind_2=[('clubs','2'),('hearts','2'),('diamonds','king'),('spades','2'),('diamonds','2')]

#Full House of three of a kind with lowest value
hand_full_house_1=[('clubs','5'),('hearts','5'),('diamonds','5'),('spades','jack'),('diamonds','jack')]
#Full House of three of a kind with highest value
hand_full_house_2=[('clubs','10'),('hearts','6'),('spades','10'),('spades','6'),('diamonds','10')]

#Flush with hand of 5
hand_flush_1=[('clubs','10'),('clubs','ace'),('clubs','jack'),('clubs','king'),('clubs','2')]
#Flush with hand of 5
hand_flush_2=[('hearts','4'),('hearts','6'),('hearts','8'),('hearts','10'),('hearts','2')]
#Flush with hand of 3
hand_flush_3=[('hearts','king'),('hearts','queen'),('hearts','10')]
#Flush with hand of 3
hand_flush_4=[('spades','7'),('spades','3'),('spades','5')]
#Flush with hand of 2
hand_flush_5=[('spades','king'),('spades','6')]
#Flush with hand of 2
hand_flush_6=[('diamonds','4'),('diamonds','10')]

#Highest Straight Flush
hand_straight_1=[('clubs','6'),('hearts','2'),('diamonds','5'),('spades','3'),('diamonds','4')]
#Lowest Straight Flush
hand_straight_2 = [('clubs','10'),('clubs','ace'),('clubs','jack'),('clubs','king'),('hearts','queen')]
#Straight Flush with hand of three
hand_straight_3=[('clubs','10'),('hearts','jack'),('diamonds','9')]
#Straight Flush with hand of three
hand_straight_4=[('clubs','2'),('hearts','4'),('diamonds','3')]
#Straight Flush with hand of two
hand_straight_5=[('clubs','2'),('hearts','3')]
#Straight Flush with hand of two
hand_straight_6=[('clubs','queen'),('hearts','jack')]

#Three of a kind at middle of order when sorted with descending order
hand_three_of_a_kind_1 = [('clubs','jack'),('hearts','ace'),('diamonds','jack'),('spades','10'),('hearts','jack')]
#Three of a kind at top of order when sorted with descending order
hand_three_of_a_kind_2 = [('clubs','10'),('hearts','2'),('diamonds','2'),('spades','9'),('diamonds','2')]
#Three of a kind at bottom of order when sorted with descending order
hand_three_of_a_kind_3 = [('clubs','8'),('hearts','5'),('diamonds','8'),('spades','6'),('diamonds','8')]
#Three of a kind with hand of 3
hand_three_of_a_kind_4 = [('clubs','4'),('diamonds','4'),('spades','4')]
#Three of a kind with hand of 3
hand_three_of_a_kind_5 = [('clubs','ace'),('diamonds','ace'),('spades','ace')]

#Consecutive Two pair at top of order when sorted with descending order
hand_two_pair_1 = [('clubs','10'),('hearts','ace'),('diamonds','10'),('spades','ace'),('diamonds','5')]
#Consecutive Two pair at bottom of order when sorted with descending order
hand_two_pair_2 = [('clubs','8'),('hearts','5'),('diamonds','8'),('spades','ace'),('diamonds','5')]
#Consecutive Two pair, one at top of order and second and bottom of order when sorted with descending order
hand_two_pair_3 = [('clubs','jack'),('hearts','2'),('diamonds','jack'),('spades','5'),('diamonds','2')]

#One pair at middle of order when sorted with descending order
hand_one_pair_1 = [('clubs','10'),('hearts','ace'),('diamonds','10'),('spades','king'),('diamonds','5')]
#One pair at top of order when sorted with descending order
hand_one_pair_2 = [('clubs','ace'),('hearts','ace'),('diamonds','10'),('spades','king'),('diamonds','9')]
#One pair at bottom of order when sorted with descending order
hand_one_pair_3 = [('clubs','2'),('hearts','2'),('diamonds','10'),('spades','king'),('diamonds','9')]
#One pair with hand of 3 at bottom of order when sorted with descending order
hand_one_pair_4 = [('clubs','6'),('hearts','6'),('diamonds','10')]
#One pair with hand of 3 at top of order when sorted with descending order
hand_one_pair_5 = [('clubs','king'),('hearts','king'),('diamonds','10')]
#One pair with hand of 2
hand_one_pair_6 = [('clubs','4'),('hearts','4')]
#One pair with hand of 2
hand_one_pair_7 = [('clubs','6'),('hearts','6')]

#High card random cards hand of 5
hand_None_1 = [('clubs','jack'),('hearts','ace'),('diamonds','8'),('spades','10'),('diamonds','2')]
#High card just missed Straight Hand hand of 5
hand_None_2 = [('clubs','10'),('clubs','ace'),('clubs','jack'),('clubs','king'),('hearts','2')]
#High card just missed Straight Hand with hand of 3
hand_None_3 = [('clubs','4'),('clubs','3'),('diamonds','ace')]
#High card just missed Straight Hand with hand of 3
hand_None_4 = [('clubs','6'),('clubs','7'),('diamonds','9')]
#High card just missed Straight Hand with hand of 2
hand_None_5 = [('clubs','ace'),('hearts','2')]
#High card just missed Straight Hand with hand of 2
hand_None_6 = [('clubs','10'),('hearts','8')]