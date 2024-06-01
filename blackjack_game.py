import random
import os
#This is a loop that loops through the user list and generates a sum for this
def loop_for_user():
    """This function loops through the user list and generates a sum for this
    """
    sum = 0
    for i in range(len(user)):
                sum = sum + user[i]
    return sum
#This is loop that loops through the dealer list and generates a sum for this
def loop_for_dealer():
    """This function loops through the dealer list and generates a sum for this
    """
    sum = 0
    for i in range(len(dealer)):
        sum = sum + dealer[i]
    return sum
#This function print the value of both the dealer and the user list
def print_the_value():
    print(user)
    print(dealer)
def card_user():
    for item in user:
                if item in card_value:
                    card_value.remove(item)
def card_dealer():
    for item in dealer:
            if item in card_value:
                card_value.remove(item)
    
    
#This is a varable that stores the list of all the card values that the cards in a blackjack game has
card_value = [1,2,3,4,5,6,7,8,9,10,10,10,11]
#user is a predefined list that will be used in the further steps that will store the user cards
user = []
#dealer is a predefined list that will be used in the further steps that will store the dealer cards
dealer = []
#This variable stores the information of the input that ask the user whether they want to play the game of the blackjack
want_to_play = input("Do you want to play a game of blackjack: ").lower()
#if yes then we move to this step
if want_to_play == 'yes':
        #for the below loop the loop lasts for two steps and two different cards enter the list
        for i in range(2):
            x = user.append(random.choice(card_value))
            card_user()
        #one card is included in the list for the dealer
        dealer.append(random.choice(card_value))
        card_dealer()
        #Here both the lists are printed along with the cards
        print_the_value()
        #This loop plays the game where it continuously ask the player if they want to play, if they do 
        while True:
            want_to_continue = input("Do you want to continue: ").lower()
            if want_to_continue == 'yes':
                user.append(random.choice(card_value))
                #Here the function shows the list of the user and the dealer
                print_the_value()
                card_user()
            else:
                dealer.append(random.choice(card_value))
                #here three function each doing specific task where the first one print the existing list second one shows the sum of the user list
                #and the third one shows the sum of the third list
                print_the_value() 
                print(loop_for_user())
                print(loop_for_dealer())
                if loop_for_user()>loop_for_dealer() and loop_for_user()<=21 or loop_for_dealer()>21:
                    print("User Wins")
                elif loop_for_user()>21 and loop_for_dealer()>21:
                    print("Dealer wins by default")
                else:
                    print("Dealer Wins")
                break
            
