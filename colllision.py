import pygame
import random

class Coll:
    arr = []
    r = 0
    def __init__(self, arr):
        self.arr = arr
        self.r = random.randint(0, len(self.arr))


    def baitColl(self, index):
        if index == self.r:
            self.r = random.randint(0, len(self.arr))
            return True
        else:
            return False
        
    def generateBait(self, screen):
        pygame.draw.rect(screen, "#f4acb7", self.arr[self.r])



