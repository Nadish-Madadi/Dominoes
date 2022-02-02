import os
from time import sleep
from setting_up import Setting
from deck import Deck
from gameboard import Game
from stats import Stats
class Main:
  if __name__ == "__main__":

    input("Welcome to a game of Dominoes! Only 2 players can play at a time. Once both players are ready please click the Enter key.\n")

    # get player names and number of games
    print("* * * * * Setting Up the Game * * * * * * * * * * * * * * * * * *\n  1. Player 1: please enter your name\n  2. Player 2: please enter your name\n  3. How many games do you want to play choose an odd number?\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

    print("Enter 1 for Player 1's name, 2 for Player 2's name, and 3 to for the number of games to play")
    name_count = 3
    options_complete = []
    x = Setting()
    while name_count > 0:
      name_choice = input("Enter number: ")
      if name_choice.isdigit() == True:
        name_choice = int(name_choice)
        if name_choice not in options_complete:
          if name_choice == 1:
            player_1 = x.name_check("1",1)
            name_count -= 1
            options_complete.append(1)
          elif name_choice == 2:
            player_2 = x.name_check("2",2)
            name_count -= 1
            options_complete.append(2)
          elif name_choice == 3:
            num_of_games = x.odd_num_check(0)
            name_count -= 1
            options_complete.append(3)
        else:
          print("Please enter a choice not previously selected")
      else:
        print("Please enter a valid choice")
        

    # transition to the game
    print(f"\nWelcome {player_1} and {player_2}!")
    sleep(1.5)
    print("Your game will begin shortly.")
    sleep(1.5)
    
    # clear the board and commence distribution of cards
    for i in range(3,0,-1):
      print(f"Clearing console in {i}...")
      sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)
    print("Console cleared. Ready to begin.")
    sleep(1.5)


    def second_part(player_1,player_2,games_played,num_of_games,wins1,wins2):
      # get player domino decks
      all_dominoes = ['12|12', '11|11', '12|11', '10|10', '11|10', '12|10', '9|9', '10|9', '11|9', '12|9', '8|8', '9|8', '10|8', '11|8', '12|8', '7|7', '8|7', '9|7', '10|7', '11|7', '12|7', '6|6', '7|6', '8|6', '9|6', '10|6', '11|6', '12|6', '5|5', '6|5', '7|5', '8|5', '9|5', '10|5', '11|5', '12|5', '4|4', '5|4', '6|4', '7|4', '8|4', '9|4', '10|4', '11|4', '12|4', '3|3', '4|3', '5|3', '6|3', '7|3', '8|3', '9|3', '10|3', '11|3', '12|3', '2|2', '3|2', '4|2', '5|2', '6|2', '7|2', '8|2', '9|2', '10|2', '11|2', '12|2', '1|1', '2|1', '3|1', '4|1', '5|1', '6|1', '7|1', '8|1', '9|1', '10|1', '11|1', '12|1', '0|0', '1|0', '2|0', '3|0', '4|0', '5|0', '6|0', '7|0', '8|0', '9|0', '10|0', '11|0', '12|0']
      y = Deck()

      print(f"* * * * * Game Board Menu * * * * * * *\n  1. {player_1} draw your dominos            \n  2. {player_2} draw your dominos            \n* * * * * * * * * * * * * * * * * * * *\n")
      print(f"Enter 1 for {player_1}'s deck or 2 for {player_2}'s deck")

      b_1, b_2 = False,False
      while b_1 == False or b_2 == False:
        choice = int(input("Enter number: "))
        
        if choice == 1:
          if b_1 == False:
            a = y.dist_dominoes_1(all_dominoes)
            player_1_deck = a[0]
            all_dominoes = a[1]
            sleep(1)
            print(f"{player_1}'s deck: {player_1_deck}")
            b_1 = True
          else:
            print(f"{player_1} already has their dominoes, please enter 2 for {player_2}")
        
        if choice == 2:
          if b_2 == False:
            b = y.dist_dominoes_2(all_dominoes)
            player_2_deck = b[0]
            all_dominoes = b[1]
            sleep(1)
            print(f"{player_2}'s deck: {player_2_deck}")
            b_2 = True
          else:
            print(f"{player_2} already has their dominoes, please enter 1 for {player_1}")
      
      p1_deck = player_1_deck
      p2_deck = player_2_deck

      player_1_sum_hdoubles = y.conv_deck(player_1_deck)
      player_2_sum_hdoubles = y.conv_deck(player_2_deck)

      g = Game()
      who_goes_first = g.det_who_goes_first(player_1,player_2,player_1_sum_hdoubles,player_2_sum_hdoubles,player_1_deck,player_2_deck)
      
      while True:
        game_proceed_check = input("Please type yes if both players are ready to begin: ")
        if game_proceed_check.lower() == "yes":
          print("Thank you for choosing to play and let's clear the board once more")
          sleep(1.5)
          for i in range(3,0,-1):
            print(f"Clearing console in {i}...")
            sleep(1)
          os.system('cls' if os.name == 'nt' else 'clear')
          
          break
        else:
          print("Please type yes when both players are ready")

      gameboard = []
      gameboard_ints = []
      print("* * * * * Playing the Game * * * * * * * * * * * * * * * * * *\n  1. place a domino on the game board\n  2. pick up one domino from the pile\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
      print("Enter 1 to place a domino on the board or 2 to pick up a domino from the pile")

      if who_goes_first == 1:
        counter = 0
        while True:
          if counter == 0:
            print(player_1_deck)
            print(player_1, end = "")
            print(f" please play a domino by entering the position of the domino you would like to play: ",end="")
            p = int(input())
            while True:
              if p not in range(0,len(player_1_deck)+1):
                print(f"Please enter a valid position {player_1}")
                p = int(input(f"Please enter a position from your deck {player_1}:"))
              else:
                break
            
            popped_val = player_1_deck.pop(p-1)
            gameboard.append(popped_val)
            a = popped_val.split("|")
            a = [int(i) for i in a]
            gameboard_ints.append(a[0])
            gameboard_ints.append(a[1])
            print(f"Gameboard: {gameboard}\n")
          else:
            e = g.place_1_init(player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,all_dominoes)
            if e == 1:
              wins1 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins1,e)
              
            elif e == 2:
              wins2 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins2,e)
            gameboard = e[0]
            player_1_deck = e[2]
            all_dominoes = e[5]
          counter += 1

          e = g.place_2_init(player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,all_dominoes)
          if e == 1:
              wins1 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins1,e)
              
          elif e == 2:
            wins2 += 1
            n = Stats()
            n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
            return (wins2,e)
          gameboard = e[0]
          player_2_deck = e[3]
          all_dominoes = e[5]
          counter += 1
          
      elif who_goes_first == 2:
        counter = 0
        while True:
          if counter == 0:
            print(player_2_deck)
            print(player_2, end = "")
            print(f" please play a domino by entering the position of the domino you would like to play: ",end="")
            p = int(input())
            while True:
              if p not in range(0,len(player_2_deck)+1):
                print(f"Enter a valid position {player_2}")
                p = int(input(f"Please enter a position from your deck {player_2}:"))
              else:
                break
            
            popped_val = player_2_deck.pop(p-1)
            gameboard.append(popped_val)
            a = popped_val.split("|")
            a = [int(i) for i in a]
            gameboard_ints.append(a[0])
            gameboard_ints.append(a[1])
            print(f"Gameboard: {gameboard}\n")
          else:
            e = g.place_2_init(player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,all_dominoes)
            if e == 1:
              wins1 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins1,e)
              
            elif e == 2:
              wins2 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins2,e)
            gameboard = e[0]
            player_2_deck = e[3]
            all_dominoes = e[5]
          counter += 1

          e = g.place_1_init(player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,all_dominoes)
          if e == 1:
              wins1 += 1
              n = Stats()
              n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
              return (wins1,e)
              
          elif e == 2:
            wins2 += 1
            n = Stats()
            n.stats(player_1,player_2,wins1,wins2,games_played,num_of_games,p1_deck,p2_deck)
            return (wins2,e)
          gameboard = e[0]
          player_1_deck = e[2]
          all_dominoes = e[5]
          counter += 1

    wins1 = 0
    wins2 = 0
    
      
    for i in range(num_of_games):
      if num_of_games-wins1 < wins1:
        print(f"{player_1} is the winner of the best of {num_of_games}")
      elif num_of_games-wins2 < wins2:
        print(f"{player_2} is the winner of the best of {num_of_games}")
      else:
        print(f"Game #{i+1}")
        games_played = i + 1
        games_won = second_part(player_1,player_2,games_played,num_of_games,wins1,wins2)
        if games_won[1] == 1:
          wins1 = games_won[0]
        elif games_won[1] == 2:
          wins2 = games_won[0]