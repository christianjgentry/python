################################################################################
#Modules
################################################################################
import random

################################################################################
#Variables
################################################################################

#create a list for each element in the game. suspect, weapon, and room
suspects = ["green", "peacock", "mustard", "scarlett", "plum", "orchid"]
weapons = ["dagger", "wrench", "revolver", "rope", "candlestick"]
rooms = ["library", "kitchen", "study", "hall", "ballroom", "billiard room",
        "dining room"]


################################################################################
#Classes
################################################################################
class Player():
	#Creates a base framework for a game character.
	def __init__(self, name):
		#Character is initialized with base attributes.
		self.name = name
		self.hand = []


################################################################################
#Definitions
################################################################################
def random_pull(my_list):
    #pull a random card from a card list and remove it from initial list.
    whodunnit_card = my_list[random.randint(0,len(my_list)-1)]
    my_list.remove(whodunnit_card)
    
    return whodunnit_card


def get_whodunnit():
    #Create the whodunnit list, the person place and thing that committed the crime.
    random_suspect = random_pull(suspects)
    random_weapon = random_pull(weapons)
    random_room = random_pull(rooms)
    
    whodunnit = [random_suspect, random_weapon, random_room]

    return whodunnit
    

def how_many_players():
    #Determine how many people are playing
    
    #create players and add them to a list of players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")
    player4 = Player("Player 4")
    player5 = Player("Player 5")
    player6 = Player("Player 6")
    
    player_flag = False
    while player_flag == False:
        
        try:
            number_of_players = int(input("How many people will be playing?\n" +
                                    "2, 3, 4, 5, 6: "))
        except:
            print("Enter an integer value between 2 and 6!\n")
            number_of_players = 0
        
        if number_of_players == 2:
            players = [player1, player2]
            player_flag = True
        elif number_of_players == 3:
            players = [player1, player2, player3]
            player_flag = True
        elif number_of_players == 4:
            players = [player1, player2, player3, player4]
            player_flag = True
        elif number_of_players == 5:
            players = [player1, player2, player3, player4, player5]
            player_flag = True
        elif number_of_players == 6:
            players = [player1, player2, player3, player4, player5, player6]
            player_flag = True
        else:
            print("2-6 players are required to play!\n")
    
    return players
    

def create_player_cardpool():
    #combine the remaining cards and then shuffle them into a new list.
    player_cardpool = []

    for i in suspects:
        player_cardpool.append(i)
        
    for i in weapons:
        player_cardpool.append(i)

    for i in rooms:
        player_cardpool.append(i)

    random.shuffle(player_cardpool)
    
    return player_cardpool
    

def deal_cards(player_cards):
    #divide the cardpool amongst the players until the cardpool is empty.
    count_to = len(player_cards)
    count = 0

    while True:
        for player in players:
            if count < count_to:
                player.hand.append(player_cards.pop())
                count += 1
            else:
                break
        
        if count == count_to:
            break
            
            
################################################################################
#Execute
################################################################################ 

players = how_many_players()
whodunnit = get_whodunnit()
player_cards = create_player_cardpool()

deal_cards(player_cards)

for player in players:
    print(player.name, "has joined the game!")

print("Whodunnit?", whodunnit)
print(players[0].name + "'s hand:", players[0].hand)
print(players[1].name + "'s hand:", players[1].hand)
print(players[2].name + "'s hand:", players[2].hand)
print(players[3].name + "'s hand:", players[3].hand)
print(players[4].name + "'s hand:", players[4].hand)
print(players[5].name + "'s hand:", players[5].hand, "\n\n")


game_won = False
game_quit = False
while game_won == False:
    for player in players:
        turn_flag = False
        while turn_flag == False:
            print(player.name + "'s turn!")
            print("Cards in hand:", player.hand, "\n")
            print("What would", player.name, "like to do?\n" 
                + "move to room/make accusation/declare whodunnit/pass\n")
            turn_choice = input(":")
            print("\n")
            
            if turn_choice == "move to room":
                print("Moving to room\n")
                turn_flag = True
            elif turn_choice == "make accusation":
                print("Making accusation\n")
                turn_flag = True
            elif turn_choice == "declare wdunnit":
                print("Declaring whodunnit\n")
                turn_flag = True
            elif turn_choice == "pass":
                print("Passing turn\n")
                turn_flag = True
            elif turn_choice == "quit":
                game_quit = True
                break
            else:
                print("Not a valid entry!!!\n")  
                
            if game_quit == True:
                break
        
        if game_quit == True:
            print("Game has been quit :(")
            game_won = True
            break
            
            
        
        
        
        
        
        
