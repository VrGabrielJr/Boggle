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
  
  def shake(self):
    for i in range(0, len(self.board)):
      num = random.randint(0,25)
      self.board[i] = self.let[num]
    
    print('\n')
    print("B O G G L E - B O A R D")
    print("------------------------")
    self.printBoard()

game = Boggle()
game.start()
game.shake()
