class Boggle:
  board = [["-" * 6] * 6]
  let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  def start(self):
    for i in self.board:
      for j in i:
        print(j,)
      

game = Boggle()
game.start()