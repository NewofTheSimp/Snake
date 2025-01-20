import pygame

class Move:
    def __init__(self, rect):
            self.rect = rect
            self.snake = [self.rect[0]]  # Initialize with the first cell
            self.index = 0
            self.last_move_time = 0  # Track the last move time
            self.move_delay = 200  # Delay in milliseconds (adjust as needed)

    def move(self, screen, direction):
        current_time = pygame.time.get_ticks()  # Get the current time
        if current_time - self.last_move_time > self.move_delay:  # Check if delay passed
            self.index += direction
            self.index = max(0, min(self.index, len(self.rect) - 1))  # Prevent out-of-bounds
            self.snake.append(self.rect[self.index])
            if len(self.snake) > 5:  # Keep snake length fixed
                self.snake.pop(0)
            self.last_move_time = current_time  # Update the last move time
        
        for s in self.snake:
            pygame.draw.rect(screen, "#9d8189", s)
        return self.index

    def moveAppend(self):
         self.snake.append(self.rect[self.index])

    def collSelf(self):
        head = self.snake[0] 
        for s in self.snake[1:]:  
            if head == s:  
                return True
        return False

    def collBorder(self, screen_width, screen_height):
        head = self.snake[-1]  # Head of the snake
        if (
            head.left < 0 or 
            head.right > screen_width or 
            head.top < 0 or 
            head.bottom > screen_height
        ):
            return True
        return False
             
            