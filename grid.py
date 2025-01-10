import pygame

class Grid:
    x = []
    y = []
    sw = 0
    sh = 0

    def __init__(self, sw,sh):
        self.sw = sw
        self.sh = sh

    def DrawGrid(self, screen):
        swGrid = self.sw / 20
        shGrid = self.sh / 20
        stepX = 0
        stepY = 0

        while stepX <= self.sw:
    
            self.x.append(stepX)
            stepX += swGrid

        while stepY <= self.sh:

            self.y.append(stepY)
            stepY += shGrid
        rectArr = []
        for y in self.y:
            for x in self.x:
                rect = pygame.Rect(x, y,swGrid, shGrid)
                pygame.draw.rect(screen, "red", rect, 1)
                rectArr.append(rect)
        return rectArr
    

        

            


