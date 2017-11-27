'''Written by Bryce Bern and Audrey Lothspeich      3/13/17

This program will open a window on which the user can play connect four either against
another human, a dumb computer AI or a smart computer AI. We adapted our piece movement function
from the ocean simualation homework.'''

#We have imported graphics and did not write any of the code in the graphics.py program
#This programs is credited entirely to Zelle
from graphics import *

#We have imported random and did not write any of the code in the random.py program
#This code is part of python.
from random import *

#Defining a piece class so we can easily place pieces later
class Piece:

    def __init__(self, color, x, y):
        self.color = color
        self.y = y
        self.y = 30
        self.x = x
        self.MakeParts()
        
    def MakeParts (self):
        self.Piece = Circle(Point(self.x, self.y), 50)
        self.Piece.setFill(self.color)
        
    def DrawSelf (self, win):
        self.Piece.draw(win)
        
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.Piece.move(dx, dy)

    def step(self):
        self.move(0, 10)    
        

#Simple graphics drawing of a menu. Allows player to pick who they want to play against or quit the program.
def DrawOpeningScreen (win):
    undraw (win)
    for i in range (3):
        Choice1 = Polygon(Point(0, 333*i), Point(1200, 333*i), Point(1200, 333*(i+1)), Point(0, 333*(i+1)))
        Choice1.setWidth (10)
        Choice1.draw(win)
    
    Instructions = Text(Point(600, 167), '2 Player')
    Instructions.setSize(30)
    Instructions.draw(win)
    Instructions = Text(Point(600, 500), 'Dumb Computer')
    Instructions.setSize(30)
    Instructions.draw(win)
    Instructions = Text(Point(600, 833), 'Smart Computer')
    Instructions.setSize(30)
    Instructions.draw(win)
    
    Rectangle = Polygon(Point(1000, 850), Point(1200, 850), Point(1200, 1000), Point(1000, 1000))
    Rectangle.setWidth(5)
    Rectangle.draw(win)
    
    Quit = Text(Point(1100, 930), 'Quit')
    Quit.setSize(30)
    Quit.draw(win)
    
    Rectangle = Polygon(Point(1000, 150), Point(1200, 150), Point(1200, 0), Point(1000, 0))
    Rectangle.setWidth(5)
    Rectangle.draw(win)
    
    AI = Text(Point(1100, 80), 'AI vs. AI')
    AI.setSize(30)
    AI.draw(win)
    #Take user input (clicking on the menu) to decide what gamemode
    point = win.getMouse ()
    y = point.y
    x = point.x
    undraw (win)
    if x > 1000 and y < 150:
        return 'AI vs. AI'
        
    if y > 850 and x > 1000:
        return 'break'
    if y < 333:
        return '2 Player'
    if 333 < y < 666:
        return 'Dumb AI'
    if 666 < y < 1000:
        return 'Smart AI'
        

#Draws the game interface: instructions and a board with 42 blank spaces.
def DrawBoard(win):
    
    Board = Polygon(Point(150, 260), Point(1010, 260), Point(1010, 1000), Point(150, 1000))
    Board.setWidth (5)
    Board.setFill('yellow')
    Board.draw(win)
    
    DrawSpaces(win)
    
    Instructions = Text(Point(600, 100), 'Click on a column to place a piece!  Get four in a row to win!')
    Instructions.setSize(20)
    Instructions.draw(win)

#Drawing the spaces on our board
def DrawSpaces(win):
    x = 0
    y = 0
    for height in range(6):
        for width in range(7):
            circle = Circle(Point(220 + x, 330 + y), 50)
            circle.setFill('white')
            circle.draw(win)
            x += 120
        x = 0
        y += 120

#Changing our board's display if somebody wins
def winboard(win, color):
    Print = Text(Point(600, 200), color + ' Wins!!!')
    Print.setSize(30)
    Print.draw(win)

#For later use - sets the entire screen to white
def undraw (win):
    undraw = Polygon(Point(0, 0), Point(1200, 0), Point(1200, 1000), Point(0, 1000))
    undraw.setFill('white')
    undraw.draw(win)

