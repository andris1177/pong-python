from random import choice
import pygame

class Ball:
    def __init__(self):
        self.screenWidth = 900
        self.screenHeight = 500
        self.x = self.screenWidth / 2
        self.y = self.screenHeight /2
        self.speed = 6
        self.speedX = self.speed * choice((-1, 1))
        self.speedY = self.speed * choice((-1, 1))
        self.radius = 20
        self.white = (255, 255, 255)
        pygame.mixer.init()
        self.wall_sound = pygame.mixer.Sound("sounds/wall.wav")


    def draw(self, screen):
        pygame.draw.circle(screen, self.white, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

        if self.y+20 >= self.screenHeight or self.y-20 <= 0:
            self.speedY *= -1
            pygame.mixer.Sound.play(self.wall_sound)

    def resetBall(self):
        self.x = self.screenWidth / 2
        self.y = self.screenHeight /2
        self.speedX = self.speed * choice((-1, 1))
        self.speedY = self.speed * choice((-1, 1))

    def getPos(self):
        return self.x, self.y
    
    def changeDirection(self):
        self.speedX *= -1
        self.speedY *= -1

    def getRadius(self):
        return self.radius