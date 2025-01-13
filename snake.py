# Example file showing a basic pygame "game loop"
import pygame
import grid
import move

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
g = grid.Grid(500,500)
rectArr = g.DrawGrid(screen)
m = move.Move(rectArr)
index = 0
direction = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    
    # Event handling (key presses)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = -1
            elif event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_UP:
                direction = -21
            elif event.key == pygame.K_DOWN:
                direction = 21
    index += direction
    m.moveDown(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()