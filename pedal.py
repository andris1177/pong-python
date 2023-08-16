import pygame

class Pedal():
    def __init__(self, side):
        self.side = side
        self.screenWidth = 900
        self.screenHeight = 500
        self.width = 10
        self.height = 140
        self.speed = 6
        self.score = 0
        self.white = (255, 255, 255)
        self.y = self.height / 2 - 15
        if side == 1:
            self.x = 5

        if self.side == 2:
            self.x = self.screenWidth - 15

    def draw(self, screen):
        pygame.draw.rect(screen, self.white, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == 1:
            self.y -= self.speed

        if direction == 2:
            self.y += self.speed

        if self.y + 140 >= self.screenHeight:
            self.y = self.screenHeight - 140

        if self.y <= 0:
            self.y = 0


    def getScore(self):
        return self.score

    def addScore(self):
        self.score += 1

    def getPosition(self):
        return self.x, self.y