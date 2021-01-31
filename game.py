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
                if self.borad[r][c] == "*":
                    continue
                self.borad[r][c] = self.neighboring(r,c)
    
    def neighboring(self, row, col):
        counter = 0
        for r in range(max(0,row-1),min(self.size,row+2)):
            for c in range(max(0,col-1),min(self.size,col+2)):
                if self.borad[r][c] == '*':
                    counter += 1
        return counter

    def dig(self, row, col):
        self.dug.append((row,col))

        if self.borad[row][col] == "*":
            return False
        elif self.borad[row][col] > 0 :
            return True
        
        for r in range(max(0,row-1),min(self.size,row+2)):
            for c in range(max(0,col-1),min(self.size,col+2)):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)

        return True

    def __str__(self):
        visible = [ [None for _ in range(self.size)] for _ in range(self.size)]
        string_borad = ""
        for r in range(self.size):
            for c in range(self.size):
                if(r,c) in self.dug:
                    visible[r][c] = " "+str(self.borad[r][c])+" "
                else:
                    visible[r][c] = " _ "
        for ls in visible:
            string_borad += f"{ls}" +"\n"
        return string_borad

def paly(size = 10,bom = 10):
    # develop game strategy
    # 1. creat borad andd put the bombs
    gm = Board(size,bom)
    # game loop
    while True:
        # 2. show the board and ask for input
        print(gm)
        inp = input("Enter palce to dig to: ").split(" ")
        r , c = int(inp[0])-1, int(inp[1])-1
        # 3. check if the location is bom
        if (r,c) in gm.dug or gm.dig(r,c):
            # 4. check if we win 
            if(len(gm.dug)== size**2-bom):
                print("*"*20)
                print("Winner Winner")
                print("*"*20)
                break
            continue

        print(gm)
        print("Hit a bom ;(")
        break
    
# Ask for size and num of boms

while True:
    s = int(input("Enter the size of the board (min 3): "))     
    b = int(input("Enter the number of boms (min 3): "))
    paly(max(3,s),max(3,b))

    if input("\nPlay again y/n? ").lower() == "n":
        break