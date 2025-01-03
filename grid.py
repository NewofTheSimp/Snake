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

        for i in self.y:
        
            v = pygame.Vector2(i,self.y[0])
            v2 = pygame.Vector2(i,self.y[-1])
            pygame.draw.line(screen, "red", (v), (v2))

        for i in self.x:
        
            v = pygame.Vector2(self.x[0], i)
            v2 = pygame.Vector2(self.x[-1], i)
            pygame.draw.line(screen, "red", (v), (v2))



            


