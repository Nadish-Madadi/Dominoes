class Stats:
  def stats(self,p_1,p_2,wins1,wins2,games_played,total_games,p1_deck,p2_deck):
    print("* * * * * Statistics Menu * * * * * * * * * * * * * * * * * *\n 1. Number of Wins per player\n 2. Total Games Played\n 3. Total Games Left\n 4. Final decks of each player from previous game\n 5. Names of each player\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    print("Enter 1 for wins, 2 for total games played, 3 for the games left, 4 for the previous deck of each player, 5 for the names of each player, and 6 to leave the menu")

    while True:
      choice = int(input("Enter choice: "))
      def read():
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          return x

      def write_o1(x,wins1,wins2):
        with open("stats.txt","w") as ww:
          x[0] = f"{p_1} wins: {wins1}\n"
          x[1] = f"{p_2} wins: {wins2}\n"
          ww.writelines(x)
      
      def write_o2(x,games_played):
        with open("stats.txt","w") as ww:
          x[2] = f"Games played: {games_played}\n"
          ww.writelines(x)
      
      def write_o3(x,total_games,games_played):
        with open("stats.txt","w") as ww:
          if total_games-wins1 < wins1:
            x[3] = "Games left: 0\n"
          elif total_games-wins2 < wins2:
            x[3] = "Games left: 0\n"
          else:
            x[3] = f"Games left: {total_games-games_played}\n"
          ww.writelines(x)

      def write_o4(x,p1_deck,p2_deck):
        with open("stats.txt","w") as ww:
          x[4] = f"{p_1} final deck for game {games_played}: {p1_deck}\n"
          x[5] = f"{p_2} final deck for game {games_played}: {p2_deck}\n"
          ww.writelines(x)

      def write_o5(x,p_1,p_2):
        with open("stats.txt","w") as ww:
          x[6] = f"Player 1 name: {p_1}\n"
          x[7] = f"Player 2 name: {p_2}\n"
          ww.writelines(x)

      if choice == 1:
        write_o1(read(),wins1,wins2)
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          print(x[0], end = "")
          print(x[1])
      elif choice == 2:
        write_o2(read(),games_played)
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          print(x[2])
      elif choice == 3:
        write_o3(read(),total_games,games_played)
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          print(x[3])
      elif choice == 4:
        write_o4(read(),p1_deck,p2_deck)
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          print(x[4], end = "")
          print(x[5])
      elif choice == 5:
        write_o5(read(),p_1,p_2)
        with open("stats.txt","r") as rr:
          x = rr.readlines()
          print(x[6], end = "")
          print(x[7])
      elif choice == 6:
        return ""
      else:
        print("Please enter a valid choice")