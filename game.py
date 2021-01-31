import random

class Board:
    def __init__(self, size,boms):
        # creat a board vars
        self.size = size
        self.boms = boms
        # save palces we have visited
        self.dug = []
        # creat the borad
        self.borad = self.make_borad()

    def make_borad(self):
        # construct the borad
        borad = [ [None for _ in range(self.size)] for _ in range(self.size)]
        
        # plant the boms
        palnted = 0
        while (palnted < self.boms):
            row = random.randint(0,self.size -1)
            col = random.randint(0,self.size -1)
            if borad[row][col] == "*":
                continue
            borad[row][col] = "*"
            palnted += 1
        
        return borad

def paly(size = 10,bom = 10):
    # develop game strategy
    # 1. creat borad andd put the bombs
    gm = Board(size,bom) 
    # 2. show the board and ask for input
    # 3. check if the location is bom
    # 4. check if we win 
    pass

