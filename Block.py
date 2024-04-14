import pygame as pygame

class Block:
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 95
        self.height = 20
        self.color = (255, 255, 255)
        self.points = 1
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.screen = screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def destroy(self):
        print("Brick Destroyed")
        return self.points

class RedBlock:
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 95
        self.height = 20
        self.color = (200, 50, 50)
        self.points = 2
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.screen = screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def destroy(self):
        print("Red Block Destroyed")
        return self.points
    
    def hit(self):
        self.color = (50, 50, 200)