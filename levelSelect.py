import pygame

class LevelSelect:

    def __init__(self,screen):
        self.screen = screen
        self.selected_option = 1
        self.hovered = 0

    def display_levelSelector(self):

        title_font = pygame.font.Font(None, 80)

        background_surf = pygame.Surface((800,600))
        background_surf.fill('#545AA7')

        return_surf = pygame.image.load('./docs/imgs/return.png' if self.hovered != 0 else './docs/imgs/return-hover.png')
        self.return_rect = return_surf.get_rect(center = (80,50))

        lvl_surf1 = pygame.image.load('./docs/imgs/levels/1.png' if self.hovered != 1 else './docs/imgs/levels/1-hover.png')
        lvl_surf2 = pygame.image.load('./docs/imgs/levels/2.png' if self.hovered != 2 else './docs/imgs/levels/2-hover.png')
        lvl_surf3 = pygame.image.load('./docs/imgs/levels/3.png' if self.hovered != 3 else './docs/imgs/levels/3-hover.png')
        lvl_surf4 = pygame.image.load('./docs/imgs/levels/4.png' if self.hovered != 4 else './docs/imgs/levels/4-hover.png')
        lvl_surf5 = pygame.image.load('./docs/imgs/levels/5.png' if self.hovered != 5 else './docs/imgs/levels/5-hover.png')
        lvl_surf6 = pygame.image.load('./docs/imgs/levels/6.png' if self.hovered != 6 else './docs/imgs/levels/6-hover.png')
        lvl_surf7 = pygame.image.load('./docs/imgs/levels/7.png' if self.hovered != 7 else './docs/imgs/levels/7-hover.png')
        lvl_surf8 = pygame.image.load('./docs/imgs/levels/8.png' if self.hovered != 8 else './docs/imgs/levels/8-hover.png')
        lvl_surf9 = pygame.image.load('./docs/imgs/levels/9.png' if self.hovered != 9 else './docs/imgs/levels/9-hover.png')

        self.lvl_rect1 = lvl_surf1.get_rect(center = (250,225))
        self.lvl_rect2 = lvl_surf2.get_rect(center = (400,225))
        self.lvl_rect3 = lvl_surf3.get_rect(center = (550,225))

        self.lvl_rect4 = lvl_surf4.get_rect(center = (250,325))
        self.lvl_rect5 = lvl_surf5.get_rect(center = (400,325))
        self.lvl_rect6 = lvl_surf6.get_rect(center = (550,325))

        self.lvl_rect7 = lvl_surf7.get_rect(center = (250,425))
        self.lvl_rect8 = lvl_surf8.get_rect(center = (400,425))
        self.lvl_rect9 = lvl_surf9.get_rect(center = (550,425))

        title_text = title_font.render('Level Selector', False, 'White')
        title_rect = title_text.get_rect(center = (400,125))


        self.screen.blit(background_surf, (0,0))
        self.screen.blit(title_text, title_rect)

        self.screen.blit(lvl_surf1,self.lvl_rect1)
        self.screen.blit(lvl_surf2,self.lvl_rect2)
        self.screen.blit(lvl_surf3,self.lvl_rect3)
        self.screen.blit(lvl_surf4,self.lvl_rect4)
        self.screen.blit(lvl_surf5,self.lvl_rect5)
        self.screen.blit(lvl_surf6,self.lvl_rect6)
        self.screen.blit(lvl_surf7,self.lvl_rect7)
        self.screen.blit(lvl_surf8,self.lvl_rect8)
        self.screen.blit(lvl_surf9,self.lvl_rect9)

        self.screen.blit(return_surf, self.return_rect)
    
    def handle_level_select(self, eventData, eventType):

        if eventType == 'Mouse Movement':
            if self.lvl_rect1.collidepoint(eventData):
                self.hovered = 1
            elif self.lvl_rect2.collidepoint(eventData):
                self.hovered = 2
            elif self.lvl_rect3.collidepoint(eventData):
                self.hovered = 3
            elif self.lvl_rect4.collidepoint(eventData):
                self.hovered = 4
            elif self.lvl_rect5.collidepoint(eventData):
                self.hovered = 5
            elif self.lvl_rect6.collidepoint(eventData):
                self.hovered = 6
            elif self.lvl_rect7.collidepoint(eventData):
                self.hovered = 7
            elif self.lvl_rect8.collidepoint(eventData):
                self.hovered = 8
            elif self.lvl_rect9.collidepoint(eventData):
                self.hovered = 9
            elif self.return_rect.collidepoint(eventData):
                self.hovered = 0
            else:
                self.hovered = -1
            return
        elif eventType == 'Mouse Select':
            if self.lvl_rect1.collidepoint(eventData):
                return 'in-game', 1
            elif self.lvl_rect2.collidepoint(eventData):
                return 'in-game', 2
            elif self.lvl_rect3.collidepoint(eventData):
                return 'in-game', 3
            elif self.lvl_rect4.collidepoint(eventData):
                return 'in-game', 4
            elif self.lvl_rect5.collidepoint(eventData):
                return 'in-game', 5
            elif self.lvl_rect6.collidepoint(eventData):
                return 'in-game', 6
            elif self.lvl_rect7.collidepoint(eventData):
                return 'in-game', 7
            elif self.lvl_rect8.collidepoint(eventData):
                return 'in-game', 8
            elif self.lvl_rect9.collidepoint(eventData):
                return 'in-game', 9
            elif self.return_rect.collidepoint(eventData):
                return 'menu'     
        elif eventType == 'Keyboard Movement':
            if eventData == 'KU':
                if self.hovered <= 3:
                    self.hovered = 0
                else:
                    self.hovered -= 3
            elif eventData == 'KD':
                if self.hovered == 7:
                    self.hovered = 1
                elif self.hovered == 8:
                    self.hovered = 2
                elif self.hovered == 9:
                    self.hovered = 3
                else:
                    self.hovered += 3
            elif eventData == 'KR':
                if self.hovered == 3:
                    self.hovered = 1
                elif self.hovered == 6:
                    self.hovered = 4
                elif self.hovered == 9:
                    self.hovered = 7
                else:
                    self.hovered += 1
            elif eventData == 'KL':
                if self.hovered == 1:
                    self.hovered = 3
                elif self.hovered == 4:
                    self.hovered = 6
                elif self.hovered == 7:
                    self.hovered = 9
                else:
                    self.hovered -= 1

        elif eventType == 'Keyboard Select':
            if self.hovered == 0:
                return 'menu'
            elif self.hovered >= 1 and self.hovered <= 9:
                return 'in-game', self.hovered







        