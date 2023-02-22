# WELCOME SCREEN
print("====================================")
print("Python Game of War")
print("====================================")
user_entered = str(input("Type PLAY and press ENTER: "))
print("\n")

# -------------- GAME SCREEN -Play The Game- Draw two cards-----------------------------
# Import Python’s random module to generate random data
import random
# initializing the variables
counter = 0
number_of_cards_won_by_player_one = 0;
number_of_cards_won_by_player_two = 0;

while(user_entered == 'PLAY'): #If yes-Type PLAY, begin the game.
  for counter in range(20): #for loop to iterate 20 times/rounds
    
    # player_one = int(input("Your card: ")) -> If player 1 needs to input use this code, or go for random generation
    # Player one (P1 or you) draws a random number, player two (computer) draws a random number from 0-9.
    player_one = random.randint(0, 9); # random integer from 0 to 9 
    player_two = random.randint(0, 9); # random integer from 0 to 9
    print("Your card: "+ str(player_one) , "Opponent's card: "+ str(player_two)) #Display the card drawn for each player.

    # Determine which number is higher and award the two cards to the player with the highest card during that round.
    if (player_one > player_two): # compare
      print("You won this round!") # display who won the round
      number_of_cards_won_by_player_one += 2 #increment by two each time/award the two cards to the player
    elif (player_one== player_two):
      print("Tie!")
    else:
      print("Player2 won this round!")
      number_of_cards_won_by_player_two += 2 #increment by two each time
      
    input("Please ENTER to continue")
    print("\n")
    counter += 1 #increment by one each time/go to the next round
  break

# DETERMINE WINNER OF THE GAME

total_cards_player1 = number_of_cards_won_by_player_one; #storing the total cards of player1
total_cards_player2 = number_of_cards_won_by_player_two; #storing the total cards of player2

# Below two lines of code commented, as it is not needed to display, but it gives the total no: of cards gained by the players 
# print("PLAYER ONE TOTAL CARDS: " + str(total_cards_player1)); 
# print("PLAYER TWO TOTAL CARDS: " + str(total_cards_player2)); 

# Conditional checking to determine the winner and display it
if (total_cards_player1 < total_cards_player2):
  print("You lost! Play again?")
elif(total_cards_player1 != 0 and total_cards_player1 == total_cards_player2): 
  print("Tie! Play again?")
elif(total_cards_player1 == 0 and total_cards_player2 == 0): 
  print("Start again")
else:  
  print("You won! Play again?")


  
  
