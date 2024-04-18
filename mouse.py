class Mouse():

    def __init__(self,menu,rules,levelSelect,game):
        self.menu = menu
        self.rules = rules
        self.levelSelect = levelSelect
        self.ingame = game

    def mouse_handler(self,state,eventData,eventType):

        if state == 'menu':
            return self.menu.handle_menu(eventData, eventType)
        elif state == 'rules':
            return self.rules.handle_rules(eventData, eventType)
        elif state == 'select level':
            return self.levelSelect.handle_level_select(eventData, eventType)
        elif state == 'end screen':
            return self.ingame.handle_end_screen(eventData, eventType)
        
