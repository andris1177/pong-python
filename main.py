import pygame
import random

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

height = 500
width = 900
black = (0, 0, 0)
white = (255, 255, 255)
speed = 10
fps = 60

player_score = 0
opponent_score = 0

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
vona_speed = 7

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

text_font = pygame.font.SysFont("arial.ttf", 50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(width/2 -15, height/2 -15, 30, 30)
player = pygame.Rect(width -20, height /2 -70, 10, 140)
opponent = pygame.Rect(10,height/2 - 70, 10, 140)


running = True
while running:
    player_score_string = str(player_score)
    text_player = text_font.render(player_score_string, 1, white)

    opponent_score_string = str(opponent_score)
    text_opponent = text_font.render(opponent_score_string, 1, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7

            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7

            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(black)
    screen.blit(text_player, (width/2 +40, 0))
    screen.blit(text_opponent, (width/2 -60, 0))
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width/2, 0), (width/2, height))

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
