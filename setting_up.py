class Setting:

  #check if names contain only letters
  def name_check(self,name,play_num):
    counter = 0
    while True:
      if name.isalpha() == True:
        return name
      else:
        if counter > 0:
          print("Please enter a name containing only letters:")
        name = input(f"Player {play_num}: please enter your name - ")
        counter += 1

  #check if number of games is odd
  def odd_num_check(self,num_games):
    while True:
      num_games = input("How many games do you want to play, choose an odd number? ")
      if num_games.isdigit() == False:
        print("Please enter an odd number:")
      elif int(num_games)%2 != 1:
        print("Please enter an odd number:")
      else:
        return int(num_games)