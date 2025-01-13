import pygame

class Move:
    rect = []
    snake = []
    index = 0

    def __init__(self, rect):
        self.rect = rect

        
    def move(self, screen, index):
        self.index += index
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]


    def moveRight(self, screen):
        self.index += 1
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]

    def moveLeft(self, screen):
        self.index -= 1
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]

    
    def moveDown(self, screen):
        self.index += 21
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]


    def moveUp(self, screen):
        self.index -= 21
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]

        