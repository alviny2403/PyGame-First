import pygame, sys, random
from assets import *
pygame.init()

# start screen text
titleFont = pygame.font.Font("freesansbold.ttf", 64)
title = titleFont.render(
    "Dino Adventure", 
    True, (255,255,255), (0,0,0)
)
titleRect = title.get_rect()
titleRect.center = (swidth//2, sheight//2)
textFont = pygame.font.Font("freesansbold.ttf", 24)
text = textFont.render(
    "--- press space to continue ---", 
    True, (255,255,255), (0,0,0)
)
textRect = text.get_rect()
textRect.center = (swidth//2, sheight//2+150)

# tutorial screen text
tutorialFont = pygame.font.Font("freesansbold.ttf", 24)
tutorial = tutorialFont.render(
    "Use WASD to move around", 
    True, (255,255,255), (0,0,0)
)
tutorialRect = tutorial.get_rect()
tutorialRect.center = (swidth//2, sheight//2)

# end screen text
endFont = pygame.font.Font("freesansbold.ttf", 64)
end = endFont.render(
    f"GAME OVER --- YOU WON!", 
    True, (255,255,255), (0,0,0)
)
endRect = end.get_rect()
endRect.center = (swidth//2,sheight//2)

# transpose map matrix for compatibility

mapBorder = 150
mapOffsetX = 0
mapOffsetY = 0
mapMove = False
mapEdge = False

def transpose(l1, l2):
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

# map matrix with asset value at each tile location
mainMap1Og = [[ 2, 42,  2,  0,  2,  1,  0,  2,  1,  2,  1,  2],  
              [39, 40, 40, 39,  2,  1,  1,  2,  2,  1,  1,  1],  
              [ 2,  1,  2, 40, 42,  1,  1,  0,  0,  1,  1,  1],  
              [ 1,  2,  2,  2, 41,  2, 39,  2,  1, 42,  1,  1],  
              [ 1,  1,  1,  1, 39, 42, 40, 40, 42, 39, 41,  1],  
              [ 1,  1,  1,  0,  1, 41,  1,  1,  2,  2, 39,  1],  
              [ 1,  1,  1,  2,  1, 39,  1,  0,  1,  1, 42, 39]]

overlay1Og = [[-1, -1, 34, 34, 33, 22, 22, 22, 22, 22, 22, 22],  
              [-1, -1, -1, -1, -1, 33, 22, 22, 22, 35, 33, 22],  
              [10, 10, 10, -1, -1, -1, 34, 34, 34, -1,  9, 22],  
              [22, 22, 22, 23, -1, -1, -1, -1, -1, -1, 33, 35],  
              [22, 22, 22, 11, -1, -1, -1, -1, -1, -1, -1, -1],  
              [22, 22, 22, 22, 23, -1,  9, 11,  9, 11, -1, -1],  
              [22, 22, 22, 22, 23, -1, 33, 22, 22, 35, -1,130]]

# transpose for RenderMap to read into for loops
mainMap1 = []
mainMap1 = transpose(mainMap1Og, mainMap1)

overlay1 = []
overlay1 = transpose(overlay1Og, overlay1)

# map matrix with asset value at each tile location
mainMap2Og = []
for i in range(int(sheight/(tileDim*tileScale))):
    temp = []
    for j in range(int(swidth/(tileDim*tileScale))):
        temp.append(random.randint(39,42))
    mainMap2Og.append(temp)

overlay2Og = [[-1]*(len(mainMap2Og[0])) for _ in range(len(mainMap2Og))]
#for i in range(len(mainMap2Og)):
#    for j in range(len(mainMap2Og[0])):
#        if mainMap2Og[i][j] in range(0,3):
#            overlay2Og[i][j] = 17
#overlay2Og[len(mainMap2Og)-1][len(mainMap2Og[0])-1] = 130

# transpose for RenderMap to read into for loops
mainMap2 = []
mainMap2 = transpose(mainMap2Og, mainMap2)

overlay2 = []
overlay2 = transpose(overlay2Og, overlay2)

collisionMap = [[1]*(len(mainMap1[0])+1) for _ in range(len(mainMap1)+1)]

for i in range(len(mainMap1)):
    for j in range(len(mainMap1[0])):
        if mainMap1[i][j] in range(39,43):
            collisionMap[i][j] = 0

mapWpx = len(mainMap1)*tileDim*tileScale
mapHpx = len(mainMap1[0])*tileDim*tileScale

playerTileIndex = [0,0]

def RenderLayer(mapOX, mapOY, grid, mapW, mapH):
    for x, i in enumerate(range(
        round(mapOX),
        round(mapOX)+mapW, 
        tileDim*tileScale
    )):
        for y, j in enumerate(range(
            round(mapOY),
            round(mapOY)+mapH,
            tileDim*tileScale
        )):
            # only render tiles within the game window
            if (
                (i > -tileDim*tileScale and i < swidth) and
                (j > -tileDim*tileScale and j < sheight) and
                grid[x][y] != -1
            ):
                screen.blit(tileList[grid[x][y]], (i,j))
    
def TestMap():
    centeringX = int((swidth-mapWpx)/2)
    centeringY = int((sheight-mapHpx)/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))

        for x, i in enumerate(range(
            centeringX, 
            centeringX+mapWpx, 
            tileDim*tileScale
        )):
            for y, j in enumerate(range(
                centeringY,
                centeringY+mapHpx,
                tileDim*tileScale
            )):
                screen.blit(tileList[mainMap1[x][y]], (i,j))
                if overlay1[x][y] != -1:
                    screen.blit(tileList[overlay1[x][y]], (i,j))

        pygame.display.update()
