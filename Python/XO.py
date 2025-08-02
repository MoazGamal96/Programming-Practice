import os


def clear_screen():
   os.system("cls")



class Player :
   def __init__(self):
      self.name = ""
      self.symbol = ""
   def choose_name (self):
      while True:
        name = input("Enter You'r Name : ")
        if name.isalpha():
           self.name = name
           break
        print("Invaled name. Pleas use letters only.")

   def choose_symbol(self):
      while True:
         symbol = input(f"{self.name}, choose Your symbol(a single letter): ")
         if symbol.isalpha() and len(symbol) == 1:
            self.symbol = symbol.upper()
            break
         print("Invalid symbol. Pleas choose a single letter.")
         
class Menue :
   
   def display_main_menu(self):
      menue_text = """ Welcome To X-O!
      1-Start Game.
      2-Quite Game.
      input("Input Your Choice (1 or 2):
      """
      choice = input (menue_text)
      return choice
   
      
   def display_endgame_menu(self):
      menue_text = """
      Game Over!!
      1-Restart Game
      2-Quite Game
      input("Input Your Choice (1 or 2): 
      1"""
      choice = input (menue_text)
      return choice
   # def validate_choice(menue_text):       
   #        while True:
   #          try:
   #           choice = int(input("Input Your Choice (1 or 2):"))
   #           break
   #          except :
   #              if choice == [1,2]:
   #                  return choice
   #              else :
   #                  print("invalid choise!!")
          

class Board:
   def __init__(self):
      self.board = [str(i) for i in range(1,10)]

   def dispalay_board(self):
      for i in range (0, 9 , 3):
         print("|".join(self.board[i:i+3]))
         if i<6 :
            print('_'*5)
   def update_board(self, choice, symbol):
      if self.is_valid_move(choice):
         self.board[choice-1] = symbol
         return True
      return False



   def is_valid_move(self, choice):
      return self.board[choice-1].isdigit()
      
   def reset_board(self):
      self.board = [str(i) for i in range(1,10)]
           

class Game:
   def __init__(self):
      self.players =[Player(),Player()]
      self.board = Board()
      self.menue = Menue()
      self.current_player_index = 0
   
   
   def start_game (self) :
      choice = self.menue.display_main_menu()
      if choice == "1" :
         self.setup_players()
         self.play_game()
      else :
         self.quit_game()
   
   
   def setup_players(self):

      for pnumber,player in enumerate(self.players,start=1) :
         print(f"Player{pnumber}, Enter your details: ")
         player.choose_name()
         player.choose_symbol()
         print("_"*40)

   
   def play_game(self):
      while True:
         self.play_turn()
         if self.chick_win() or self.chick_draw():
            choice = self.menue.display_endgame_menu()
            if choice ==1:
               self.restart_game
            else :
               self.quit_game 
               break 
   
   
   def restart_game(self):
      self.board.reset_board()
      self.current_player_index = 0
      self.play_game()
   
   
   def chick_win(self):
      win_compinations = [
         [0,1,2], [3,4,5],[6,7,8], #rows
         [0,3,6],[1,4,7],[2,5,8],  #colmns
         [0,4,8],[2,4,6]           #diagonals
      ]
      for compo in win_compinations:
         if (self.board.board[compo[0]]) == self.board.board[compo[1]] ==self.board.board[compo[2]]:
         #chick if the count cells in the lists are equall to each other (x,x,x) or (o,o,o)  
           return True
      return False
   


   def chick_draw(self):
    return all (not cell.isdigit() for cell in self.board.board)#True if there is not any numbers in cells 
   
   
   def play_turn(self):
      player =self.players[self.current_player_index]
      self.board.dispalay_board()
      print(f"{player.name}'s turn ({player.symbol})")
      while True:
       try:
            cell_choice = int(input("chose a cell (1-9): "))
            if 1<= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
               break
            else:
               print("Invalid Move, Try Again: ")
       except ValueError:
            print("Pleas Enter a Number between (1-9): ")
      
      self.switch_player()
   
   
   def switch_player (self):
      self.current_player_index = 1 - self.current_player_index
   
   
   def  quit_game(self):
      print("Thank You For Playing")
game = Game()
game.start_game()