import pygame

class Move:
    rect = []
    snake = []
    index = 0

    def __init__(self, rect):
        self.rect = rect

    def moveRight(self, screen):
        pygame.time.delay(1000)
        self.index += 1
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake = self.snake[1:]

    def moveLeft(self, screen):
        pygame.time.delay(1000)
        self.index -= 1
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake.pop()

    
    def moveDown(self, screen):
        pygame.time.delay(1000)
        self.index += 21
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake.pop()


    def moveUp(self, screen):
        pygame.time.delay(1000)
        self.index -= 21
        self.snake.append(self.rect[self.index])
        for s in self.snake:
            pygame.draw.rect(screen, "blue", s, 1)
        self.snake.pop()

        