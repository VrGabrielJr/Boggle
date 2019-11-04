import random

class Boggle:
  board = ["_"] * 16
  let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  def start(self):
    print("Welcome to Text-Base Boggle!")
    self.printBoard()

  def printBoard(self):
    for i in range(0, len(self.board), 4):
      print(' '.join(self.board[i:i+4]))
  
  # def shake(self):
  #   for i in range(0,len(self.board)):
  #     for j in range(0,len(self.board[i])):
  #       num = random.randint(0,25)
  #       self.board[i][j] = self.let[num]
  #       print(self.board[i][j], end=" ")
  #     print()
  #   print("\n")
  #   self.printBoard()

game = Boggle()
game.start()
