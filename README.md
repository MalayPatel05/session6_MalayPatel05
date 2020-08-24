
# Session 6 - First Class Functions Part I

This assignment project is written in Python, and tested with pytest. It includes following files.
-session6.py      : This is the assignment code
-test_session6.py : This is pytest unit test. It tests completeness of assignment

>This assignment checks understanding of following concepts:
- High level functions map and zip
- List Expansion

>Assignement Problem Statement:
- **Problem Statement 1:** Create Deck of 52 cards using single line expression. Make use of lambda, zip and map function.
- **Problem Statement 2:** Write a function to create deck of 52 cards. Do not use of lambda, zip and map function.
- **Problem Statement 3:** Write a function to find out winner in a 2 player poker game. In each game, each player can have set of either 3,4 or 5 cards. For each game only one deck of cards is used.   

*Poker Hands Ranking*    
    1. *Royal Flush:*A, K, Q, J, 10, all the same suit. *In the event of a tie:* Split the pot  
    2. *Straight Flush:*Five cards in a sequence, all in the same suit. *In the event of a tie:* Highest rank at the top of the sequence wins.     
    3. *Four of a kind:*All four cards of the same rank. *In the event of a tie:* Highest four of a kind wins.    
    4. *Full house:*Three of a kind with a pair. *In the event of a tie:* Highest three matching cards wins the pot.   
    5. *Flush:*Any five cards of the same suit, but not in a sequence. *In the event of a tie:* The player holding the highest ranked card wins. If necessary, the second-highest, third-highest, fourth-highest, and fifth-highest cards can be used to break the tie.  
    6. *Straight:*Five cards in a sequence, but not of the same suit. *In the event of a tie:* Highest ranking card at the top of the sequence wins.  
    7. *Three of a kind:*Three cards of the same rank. *In the event of a tie:* Highest ranking three of a kind wins.  
    8. *Two pair:*Two different pairs. *In the event of a tie: *Highest pair wins. If players have the same highest pair, highest second pair wins. If both players have two identical pairs, highest side card wins.  
    9. *Pair:*Two cards of the same rank.  *In the event of a tie:* Highest pair wins. If players have the same pair, the highest side card wins, and if necessary, the second-highest and third-highest side card can be used to break the tie.
    10. *High Card:*When you haven't made any of the hands above, the player with highest card wins. *In the event of a tie:* Split the pot  

>Solution for Problem Statement 1:  
A deck of 52 cards is collection of all possible outcome of selecting pair of objects from two sets:  
    set 1. - set of suits = {spades,club,hearts,diamonds}  
    set 2. - set of card face = {ace,king,queen,jack,10,9,8,7,6,5,4,3,2}

This is a permutation selection. The following is the procedure to identify all possible outcome of this permutaiont:  
- Step 1: Select an object from set of suits.  
- Step 2: Create permutations of selected object with objects set of card face.  
- Step 3: Repeat Step 1 and Step 2 till all objects of suits are exhausted.

Code Design for Problem Statement 1:  
To achieve this using single statement expression:
Design 1: Use list comprehension with nested for loop
Design 2: If we create   
 - Step 1: 



> Description of Functions/Class

### Map


### Zip
This function calculates powers in given range for given positive number. 

### polygon_area
This function calculates area of polygon with sides >3 and 6.

### temp_converter
This function converts temperature scale between Farenheit and Celcius.

### speed_converter
This function converts speed in kmph to combination of dist in km/m/ft/yrd and time in be ms/s/m/hr/day