#How the smart computer makes decisions
def decisions (win, ListofRed, ListofBlack, columns, color):
    if color == 'red':
        list = [ListofRed, ListofBlack]
    if color == 'black':
        list = [ListofBlack, ListofRed]
    #Here, the range of i acts as a way to check for 4, 3, and 2 in a row combinations
    for i in range(3, 0, -1):
        #Checking for both red and black values
        for item in list:
            for x in range(1, 8):
                #Setting a trial piece equal to all possible placements (ie, the lowest blank spacee in a column)
                TrialPiece = [x, columns[x-1]+1]
                #If the Trial Piece would trigger a 4, 3, or 2 in a row, return the winning x-value!
                if CheckWin (item, TrialPiece, i) == True and columns[x-1] < 6:
                    return 150 + 120*x
                    
    return randint(151, 1010)
    

def PlacePiece (win, color, columns, PlayerChoice, ListofRed, ListofBlack):   
    while True:

        if (color == 'black' or color == 'red') and PlayerChoice == 'AI vs. AI':
            x = (int(decisions (win, ListofRed, ListofBlack, columns, color)))
            y = 5
            
        #Dumb AI returns random integers
        elif color == 'black' and PlayerChoice == 'Dumb AI':
            x = randint(151, 1010)
            y = 5

        #Smart AI will choose to first place a winning piece, then stop the oppenent.
        #Next it will choose to play 3-in-a-row, then stop an opposing 3-in-a-row, etc.
        elif color == 'black' and PlayerChoice == 'Smart AI':
    
            x = (int(decisions (win, ListofRed, ListofBlack, columns, color)))
            y = 5
        
        #Just Use a player input
        else:
            point = win.getMouse()
            x = point.x
            y = point.y
        
        #Safeguarding for someone not clicking in a column
        if x < 150 or x > 1010:
            print("click somewhere above the board!")
        
        #Translating our number into clean low integers
        else:
            newx, columnsnumber = ConvertCoordinates (x, columns)
            if columnsnumber > 6:
                print('That column is full!')
            else:
                break
    
    #Drawing and moving our piece into the given place
    piece = Piece(color, newx, y)
    piece.DrawSelf (win)
    while True:
        piece.step()
        update(100)
        if piece.y >= 930 - 120 * (columnsnumber - 1):
            break
    return ChangeCoord (piece.x, piece.y)

#Used to return clean low integer values
def ChangeCoord (x, y):    
    x = (x-150)//120 + 1
    y = (1050-y)//120
    list = [x, y]
    return list

#Converting our coordinates into pixel dimensions in the window
def ConvertCoordinates (x, columns):
    a = 0
    for n in range(7):
        if n == 6:
            a = 20
        if 150 + 120*n <= x <= 270 + 120*n + a:
            x = 220 + 120*n
            columns[n] +=1
            columnsnumber = columns[n]
    
    return x, columnsnumber



