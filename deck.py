import random

class Deck:
  
  def dist_dominoes_1(self,dominoes):
    
    player_1_deck_ = []
    while len(player_1_deck_) < 7:
      player_1_deck_.append(dominoes.pop(random.randint(1,len(dominoes)-1)))
    return (player_1_deck_,dominoes)
  
  def dist_dominoes_2(self,dominoes):
    
    player_2_deck_ = []
    while len(player_2_deck_) < 7:
      player_2_deck_.append(dominoes.pop(random.randint(1,len(dominoes)-1)))
    return (player_2_deck_,dominoes)
  
  # get sum of highest double in each player's deck
  def conv_deck(self,deck):

    p_d = [i.split("|") for i in deck]
    p_d_c = []

    for i in range(len(p_d)):
      p_d[i][0], p_d[i][1] = int(p_d[i][0]), int(p_d[i][1])
    
    for i in range(len(p_d)):
      if p_d[i][0] == p_d[i][1]:
        p_d_c.append(p_d[i])

    p_d_c_ = [sum(i) for i in p_d_c]

    if len(p_d_c_) == 0:
      return 0
    return max(p_d_c_)
  
  def sum_deck(self,deck_):
    p_d = [i.split("|") for i in deck_]
    

    for i in range(len(p_d)):
      p_d[i][0], p_d[i][1] = int(p_d[i][0]), int(p_d[i][1])
    
    p_d = [sum(i) for i in range(len(p_d))]
    
    return max(p_d)

# quick deck to test with and will give exactly 13 in the gameboard such that first pickup cannot be played
# player_1_deck_ = ["1|1","2|2","3|3","4|4","5|5","6|6","7|7"]
# player_2_deck_ = ["1|1","1|2","2|3","3|4","4|5","5|6","6|7"]