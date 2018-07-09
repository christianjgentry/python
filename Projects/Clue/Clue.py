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
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    player5 = []
    player6 = []
    
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
                player.append(player_cards.pop())
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
    print(player)

print("Whodunnit?", whodunnit)
