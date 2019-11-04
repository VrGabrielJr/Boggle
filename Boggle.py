import random

class Boggle:
  board = [["-","-","-","-","-","-"]] * 6
  let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  def start(self):
    print("Welcome to Text-Base Boggle!")
    self.printBoard()

  def printBoard(self):
    for i in range(0,len(self.board)):
      for j in range(0, len(self.board[i])):
        print(self.board[i][j], end = " ")
      print()
  
  def shake(self):

    print(len(self.board))
    for i in range(0,len(self.board)):
      for j in range(0,len(self.board[0])):
        num = random.randint(0,25)
        letter = self.let[num]
        self.board[i][j] = letter
        print("i", i, "j", j)
        print("length of board[0]", len(self.board[i]))

    self.printBoard()

game = Boggle()
game.start()