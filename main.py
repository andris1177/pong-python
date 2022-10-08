#import
import pygame
import random

#függvények
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x 
    ball.y += ball_speed_y 

    if ball.top <=0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.left <=0:
        ball_reset()
        player_score += 1

    if ball.right >= width:
        ball_reset()
        opponent_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0

    if player.bottom >= height:
        player.bottom = height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += vona_speed
    
    if opponent.bottom > ball.y:
        opponent.bottom -= vona_speed

    if opponent.top <= 0:
        opponent.top = 0
        
    if opponent.bottom >= height:
        opponent.bottom = height

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center =(width/2, height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#változók
height = 500
width = 900
black = (0, 0, 0)
white = (255, 255, 255)
speed = 10
fps = 60

#pontok
player_score = 0
opponent_score = 0

#labda
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
vona_speed = 7

#pygame inicializálása
pygame.init()
pygame.font.init()

#az óra beállítása fps korlátozás miatt
clock = pygame.time.Clock()

#az eredmény kiírása
text_font = pygame.font.SysFont("arial.ttf", 50)

#ablak létrehozás és title
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

#kijelzőre rajzolt elemek
ball = pygame.Rect(width/2 -15, height/2 -15, 30, 30)
player = pygame.Rect(width -20, height /2 -70, 10, 140)
opponent = pygame.Rect(10,height/2 - 70, 10, 140)


#fő ciklus
running = True
while running:
    player_score_string = str(player_score)
    text_player = text_font.render(player_score_string, 1, white)

    opponent_score_string = str(opponent_score)
    text_opponent = text_font.render(opponent_score_string, 1, white)

    #figyeli a billentyúzet-et
    for event in pygame.event.get():
        #kilépés
        if event.type == pygame.QUIT:
            running = False

        #ha a billenytű le van nyomvba
        if event.type == pygame.KEYDOWN:
            #le
            if event.key == pygame.K_DOWN:
                player_speed += 7

            #fel
            if event.key == pygame.K_UP:
                player_speed -= 7

        #ha nincs lenyomva
        if event.type == pygame.KEYUP:
            #nem menjen tovább
            if event.key == pygame.K_DOWN:
                player_speed -= 7

            #nem menjen tovább
            if event.key == pygame.K_UP:
                player_speed += 7

    #függvények meghívása
    ball_animation()
    player_animation()
    opponent_animation()

    #kijelző kitőltése krakterekkel
    screen.fill(black)
    screen.blit(text_player, (width/2 +40, 0))
    screen.blit(text_opponent, (width/2 -60, 0))
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width/2, 0), (width/2, height))

    #kijelzőre rajzolás
    pygame.display.flip()

    #fps beállítása 60-ra
    clock.tick(fps)

#kilép a pygame-ből
pygame.quit()
