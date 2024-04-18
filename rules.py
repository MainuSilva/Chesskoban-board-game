import pygame

class Rules:

    def __init__(self,screen):
        self.screen = screen
        

    def display_rules(self):
        rules_font = pygame.font.Font(None, 20)
        title_font = pygame.font.Font(None, 100)
        back_font = pygame.font.Font(None, 50)

        background_surf  = pygame.Surface((800,600))
        background_surf.fill('#545AA7')

        sel_color = '#152238'

        title_text = title_font.render('Chesskoban', False, 'White')
        title_rect = title_text.get_rect(center = (400,150))

        self.return_text = back_font.render('Back', False, sel_color)
        self.return_rect = self.return_text.get_rect(center = (400,500))

        self.screen.blit(background_surf, (0,0))
        self.screen.blit(title_text, title_rect)

        line = "Chesskoban is a Puzzle game with the combination of Chess mechanics and Sokoban game for chess lovers and beginners"

        self.rules_text = rules_font.render(line, False, 'White')
        self.rules_rect = self.rules_text.get_rect(center = (400, 300))
        self.screen.blit(self.rules_text, self.rules_rect)

        line = "You will control the white horses, needing to reposition them to capture the black horses"
        
        self.rules_text = rules_font.render(line, False, 'White')
        self.rules_rect = self.rules_text.get_rect(center = (400, 350))
        self.screen.blit(self.rules_text, self.rules_rect)

        self.screen.blit(self.return_text, self.return_rect)

    def handle_rules(self,eventData,eventType):

        if eventType == "Keyboard Select":
            if eventData == 'ENTER':
                return 'menu'
        elif eventType == "Mouse Select":
            if self.return_rect.collidepoint(eventData):
                return 'menu'
            
        