#Our checkwin parameter allows us to tell whether or not any number of pieces is in a row
def CheckWin (list, newPiece, checkwin):
    #Setting the x and y values of the 'newly placed' piece to variables
    checkx = newPiece[0]
    checky = newPiece[1]
    count = 0
    verticallist = []
    #Adding all vertical values that relate to our newly placed piece into a list
    for item in list:
        if item[0] == checkx and (checky - 1 == item[1] or checky - 2 == item[1] or checky - 3 == item[1]):
            verticallist.append(item)
    verticallist.append(newPiece)
    verticallist.sort()

    #If there are enough pieces in a row, you win!
    for item in verticallist:
        index = verticallist.index(item)
        if index + 1 == len(verticallist):
            pass
        elif item[1] + 1 == verticallist[index+1][1]:
            count += 1
            #Changed
            if count > (checkwin - 1):
                return True
                
        else:
            count = 0
        
    count = 0
    horizontallist = []
    
    #Same routine as vertical
    for item in list:
        if (item[0] == newPiece[0] + 1 or item[0] == newPiece[0] + 2 or item[0] == newPiece[0] + 3 or item[0] == newPiece[0] + -1 or item[0] == newPiece[0] - 2 or item[0] == newPiece[0] - 3) and item[1] == newPiece[1]:
            horizontallist.append(item) 
    horizontallist.append(newPiece)
    horizontallist.sort()

    for item in horizontallist:
        index = horizontallist.index(item)
        if index + 1 == len(horizontallist):
            pass
        elif item[0] + 1 == horizontallist[index+1][0]:
            count += 1
            #Changed
            if count > (checkwin - 1):
                return True
                
        else:
            count = 0


    count = 0
    diagonal1 = []
    diagonal2 = []
    #Getting all possible diagonal values into a list
    for item in list:
        for n in range (1, 4):    
            if (item[0] == checkx + n and item[1] == checky + n) or (item[0] == checkx - n and item[1] == checky - n):
                diagonal1.append(item)
        for n in range(1, 4):
            if (item[0] == checkx - n and item[1] == checky + n) or (item[0] == checkx + n and item[1] == checky - n):
                diagonal2.append(item)
                
    
    #We need to separate lists for diagonals because they can be left to right or right to left
    diagonal1.append([checkx, checky])
    diagonal2.append([checkx, checky])
    diagonal1.sort()
    diagonal2.sort()
    

    #Checking one diagonal (similar to vertical and horizontal)
    for item in diagonal1:
        index = diagonal1.index(item)
        if index + 1 == len(diagonal1):
            pass
            
        elif item[0] + 1 == diagonal1[index+1][0] and (item[1] + 1 == diagonal1[index+1][1]):
            count += 1

            if count > (checkwin - 1): 
                return True 
        else:
            count = 0
        
  
           
    count = 0
     
    #Checking other diagonal
    for item in diagonal2:
        index = diagonal2.index(item)
        if index + 1 == len(diagonal2):
            pass
        
        elif item[0] + 1 == diagonal2[index+1][0] and item[1] - 1 == diagonal2[index+1][1]:
            count += 1
            #Changed

            if count > (checkwin - 1):
                return True
        #Still need this?
        else:
            count = 0
            
#Keeps track of the number of pieces each player has played, where they are located, and how full the board is.
def turns (win, PlayerChoice):
    #columns allows us to keep track of how full each column is
    columns = [0,0,0,0,0,0,0]
    #these two lists will allow us to keep track of every single red or black piece placed
    ListofRed = []
    ListofBlack = []
    
    #This loop allows the turns to go on continuously
    while True:
        #If we reach a certain number of placements, the game is a tie
        if len(ListofRed)+len(ListofBlack) > 41:
            print("tie game!")
            Print = Text(Point(600, 200), 'TIE GAME!!!')
            Print.setSize(30)
            Print.draw(win)
            break
        
        #Red places first
        newPiece = PlacePiece (win, 'red', columns, PlayerChoice, ListofRed, ListofBlack)
        ListofRed.append(newPiece)
        ListofRed.sort()
        if CheckWin (ListofRed, newPiece, 3) == True:
            print('four in a row')
            winboard (win, 'Red')
            break
        
        #Now black
        newPiece = PlacePiece (win, 'black', columns, PlayerChoice, ListofRed, ListofBlack)
        ListofBlack.append(newPiece)
        ListofBlack.sort()
        if CheckWin (ListofBlack, newPiece, 3) == True:
            print('four in a row')
            winboard (win, 'Black')
            break
            
def main ():
    #Setting up basic window features.
    winHeight = 1000
    winWidth = 1200
    win = GraphWin('Connect Four', winWidth, winHeight)
    #This loop allows our window to stay open and be playable multiple times in a row
    while True:
        PlayerChoice = DrawOpeningScreen(win)
        #If the player clicks on 'quit', then the program will close
        if PlayerChoice == 'break':
            break
        DrawBoard(win)
        turns (win, PlayerChoice)      
        win.getMouse()


if __name__ == '__main__':
    main ()
















    
