from deck import Deck

class Win:
  def domino_over(self, player_1_deck, player_2_deck, player_1, player_2):
    if len(player_1_deck) < len(player_2_deck):
      print(f"\n{player_1} has won! They have the least number of dominos")
      return 1
    elif len(player_2_deck) < len(player_1_deck):
      print(f"\n{player_2} has won! They have the least number of dominos")
      return 2
    else:
      s = Deck()
      t = s.sum_deck(player_1_deck)
      t_ = s.sum_deck(player_2_deck)
      if t > t_:
        print(f"\n{player_1} has won! All dominos within the pile are used up and the highest sum of domino was taken from each deck. The highest won")
        return 1
      else:
        print(f"\n{player_2} has won! All dominos within the pile are used up and the highest sum of domino was taken from each deck. The highest won")
        return 2
  
  def deck_over(self, player):
    return f"\n{player} has won! No more dominoes in their deck"