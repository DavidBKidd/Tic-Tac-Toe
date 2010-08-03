'''
Created on Aug 2, 2010

@author: David Kidd

Coding Begin: 2:13 PM
Coding End:   8:36 PM
'''

class Board:
    def __init__(self):
        self.Array=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.WinningArray=[[[0,0],[0,1],[0,2]],
                           [[1,0],[1,1],[1,2]],
                           [[2,0],[2,1],[2,2]],
                           [[0,0],[1,0],[2,0]],
                           [[0,1],[1,1],[2,1]],
                           [[0,2],[1,2],[2,2]],
                           [[0,0],[1,1],[2,2]],
                           [[2,0],[1,1],[0,2]]]
    
    def DisplayBoard(self):
        print " x 1 2 3"
        print "y"
        print "1  " + self.Array[0][0] + '|' + self.Array[1][0] + '|' + self.Array[2][0]
        print "   -+-+-"
        print "2  " + self.Array[0][1] + '|' + self.Array[1][1] + '|' + self.Array[2][1]
        print "   -+-+-"
        print "3  " + self.Array[0][2] + '|' + self.Array[1][2] + '|' + self.Array[2][2]
    
    def AddMove(self, x, y, Player):
        self.Array[x][y] = Player
    def DeleteMove(self, x, y):
        self.Array[x][y] = " "
    #validate Move: Human players might enter in bad data
    def ValidateMove(self, move):
        splitstr = move.split(",")
        if len(splitstr) != 2:
            return False
        x = int(splitstr[0])-1
        y = int(splitstr[1])-1
        if (x < 0) or (x > 2) or (y < 0) or (y > 2):
            return False
        if (self.Array[x][y] != " "):
            return False
        return True
    
    #Check for a win
    def CheckWin(self):
        #8 win conditions.Chack them manually
        Winner = " "
        for i in range(8):
            if (self.Array[self.WinningArray[i][0][0]][self.WinningArray[i][0][1]] == self.Array[self.WinningArray[i][1][0]][self.WinningArray[i][1][1]] == self.Array[self.WinningArray[i][2][0]][self.WinningArray[i][2][1]]):
                Winner = self.Array[self.WinningArray[i][0][0]][self.WinningArray[i][0][1]]
                if (Winner != " "):
                    break
        if (Winner == " "): #check if we have a tie
            Winner = "T"
            for x in range(3):
                for y in range(3):
                    if (self.Array[x][y]==" "):
                        Winner = " "
        return Winner
    #check for a winning move (two in a row and a clear third)
    def CheckForWinningMove(self, Player):
        point=[-1,-1]
        for i in range(8):
            SetArray = [self.Array[self.WinningArray[i][0][0]][self.WinningArray[i][0][1]], self.Array[self.WinningArray[i][1][0]][self.WinningArray[i][1][1]], self.Array[self.WinningArray[i][2][0]][self.WinningArray[i][2][1]]]
            if (SetArray.count(Player) == 2) and (SetArray.count(' ') == 1):
                item = SetArray.index(' ')
                point = self.WinningArray[i][item]
        return point
    #check for a threatening opportunity (2 clear and one marked)
    def CheckForOpportunity(self,Player):
        point = [-1,-1]
        pointArray = []
        for i in range(8):
            SetArray = [self.Array[self.WinningArray[i][0][0]][self.WinningArray[i][0][1]], self.Array[self.WinningArray[i][1][0]][self.WinningArray[i][1][1]], self.Array[self.WinningArray[i][2][0]][self.WinningArray[i][2][1]]]
            if (SetArray.count(Player) == 1) and (SetArray.count(' ') == 2):
                item = SetArray.index(' ')
                point = self.WinningArray[i][item]
                if (pointArray.count(point)==0):
                    pointArray.append(point)
                item = SetArray.index(' ',item+1 )
                point = self.WinningArray[i][item]
                if (pointArray.count(point)==0):
                    pointArray.append(point)
        return pointArray
        
    def CheckForEmptyCornerOppositePlayer(self,Player):
        point = [-1,-1]
        if (self.Array[0][0] == Player) and (self.Array[2][2] == " "):
            point = [2,2]
        elif (self.Array[2][2] == Player) and (self.Array[0][0] == " "):
            point = [0,0]
        elif (self.Array[0][2] == Player) and (self.Array[2][0] == " "):
            point = [2,0]
        elif (self.Array[2][0] == Player) and (self.Array[0][2] == " "):
            point = [0,2]
        return point
            
    def CheckForEmptyCorner(self):
        point = [-1,-1]
        if (self.Array[0][0] == " "):
            point = [0,0]
        elif (self.Array[2][2] == " "):
            point = [2,2]
        elif (self.Array[0][2] == " "):
            point = [0,2]
        elif (self.Array[2][0] == " "):
            point = [2,0]
        return point
        
    def CheckForEmptySide(self):
        point = [-1,-1]
        if (self.Array[0][1] == " "):
            point = [0,1]
        elif (self.Array[1][0] == " "):
            point = [1,0]
        elif (self.Array[1][2] == " "):
            point = [1,2]
        elif (self.Array[2][1] == " "):
            point = [2,1]
        return point

    def CheckForForkCondition(self, Player):
        point = []
        pointArray = []
        uniquePointArray = []
        for i in range(8):
            SetArray = [self.Array[self.WinningArray[i][0][0]][self.WinningArray[i][0][1]], self.Array[self.WinningArray[i][1][0]][self.WinningArray[i][1][1]], self.Array[self.WinningArray[i][2][0]][self.WinningArray[i][2][1]]]
            if (SetArray.count(Player) == 1) and (SetArray.count(' ') == 2):
                item = SetArray.index(' ')
                point = self.WinningArray[i][item]
                pointArray.append(point)
                item = SetArray.index(' ',item+1 )
                point = self.WinningArray[i][item]
                pointArray.append(point)
        
        for i in range(len(pointArray)):
            if (pointArray.count(pointArray[i])>1):
                if (uniquePointArray.count(pointArray[i])==0):
                    uniquePointArray.append(pointArray[i])

        return uniquePointArray

