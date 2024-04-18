import pygame

class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.selected_option = 1

    def display_menu(self):
        menu_font = pygame.font.Font(None, 70)
        title_font = pygame.font.Font(None, 100)
        sel_color = '#152238'

        background_surf  = pygame.Surface((800,600))
        background_surf.fill('#545AA7')

        title_text = title_font.render('Chesskoban', False, 'White')
        title_rect = title_text.get_rect(center = (400,150))

        self.play_text = menu_font.render('Play', False, sel_color if self.selected_option == 1 else 'White')
        self.play_rect = self.play_text.get_rect(center = (400, 300))

        self.rules_text = menu_font.render('Rules', False, sel_color if self.selected_option == 2 else 'White')
        self.rules_rect = self.rules_text.get_rect(center = (400, 400))

        self.quit_text = menu_font.render('Quit', False, sel_color if self.selected_option == 3 else 'White')
        self.quit_rect = self.quit_text.get_rect(center = (400, 500))

        self.screen.blit(background_surf, (0,0))
        self.screen.blit(title_text, title_rect)
        self.screen.blit(self.play_text, self.play_rect)
        self.screen.blit(self.rules_text, self.rules_rect)
        self.screen.blit(self.quit_text, self.quit_rect)

    def handle_menu(self, eventData, eventType):
        
        if eventType == 'Keyboard Movement':
            if eventData == 'KD':
                if self.selected_option == 3:
                    self.selected_option = 1
                else:    
                    self.selected_option += 1
                return 
            elif eventData == 'KU':
                if self.selected_option == 1:
                    self.selected_option = 3
                else:
                    self.selected_option -= 1
                return
        elif eventType == 'Mouse Movement':
            if self.play_rect.collidepoint(eventData):
                self.selected_option = 1
                return
            elif self.rules_rect.collidepoint(eventData):
                self.selected_option = 2
                return
            elif self.quit_rect.collidepoint(eventData):
                self.selected_option = 3
                return
        elif eventType == 'Keyboard Select':
            print("Hello")
            if self.selected_option == 1:
                return 'select level'
            elif self.selected_option == 2:
                return 'rules'
            elif self.selected_option == 3:
                return 'quit'
        elif eventType == 'Mouse Select':
            if self.play_rect.collidepoint(eventData):
                return 'select level'
            elif self.rules_rect.collidepoint(eventData):
                return 'rules'
            elif self.quit_rect.collidepoint(eventData):
                return 'quit'