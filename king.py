import pygame

class King:
    
    def __init__(self, screen, pos):
        self.screen = screen
        self.pos = pos
        self.color = (255, 0, 0)

    def can_king_move(self, direction, board, horses):
        row, col = self.pos
        if direction == 'left':
            if (row, col -1 ) in horses:
                horse_piece = horses[(row, col-1)]
                if horse_piece.allied:
                    if horse_piece.moveHorse(direction, board, horses):
                        horses.pop((row,col - 1))
                        horses[(row, col - 2)] = horse_piece
                        return True
                    return False
                else:
                    return False
            else:
                return col > 0 and board[row][col - 1] != None
        elif direction == 'right':
            if (row, col + 1 ) in horses:
                horse_piece = horses[(row, col+1)]
                if horse_piece.allied:
                    if horse_piece.allied:
                        if horse_piece.moveHorse(direction, board, horses):
                            horses.pop((row,col + 1))
                            horses[(row, col + 2)] = horse_piece    
                            return True
                        return False
                else:
                    return False
            else:
                return col < len(board[0]) - 1 and board[row][col + 1] != None
        elif direction == 'up':
            if (row - 1, col ) in horses:
                horse_piece = horses[(row - 1, col)]
                if horse_piece.allied:
                    if horse_piece.moveHorse(direction, board, horses):
                        horses.pop((row - 1,col))
                        horses[(row - 2, col)] = horse_piece  
                        return True
                    return False
                else:
                    return False
            else:
                return (row > 0 and board[row - 1][col]) != None
        elif direction == 'down':
            if (row + 1, col ) in horses:
                horse_piece = horses[(row + 1, col)]
                if horse_piece.allied:
                    if horse_piece.moveHorse(direction, board, horses):
                        horses.pop((row + 1,col))
                        horses[(row + 2, col)] = horse_piece
                        return True
                    return False
                else:
                    return False
            else:
                return row < len(board) - 1 and board[row + 1][col] != None
        return False  
    
    def moveKing(self, eventData, board, horses):
        if eventData == 'KD':
            if self.can_king_move('down',board, horses):
                newPos = min(len(board) - 1, self.pos[0] + 1)
                self.pos = (newPos, self.pos[1])
                return True
        elif eventData == 'KU':
            if self.can_king_move('up', board, horses):
                newPos = max(0, self.pos[0] - 1)
                self.pos = (newPos, self.pos[1])
                return True
        elif eventData == 'KR':
            if self.can_king_move('right', board, horses):
                newPos = min(len(board[0]) - 1, self.pos[1] + 1)
                self.pos = (self.pos[0], newPos)
                return True
        elif eventData == 'KL':
            if self.can_king_move('left', board, horses):
                newPos = max(0, self.pos[1] - 1)
                self.pos = (self.pos[0], newPos)
                return True

    def drawKing(self, cellSize):

        kingImage = pygame.transform.scale(pygame.image.load('docs/imgs/king.png'), (cellSize, cellSize))
        self.screen.blit(kingImage, (self.pos[1] *  cellSize, self.pos[0] * cellSize))