HumanPlayer = " "
ComputerPlayer = " "
while ((len(HumanPlayer)!= 1) or ((HumanPlayer.find("X") == -1) and (HumanPlayer.find("O") == -1))):
    HumanPlayer = raw_input("Choose your side, X or O:")

if (HumanPlayer == "X"):
    ComputerPlayer = "O"
else:
    ComputerPlayer = "X"
    
playBoard = Board()
playBoard.DisplayBoard()
LastPlayer = "O"
CurrentPlayer = " "
while (playBoard.CheckWin()==" "):
    if (LastPlayer == "O"):
        CurrentPlayer = "X"
    else:
        CurrentPlayer = "O"
    
    if (CurrentPlayer == HumanPlayer): #let the human make a move
        validMove = False
        while (not validMove):
            move = raw_input("Make a move (x,y): ")
            validMove = playBoard.ValidateMove(move)
            if validMove:
                xval = int(move.split(",")[0])-1
                yval = int(move.split(",")[1])-1
                playBoard.AddMove(xval, yval, CurrentPlayer)
            else:
                print "Not a valid move. Try again"
    else: #if there is a winning move, play it
        move = playBoard.CheckForWinningMove(ComputerPlayer)
        if (move[0] != -1):
            playBoard.AddMove(move[0],move[1],ComputerPlayer)
        else: #if the human player has a winning move, block it
            move = playBoard.CheckForWinningMove(HumanPlayer)
            if (move[0] != -1):
                playBoard.AddMove(move[0],move[1],ComputerPlayer)
            else: #If there is an opportunity to create a fork, do so
                movelist = playBoard.CheckForForkCondition(ComputerPlayer)
                if (len(movelist)>0):
                    #it doesn't really matter which move you make
                    playBoard.AddMove(movelist[0][0],movelist[0][1],ComputerPlayer)
                else: #check to see if the human can create a fork
                    threatlist = playBoard.CheckForForkCondition(HumanPlayer)
                    if (len(threatlist)>0):
                        if (len(threatlist)==1): #the easy condition: block it
                            playBoard.AddMove(threatlist[0][0],threatlist[0][1],ComputerPlayer)
                        else: #the complicated condition. Threaten instead, but not if blocking the threat completes the fork
                            movelist = playBoard.CheckForOpportunity(ComputerPlayer)
                            if (len(movelist)>0):
                                for move in movelist: #test each move to see if the blocking move is in the threatlist
                                    playBoard.AddMove(move[0],move[1],ComputerPlayer)
                                    responseMove = playBoard.CheckForWinningMove(ComputerPlayer)
                                    if (threatlist.count(responseMove) > 0):
                                        playBoard.DeleteMove(move[0], move[1])
                                    else:
                                        break
                    else: #see if the center can be taken
                        if (playBoard.Array[1][1] == " "):
                            playBoard.AddMove(1, 1, ComputerPlayer)
                        else: #check corners. If opponent, play opposite
                            move = playBoard.CheckForEmptyCornerOppositePlayer(HumanPlayer)
                            if (move[0] != -1):
                                playBoard.AddMove(move[0],move[1],ComputerPlayer)
                            else:#play an empty corner
                                move = playBoard.CheckForEmptyCorner()
                                if (move[0] != -1):
                                    playBoard.AddMove(move[0],move[1],ComputerPlayer)
                                else:#play an empty side
                                    move = playBoard.CheckForEmptySide()
                                    if (move[0] != -1):
                                        playBoard.AddMove(move[0],move[1],ComputerPlayer)
                                    else: #no moves to make
                                        print "Error! No Valid Moves! You Need to debug better!"
    playBoard.DisplayBoard()
    LastPlayer = CurrentPlayer
    
WinningPlayer = playBoard.CheckWin()
if (WinningPlayer == "T"):
    print "It's a tie."
else:
    print WinningPlayer + "wins!"