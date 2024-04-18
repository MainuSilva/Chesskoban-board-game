class Keyboard():

    def __init__(self,menu,rules,levelSelect,in_game):
        self.menu = menu
        self.rules = rules
        self.levelSelect = levelSelect
        self.in_game = in_game

    def keyboard_handler(self,state,eventData,eventType):
        if state == 'menu':
            return self.menu.handle_menu(eventData, eventType)
        elif state == 'rules':
            return self.rules.handle_rules(eventData, eventType)
        elif state == 'select level':
            return self.levelSelect.handle_level_select(eventData, eventType)
        elif state == 'in-game':
            if eventData == 'ESC':
                return 'select level' 
            else:
            	return self.in_game.handle_king_movement(eventData)
        elif state == 'end screen':
            return self.in_game.handle_end_screen(eventData,eventType)
        
