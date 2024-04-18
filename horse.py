import pygame

class Horse:

    def __init__(self,screen, pos, allied):
        self.pos = pos
        self.screen = screen
        self.allied = allied

    def isInBoard(self,pos,board):
        
        if pos[1] < 0 or pos[0] < 0:
            return False
        if pos[1] > len(board[0]) - 1 or pos[0] > len(board) - 1:
            return False
        if board[pos[0]][pos[1]] == None:
            return False
        return True

    def canBeCaptured(self,horses,board):

        knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        possiblePositions = []
        allHorses = []

        for (x,y) in knightMoves:
            if self.isInBoard((self.pos[0] + x, self.pos[1] + y), board):
                possiblePositions.append((self.pos[0] + x, self.pos[1] + y))

        for pos,horse in horses.items():
            if pos in possiblePositions and horse.allied:
                allHorses.append(pos)

        return allHorses

    def canMove(self, direction, board, horses):
        row, col = self.pos
        if direction == 'left':
            if (row,col-1) in horses:
                return False
            return col > 0 and board[row][col - 1] != None
        elif direction == 'right':
            if (row,col+1) in horses:
                return False
            return col < len(board[0]) - 1 and board[row][col + 1] != None
        elif direction == 'up':
            if (row - 1,col) in horses:
                return False
            return row > 0 and board[row - 1][col] != None
        elif direction == 'down':
            if (row + 1,col) in horses:
                return False
            return row < len(board) - 1 and board[row + 1][col] != None
        return False  

    def moveHorse(self, direction,board, horses):
        if direction == 'left':
            if self.canMove(direction,board,horses):
                newPos = max(0, self.pos[1] - 1)
                self.pos = (self.pos[0], newPos)
                return 1
            return 0
        elif direction == 'right':
            if self.canMove(direction, board,horses):
                newPos = min(len(board[0]) - 1, self.pos[1] + 1)
                self.pos = (self.pos[0], newPos)
                return 1
            return 0 
        elif direction == 'up':
            if self.canMove(direction,board,horses):
                newPos = max(0, self.pos[0] - 1)
                self.pos = (newPos, self.pos[1])
                return 1
            return 0 
        elif direction == 'down':
            if self.canMove(direction,board,horses):
                newPos = min(len(board) - 1, self.pos[0] + 1)
                self.pos = (newPos, self.pos[1])
                return 1
            return 0
                

    def drawHorse(self,cellSize):
        horseImage = pygame.transform.scale(pygame.image.load('docs/imgs/white-knight.png') if self.allied else pygame.image.load('docs/imgs/black-knight.png'), (cellSize, cellSize))
        self.screen.blit(horseImage, (self.pos[1] *  cellSize, self.pos[0] * cellSize))