LEVEL1 = [
    [None, None, None, None, 'b'],
    ['w', None, None, None, 'w'],
    ['b', 'w', 'b', 'w', 'b'],
    [None, 'b', 'w', 'b', None],
    [None, 'w', 'b', 'w', None],
    [None, 'b', 'w', 'b', None], 
]

LEVEL1_PIECES = {(4,1) : 'H', (4,3) : 'H', (1,0) : 'E', (0,4) : 'E', (5,2) : 'K'}

LEVEL2 = [
    ['w', None, 'w', None, 'w'],
    ['b', None, 'b', None, 'b'],
    ['w', None, 'w', None, 'w'],
    ['b', None, 'b', None, 'b'],
    ['w', None, 'w', None, 'w'],
    ['b' ,'w' ,'b' ,'w' ,'b'],
    ['w' ,'b' ,'w' ,'b' ,'w'],
]

LEVEL2_PIECES = { (5,2) : 'H' , (5,3) : 'H', (1, 4) : 'E', (0,0) : 'E', (6,2) : 'K'}

LEVEL3 = [
    [None, None, None, None, None, None, None, 'b', 'w', 'b'],
    [None, None, None, 'w', 'b', 'w', None, 'w', 'b', None],
    [None, None, None, 'b', None, 'b', None, 'b', 'w', None],
    ['b', None, None, 'w', None, 'w', 'b', 'w', 'b', None],
    ['w', 'b', 'w', 'b', None, 'b', 'w', 'b', 'w', 'b'],
    [None, None, 'b', 'w', 'b', 'w', 'b', 'w', None, None],
    [None, None, 'w', None, None, 'b', None, 'b', None, None],
    [None, None, 'b', 'w', 'b', 'w', None, 'w', 'b', 'w'],
    [None, None, None, None, 'w', 'b', 'w', 'b', None, None],
    [None, None, None, 'w', 'b', 'w', None, None, None, None]
]

LEVEL3_PIECES = {(2,3): 'H', (2, 8): 'E', (9,4): 'K'} 

LEVEL4 = [

    [None, None, 'w', None, None, None, None, None, None,],
    ['b','w','b','w','b','w','b','w',None],
    [None, None, 'w', 'b', None, None, 'w', 'b', 'w'],
    ['b', 'w', 'b', 'w', 'b', 'w', 'b', None, 'b'],
    ['w', None, 'w', 'b', 'w', 'b', 'w', None, None],
    ['b', None, 'b', 'w', 'b', 'w', 'b', None, None],
    ['w', None, 'w', 'b', None, None, None, None, None],
    ['b', 'w', 'b', None, None, None, None, None, None]
]

LEVEL4_PIECES = {(2,2): 'H', (1, 7): 'H', (5,3): 'H', (1,0): 'E', (0, 2): 'E', (3,8): 'E', (6,3): 'K'} 


LEVEL5 = [
    [None, None, None, None, None, None, None,'b', 'w', 'b'],
    [None, None, None, 'w', 'b', 'w', None, 'w', 'b', None], 
    [None, None, None, 'b', None, 'b', None, 'b', 'w',None],   
    ['b', None, None, 'w', None, 'w', 'b', 'w', 'b', None],
    ['w', 'b', 'w', 'b', None, 'b', 'w', 'b', 'w', 'b'],
    [None, None, 'b', 'w', 'b', 'w', 'b', 'w', None, None],
    [None,None, 'w', None, None,  'b', None, 'b', None, None],
    [None, None, 'b', 'w', 'b', 'w', None, 'w', 'b', 'w'],
    [None, None, None, None, 'w', 'b', 'w', 'b', None, None],
    [None, None, None, 'w', 'b', 'w', None, None, None, None]
]

LEVEL5_PIECES = {(2,5): 'H', (5, 4): 'H', (4,6): 'H', (3, 7): 'H', (7,7): 'H', (3,0): 'E', (0, 9): 'E', (1,8): 'E', (7, 9): 'E', (9,3): 'E', (5,6): 'K'} 
