import pygame 
import levels
import king 
import horse

class Game ():

    def __init__(self,screen):
        self.screen = screen

    def setLevel(self,level):
        self.level = level
        self.gameSetUp()

    def setMoves(self):
        self.moves = 0

    def gameSetUp(self):

        if self.level >= 1 and self.level <= 3:
            self.color1 = (189, 191, 212)
            self.color2 = (109, 111, 155)
        elif self.level >= 4 and self.level <= 6:
            self.color1 = (207, 14, 14)
            self.color2 = (245, 245, 220)
        else:
            self.color1 = (0, 191, 255)
            self.color2 = (211, 211, 211)

        if self.level == 1:
            self.board = levels.LEVEL1
            self.pieces = levels.LEVEL1_PIECES
        elif self.level == 2:
            self.board = levels.LEVEL2
            self.pieces = levels.LEVEL2_PIECES
        elif self.level == 3:
            self.board = levels.LEVEL3
            self.pieces = levels.LEVEL3_PIECES
        elif self.level == 4:
            self.board = levels.LEVEL4
            self.pieces = levels.LEVEL4_PIECES
        elif self.level == 5:
            self.board = levels.LEVEL5
            self.pieces = levels.LEVEL5_PIECES

        WIDTH, HEIGHT = 800, 800
        max_cols = max(len(row) for row in self.board)
        self.gridSize = 3
        self.cellSize = min(WIDTH // max_cols, HEIGHT // len(self.board))

        self.horses = {}

        for pos, piece_type in self.pieces.items():
            if piece_type == 'K':
                self.king = king.King(self.screen, pos)
            elif piece_type == 'H':
                horse_piece = horse.Horse(self.screen, pos, 1)
                self.horses[pos] = horse_piece
            elif piece_type == 'E':
                horse_piece = horse.Horse(self.screen, pos, 0)
                self.horses[pos] = horse_piece
    
    def assign_choices(self, items):
        assigned_choices = {} 

       
        sorted_items = sorted(items.items(), key=lambda x: len(x[1]), reverse=True)

        for item, choices in sorted_items:
            for choice in choices:
                if choice not in assigned_choices.values():
                    assigned_choices[item] = choice
                    break
            
        if len(assigned_choices) == len(items):
            return assigned_choices
        else:
            return None
        
    def gameOver(self):
        allCaptures = {}
 
        for pos,horse in self.horses.items():
            if not horse.allied:
                allCaptures[pos] = horse.canBeCaptured(self.horses, self.board)
        if self.assign_choices(allCaptures):
            return True

    def handle_king_movement(self, eventData):
        if self.king.moveKing(eventData, self.board, self.horses):
            self.moves += 1
            
    def draw_level(self):
        self.screen.fill((0, 0, 0))
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 'b':
                    color = self.color1
                elif cell == 'w':
                    color = self.color2
                
                else:
                    continue
                pygame.draw.rect(self.screen, color, (j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize))

        self.king.drawKing(self.cellSize)    

        for pos,horse in self.horses.items():
            horse.drawHorse(self.cellSize)

    def draw_endSreen(self):
        
        sel_color = '#152238'

        background_surf  = pygame.Surface((800,600))
        background_surf.fill('#545AA7')

        return_surf = pygame.image.load('./docs/imgs/return-hover.png')
        self.return_rect = return_surf.get_rect(center = (400,550))

        title_font = pygame.font.Font(None, 50)

        title_text = title_font.render('LEVEL ' + str(self.level), False, 'White')
        title_rect = title_text.get_rect(center = (400,150))

        yourmoves_text = title_font.render('Your Moves:  ' + str(self.moves), False, 'White')
        yourmoves_rect = yourmoves_text.get_rect(center = (400,250))

        pcmoves_text = title_font.render('Optimal Moves: Soon (?) ', False, 'White')
        pcmoves_rect = pcmoves_text.get_rect(center = (400,350))

        score_text = title_font.render('Score = To Do ', False, 'White')
        score_rect = score_text.get_rect(center = (400,450))

        self.screen.blit(background_surf, (0,0))
        self.screen.blit(title_text,title_rect)
        self.screen.blit(yourmoves_text,yourmoves_rect)
        self.screen.blit(pcmoves_text,pcmoves_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(return_surf,self.return_rect)

    def handle_end_screen(self,eventData,eventType):
        if eventType == 'Mouse Movement':
            return
        elif eventType == 'Mouse Select':
            if self.return_rect.collidepoint(eventData):
                return 'select level'
        elif eventType == 'Keyboard Movement':
            return
        elif eventType == 'Keyboard Select':
            return 'select level'
