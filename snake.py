# Example file showing a basic pygame "game loop"
import pygame
import grid
import move
import colllision

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
g = grid.Grid(500,500)
rectArr = g.DrawGrid(screen)
m = move.Move(rectArr)
c = colllision.Coll(rectArr)
direction = 1
c.generateBait(screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#d8e2dc")

    # RENDER YOUR GAME HERE
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = -21 
    if keys[pygame.K_s]:
        direction = 21
    if keys[pygame.K_a]:
        direction = -1
    if keys[pygame.K_d]:
        direction = 1
    i = m.move(screen, direction)
    c.generateBait(screen)
    if c.baitColl(i):
        m.moveAppend()      
    if  m.collSelf():
         running = False

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()