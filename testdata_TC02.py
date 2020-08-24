#TestData=[(Test Data 01),(Test Data 02)....]
#(Test Data 0n) = ([hand],'expected result,testid')
#hand=[('suit','val'),('suit','val')...]
from testdata_hands import *
import pytest
TestData =[pytest.param(hand_royal_flush_1,'royal_flush',id='TC02_01_royal_flush'),#Hand of 5
            pytest.param(hand_royal_flush_2,'royal_flush',id='TC02_02_royal_flush'),#Hand of 5
            pytest.param(hand_royal_flush_3,'royal_flush',id='TC02_03_royal_flush'),#Hand of 3
            pytest.param(hand_royal_flush_5,'royal_flush',id='TC02_04_royal_flush'),#Hand of 2
            pytest.param(hand_straight_flush_1,'straight_flush',id='TC02_05_straight_flush'),# Straight Flush Highest Hand of 5
            pytest.param(hand_straight_flush_2,'straight_flush',id='TC02_06_straight_flush'),# Straight Flush Lowest Hand of 5
            pytest.param(hand_straight_flush_3,'straight_flush',id='TC02_07_straight_flush'),# Straight Flush hand of 3
            pytest.param(hand_straight_flush_5,'straight_flush',id='TC02_08_straight_flush'),# Straight Flush hand of 2
            pytest.param(hand_four_of_a_kind_1,'four_of_a_kind',id='TC02_09_four_of_a_kind'),#Four of a kind Highest Value
            pytest.param(hand_four_of_a_kind_2,'four_of_a_kind',id='TC02_10_four_of_a_kind'),#Four of a kind Lowest Value
            pytest.param(hand_full_house_1,'full_house',id='TC02_11_full_house'),#Full House of three of a kind with lowest value
            pytest.param(hand_full_house_2,'full_house',id='TC02_12_full_house'),#Full House of three of a kind with highest value
            pytest.param(hand_flush_1,'flush',id='TC02_13_flush'),#Flush with hand of 5
            pytest.param(hand_flush_3,'flush',id='TC02_14_flush'),#Flush with hand of 3
            pytest.param(hand_flush_5,'flush',id='TC02_15_flush'),#Flush with hand of 2
            pytest.param(hand_straight_1,'straight',id='TC02_16_straight'),#Highest Straight Flush hand of 5
            pytest.param(hand_straight_2,'straight',id='TC02_17_straight'),#Lowest Straight Flush hand of 5
            pytest.param(hand_straight_3,'straight',id='TC02_18_straight'),#Highest Straight Flush hand of 3
            pytest.param(hand_straight_5,'straight',id='TC02_19_straight'),#Highest Straight Flush hand of 2
            pytest.param(hand_three_of_a_kind_1,'three_of_a_kind',id='TC02_20_three_of_a_kind'),#Three of a kind at middle of order when sorted with descending order hand of 5
            pytest.param(hand_three_of_a_kind_2,'three_of_a_kind',id='TC02_21_three_of_a_kind'),#Three of a kind at top of order when sorted with descending order hand of 5
            pytest.param(hand_three_of_a_kind_3,'three_of_a_kind',id='TC02_22_three_of_a_kind'),#Three of a kind at bottom of order when sorted with descending order
            pytest.param(hand_three_of_a_kind_4,'three_of_a_kind',id='TC02_23_three_of_a_kind'),#Three of a kind with hand of 3
            pytest.param(hand_two_pair_1,'two_pair',id='TC02_24_two_pair'),#Consecutive Two pair at top of order when sorted with descending order
            pytest.param(hand_two_pair_2,'two_pair',id='TC02_25_two_pair'),#Consecutive Two pair at bottom of order when sorted with descending order
            pytest.param(hand_two_pair_3,'two_pair',id='TC02_26_two_pair'),#Consecutive Two pair, one at top of order and second and bottom of order when sorted with descending order
            pytest.param(hand_one_pair_1,'one_pair',id='TC02_27_one_pair'),#One pair at middle of order when sorted with descending order hand of 5
            pytest.param(hand_one_pair_2,'one_pair',id='TC02_28_one_pair'),#One pair at top of order when sorted with descending order hand of 5
            pytest.param(hand_one_pair_3,'one_pair',id='TC02_29_one_pair'),#One pair at bottom of order when sorted with descending order hand of 5
            pytest.param(hand_one_pair_4,'one_pair',id='TC02_30_one_pair'),#One pair with hand of 3 at bottom of order when sorted with descending order
            pytest.param(hand_one_pair_5,'one_pair',id='TC02_31_one_pair'),#One pair with hand of 3 at top of order when sorted with descending order
            pytest.param(hand_one_pair_6,'one_pair',id='TC02_32_one_pair'),#One pair with hand of 2
            pytest.param(hand_None_1,'high_card',id='TC02_33_one_pair'),#High card random cards hand of 5
            pytest.param(hand_None_2,'high_card',id='TC02_34_one_pair'),#High card just missed Straight Hand hand of 5
            pytest.param(hand_None_3,'high_card',id='TC02_35_one_pair'),#High card just missed Straight Hand with hand of 3
            pytest.param(hand_None_5,'high_card',id='TC02_36_one_pair'),#High card just missed Straight Hand with hand of 2
            ]