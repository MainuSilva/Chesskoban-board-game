import pygame
import sys
import menu
import rules
import levelSelect
import keyboard
import mouse
import game


# Initialize Pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

state = 'menu'
level = -1

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

mn = menu.Menu(screen)
rls = rules.Rules(screen)
ls = levelSelect.LevelSelect(screen)
gs = game.Game(screen)
kbd = keyboard.Keyboard(mn,rls,ls,gs)
ms = mouse.Mouse(mn,rls,ls,gs)


resize = True
# Game loop
while True:

    if state == 'menu':
        mn.display_menu()
    elif state == 'rules':
        rls.display_rules()
    elif state == 'select level':
        ls.display_levelSelector()
    elif state == 'in-game':
        if (resize):
            screen = pygame.display.set_mode((WIDTH,800))
            resize = False

        gs.draw_level()

        if gs.gameOver():
            state = 'end screen'
            screen = pygame.display.set_mode((WIDTH,HEIGHT))
            resize = True
    elif state == 'end screen':
        gs.draw_endSreen()
    elif state == 'quit':
        pygame.quit()
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                kbd.keyboard_handler(state,'KD', 'Keyboard Movement')
                 
            elif event.key == pygame.K_UP:
                kbd.keyboard_handler(state, 'KU', 'Keyboard Movement')

            elif event.key == pygame.K_LEFT:
                kbd.keyboard_handler(state, 'KL', 'Keyboard Movement')
 
            elif event.key == pygame.K_RIGHT:
                kbd.keyboard_handler(state, 'KR', 'Keyboard Movement') 
                
            elif event.key == pygame.K_ESCAPE:
                kbd.keyboard_handler(state, 'ESC', 'Keyboard Movement') 

            elif event.key == pygame.K_RETURN:
                int_state = kbd.keyboard_handler(state, 'ENTER', 'Keyboard Select')
                if isinstance(int_state, tuple):
                    if len(int_state) == 2:
                        state, level = int_state
                        gs.setLevel(level)
                        gs.setMoves()
                    elif len(int_state) == 1:
                        state = int_state[0]
                        level = -1
                else:
                    state = int_state
                    level = -1

        elif event.type == pygame.MOUSEMOTION:
            ms.mouse_handler(state,event.pos,'Mouse Movement')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                int_state = ms.mouse_handler(state, event.pos, 'Mouse Select')
                if isinstance(int_state, tuple):
                    if len(int_state) == 2:
                        state, level = int_state
                        gs.setLevel(level)
                        gs.setMoves()
                    elif len(int_state) == 1:
                        state = int_state[0]
                        level = -1
                else:
                    state = int_state
                    level = -1

        

    pygame.display.update()
    clock.tick(60)
