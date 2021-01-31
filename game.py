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
        # creat the numbers on each cell
        self.values() 

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

    def values(self):
        # assing num 0-8 to each cell 
        for r in range(self.size):
            for c in range(self.size):
                if self.borad == "*":
                    continue
                self.borad[r][c] = self.neighboring(r,c)
    
    def neighboring(self, row, col):
        counter = 0
        for r in range(max(0,row-1),min(self.size-1,row+2)):
            for c in range(max(0,col-1),min(self.size,col+2)):
                if self.borad[r][c] == '*':
                    counter += 1
        return counter

def paly(size = 10,bom = 10):
    # develop game strategy
    # 1. creat borad andd put the bombs
    gm = Board(size,bom) 
    # 2. show the board and ask for input
    # 3. check if the location is bom
    # 4. check if we win 
    pass

