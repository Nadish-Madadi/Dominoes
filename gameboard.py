import random
from time import sleep
from win_check import Win
class Game:
  def det_who_goes_first(self,player_1,player_2,player_1_sum_hdoubles,player_2_sum_hdoubles,player_1_deck,player_2_deck):
    
    
    if "12|12" in player_1_deck or player_1_sum_hdoubles > player_2_sum_hdoubles:
      print(f"{player_1} goes first")
      return 1

    
    elif "12|12" in player_2_deck or player_2_sum_hdoubles > player_1_sum_hdoubles:
      print(f"{player_2} goes first")
      return 2

    else:
      print("\nNo player has a double; therefore, whoever has the higher first number of their first domino will go first or if this number is the same, the second number of the first domino will be compared in the same way\n")
      print(f"For example if {player_1} has 12|2 and {player_2} has 9|3, {player_1} goes first because 12 > 9\n")

      sleep(2)
      p1_1, p2_1 = player_1_deck[0].split("|"), player_2_deck[0].split("|")
      if int(p1_1[0]) > int(p2_1[0]): 
        print(f"{player_1} goes first")
        return 1
      elif int(p1_1[0]) == int(p2_1[0]):
        if int(p1_1[1]) > int(p2_1[1]): 
          print(f"{player_1} goes first")
          return 1
        if int(p1_1[1]) < int(p2_1[1]): 
          print(f"{player_2} goes first")
          return 2
      else: 
        print(f"Based on your actual decks, {player_2} will go first")
        return 2
    
  def place_1_init(self,player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,dominoes):

    if len(dominoes) == 0:
      r = Win()
      return r.domino_over(player_1_deck, player_2_deck, player_1, player_2)
       
    print("Enter 1 to play a domino")
    print("Enter 2 to pick up a domino")
    print(f"Gameboard: {gameboard}")
    print(f"{player_1}'s deck: {player_1_deck}")
    g_1 = 0
    while True:
      choice = int(input("Enter number: "))
      if choice == 1:
        check_func = self.check_if_possible(player_1_deck,gameboard,gameboard_ints)
        if len(check_func) != 0:
          g_1 = int(input(f"What piece would you like to place {player_1} (enter position of domino): "))
          
          if g_1 not in range(1,len(player_1_deck)+1):
            print("Please enter a position within the range of your deck")
          else:
            player_1_split_deck = player_1_deck[g_1-1].split("|")
                
            player_1_split_deck[0], player_1_split_deck[1] = int(player_1_split_deck[0]), int(player_1_split_deck[1])
          
            if len(gameboard) == 0:
              popped = player_1_deck.pop(g_1 - 1)
              gameboard.append(popped)
              gameboard_ints.append(int(player_1_split_deck[0]))
              gameboard_ints.append(int(player_1_split_deck[1]))
              break

            elif player_1_split_deck[0] == gameboard_ints[0]:
              player_1_split_deck = [str(i) for i in player_1_split_deck]
              popped = player_1_deck.pop(g_1 - 1)
              player_1_split_deck.reverse()
              c = "|".join(player_1_split_deck)
              gameboard.insert(0,c)
              gameboard_ints.insert(0,int(player_1_split_deck[1]))
              gameboard_ints.insert(0,int(player_1_split_deck[0]))
              break
            
            elif player_1_split_deck[-1] == gameboard_ints[-1]:
              player_1_split_deck = [str(i) for i in player_1_split_deck]
              popped = player_1_deck.pop(g_1 - 1)
              player_1_split_deck.reverse()
              c = "|".join(player_1_split_deck)
              gameboard.append(c)
              gameboard_ints.append(int(player_1_split_deck[0]))
              gameboard_ints.append(int(player_1_split_deck[1]))
              break

            elif player_1_split_deck[0] == gameboard_ints[-1]:
              popped = player_1_deck.pop(g_1 - 1)
              gameboard.append(popped)
              gameboard_ints.append(int(player_1_split_deck[0]))
              gameboard_ints.append(int(player_1_split_deck[1]))
              break

            elif player_1_split_deck[-1] == gameboard_ints[0]:
              popped = player_1_deck.pop(g_1 - 1)
              gameboard.insert(0,popped)
              gameboard_ints.insert(0,int(player_1_split_deck[1]))
              gameboard_ints.insert(0,int(player_1_split_deck[0]))
              break 
            else:
              print("That domino cannot be played. Please try with another domino in your deck")
        else:
          print("No domino can be played, please pickup from the domino pile")
      elif choice == 2:
        check_func = self.check_if_possible(player_1_deck,gameboard,gameboard_ints)
        if len(check_func) > 0:
          print(f"{len(check_func)} dominos from your deck can be played: {check_func}")
        else:
          popped_el = dominoes.pop(random.randint(1,len(dominoes)-1))
          player_1_deck.append(popped_el)
          print(f"{player_1} has picked up {popped_el}")
          check_func_ = self.check_if_possible(popped_el,gameboard,gameboard_ints)
          if len(check_func_) == 0:
            break
          else:
            print(f"{popped_el} can be played, please choose option 1 and play that domino, you cannot proceed until it is played")
            print(f"Gameboard: {gameboard}")
            print(f"{player_1}'s deck: {player_1_deck}")
      else:
        print("Please re-enter a valid number (1 or 2)")
    if len(player_1_deck) == 0 and len(gameboard) >= 13:
      r = Win()
      print(r.deck_over(player_1))
      return 1
    

    print(f"\nIt's now your turn {player_2}!")

    return (gameboard,g_1,player_1_deck,player_2_deck,gameboard_ints,dominoes)
    
  def place_2_init(self,player_1,player_1_deck,player_2,player_2_deck,gameboard,gameboard_ints,dominoes):
    if len(dominoes) == 0:
      r = Win()
      print(r.domino_over(player_2_deck, player_2_deck, player_1, player_2))
      return 0

    print("Enter 1 to play a domino")
    print("Enter 2 to pick up a domino")
    print(f"Gameboard: {gameboard}")
    print(f"{player_2}'s deck: {player_2_deck}")
    g_2 = 0
    while True:
      choice = int(input("Enter number: "))
      if choice == 1:
        check_func = self.check_if_possible(player_2_deck,gameboard,gameboard_ints)
        if len(check_func) != 0:
          g_2 = int(input(f"What piece would you like to place {player_2} (enter position of domino): "))
          if g_2 not in range(1,len(player_2_deck)+1):
            print("Please enter a position within the range of your deck")
          else:
            player_2_split_deck = player_2_deck[g_2-1].split("|")
                
            player_2_split_deck[0], player_2_split_deck[1] = int(player_2_split_deck[0]), int(player_2_split_deck[1])
          
            if len(gameboard) == 0:
              popped = player_2_deck.pop(g_2 - 1)
              gameboard.append(popped)
              gameboard_ints.append(int(player_2_split_deck[0]))
              gameboard_ints.append(int(player_2_split_deck[1]))
              break

            elif player_2_split_deck[0] == gameboard_ints[0]:
              player_2_split_deck = [str(i) for i in player_2_split_deck]
              popped = player_2_deck.pop(g_2 - 1)
              player_2_split_deck.reverse()
              c = "|".join(player_2_split_deck)
              gameboard.insert(0,c)
              gameboard_ints.insert(0,int(player_2_split_deck[1]))
              gameboard_ints.insert(0,int(player_2_split_deck[0]))
              break
            
            elif player_2_split_deck[-1] == gameboard_ints[-1]:
              player_2_split_deck = [str(i) for i in player_2_split_deck]
              popped = player_2_deck.pop(g_2 - 1)
              player_2_split_deck.reverse()
              c = "|".join(player_2_split_deck)
              gameboard.append(c)
              gameboard_ints.append(int(player_2_split_deck[0]))
              gameboard_ints.append(int(player_2_split_deck[1]))
              break

            elif player_2_split_deck[0] == gameboard_ints[-1]:
              popped = player_2_deck.pop(g_2 - 1)
              gameboard.append(popped)
              gameboard_ints.append(int(player_2_split_deck[0]))
              gameboard_ints.append(int(player_2_split_deck[1]))
              break

            elif player_2_split_deck[-1] == gameboard_ints[0]:
              popped = player_2_deck.pop(g_2 - 1)
              gameboard.insert(0,popped)
              gameboard_ints.insert(0,int(player_2_split_deck[1]))
              gameboard_ints.insert(0,int(player_2_split_deck[0]))
              break
            else:
              print("That domino cannot be played. Please try with another domino in your deck")
        else:
          print("No domino can be played, please pickup from the domino pile")
      elif choice == 2:
        check_func = self.check_if_possible(player_2_deck,gameboard,gameboard_ints)
        if len(check_func) > 0:
          print(f"{len(check_func)} dominos from your deck can be played: {check_func}")
        else:
          popped_el = dominoes.pop(random.randint(1,len(dominoes)-1))
          player_2_deck.append(popped_el)
          print(f"{player_2} has picked up {popped_el}")
          check_func_ = self.check_if_possible(popped_el,gameboard,gameboard_ints)
          if len(check_func_) == 0:
            break
          else:
            print(f"{popped_el} can be played, please choose option 1 and play that domino, you cannot proceed until it is played")
            print(f"Gameboard: {gameboard}")
            print(f"{player_2}'s deck: {player_2_deck}")
      else:
        print("Please re-enter a valid number (1 or 2)")
    if len(player_2_deck) == 0 and len(gameboard) >= 13:
      r = Win()
      print(r.deck_over(player_2))
      return 2
    
    print(f"\nIt's now your turn {player_1}!")
    

    return (gameboard,g_2,player_1_deck,player_2_deck,gameboard_ints,dominoes)

  def check_if_possible(self,player_deck,gameboard,gameboard_ints):
    x = {}
    param_len = 0
    if isinstance(player_deck, str):
      param_len = 1
    else:
      param_len = len(player_deck)
    for i in range(param_len):
      if param_len == 1:
        if isinstance(player_deck,list):
          player_split_deck = player_deck[i].split("|")
        else:
          player_split_deck = player_deck.split("|")
      else:
        player_split_deck = player_deck[i].split("|")
      player_split_deck = [int(i) for i in player_split_deck]
      
      if player_split_deck[0] == gameboard_ints[0] or player_split_deck[-1] == gameboard_ints[-1] or player_split_deck[0] == gameboard_ints[-1] or player_split_deck[-1] == gameboard_ints[0]:
        if param_len == 1:
          x[i+1] = f"{player_split_deck[0]}|{player_split_deck[-1]}"
        else:
          x[i+1] = (player_deck[i])
    return x