import pygame

class Move:
    rect = []
    snake = []
    index = 0

    def __init__(self, rect):
        self.rect = rect

        
    def move(self, screen, direction):
        self.index += direction
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]
  
