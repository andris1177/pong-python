import pygame
from pedal import *
from ball import *

class Pong():
    def __init__(self):
        self.screenWidth = 900
        self.screenHeight = 500
        self.fps = 60
        self.running = True
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.pedal1 = Pedal(1)
        self.pedal2 = Pedal(2)
        self.ball = Ball()
        self.run()

    def initPygame(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.text_font = pygame.font.SysFont("arial.ttf", 50)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Pong")
        self.pedal_sound = pygame.mixer.Sound("sounds/paddel.wav")
        self.score_sound = pygame.mixer.Sound("sounds/score.wav")

    def draw(self):
        self.screen.fill(self.black)
        self.screen.blit(self.player_score_text, (self.screenWidth/2 +40, 0))
        self.screen.blit(self.opponent_score_text, (self.screenWidth/2 -60, 0))
        pygame.draw.aaline(self.screen, self.white, (self.screenWidth/2, 0), (self.screenWidth/2, self.screenHeight))
        self.pedal1.draw(self.screen)
        self.pedal2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def checkCollision(self):
        if self.ball.getPos()[0] >= self.screenWidth:
            self.pedal2.addScore()
            pygame.mixer.Sound.play(self.score_sound)
            self.ball.resetBall()

        if self.ball.getPos()[0] <= 0:
            self.pedal1.addScore()
            pygame.mixer.Sound.play(self.score_sound)
            self.ball.resetBall()

        if (self.pedal1.getPosition()[0] - self.ball.getPos()[0]) * (self.pedal1.getPosition()[0] - self.ball.getPos()[0]) <= self.ball.getRadius() * self.ball.getRadius() and self.ball.getPos()[1] >= self.pedal1.getPosition()[1] and self.ball.getPos()[1] <= self.pedal1.getPosition()[1] + self.screenHeight / 4:
            self.ball.changeDirection()
            pygame.mixer.Sound.play(self.pedal_sound)

        if (self.pedal2.getPosition()[0] - self.ball.getPos()[0]) * (self.pedal2.getPosition()[0] - self.ball.getPos()[0]) <= self.ball.getRadius() * self.ball.getRadius() and self.ball.getPos()[1] >= self.pedal2.getPosition()[1] and self.ball.getPos()[1] <= self.pedal2.getPosition()[1] + self.screenHeight / 4:
            self.ball.changeDirection()
            pygame.mixer.Sound.play(self.pedal_sound)

    def moveOpponent(self):
        if self.ball.getPos()[1] > self.pedal2.getPosition()[1]:
            self.pedal2.move(2)

        if self.ball.getPos()[1] < self.pedal2.getPosition()[1]:
            self.pedal2.move(1)


    def mainLoop(self):
        while self.running:
            self.player_score_string = str(self.pedal1.getScore())
            self.player_score_text = self.text_font.render(self.player_score_string, 1, self.white)

            self.opponent_score_string = str(self.pedal2.getScore())
            self.opponent_score_text = self.text_font.render(self.opponent_score_string, 1, self.white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_UP]:
                self.pedal1.move(1)

            if self.keys[pygame.K_DOWN]:
                self.pedal1.move(2)

            self.draw()
            self.moveOpponent()
            self.checkCollision()
            self.ball.move()
            self.clock.tick(self.fps)

    def run(self):
        self.initPygame()
        self.mainLoop()
        pygame.quit()

game = Pong()