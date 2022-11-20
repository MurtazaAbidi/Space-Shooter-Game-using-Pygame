import pygame
import random
from pygame import mixer

mixer.init()
mixer.music.load('Background.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("ihi Game Assignment")
gameOver = False
bar_x, bar_y = 200 , 400
shoot = bar_y
enemy_x, enemy_y = 10 , 50
enemy_direction_x, enemy_direction_y = 1 , 1

background = pygame.image.load ('background.png')
spaceship = pygame.image.load('spaceShip.png')

score = 0
life = 3
enemy_speed = 1

moveBarLeft = False
moveBarRight = False
launch_fire = False
HardMode = False

fnt = pygame.font.SysFont('Arial', 40)

while not gameOver: 
    screen.blit (background, (0,0))
    pygame.time.Clock().tick(900)


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameOver = True
        if e.type == pygame.KEYUP or e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                moveBarLeft = not moveBarLeft
            elif e.key == pygame.K_RIGHT:
                moveBarRight = not moveBarRight
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and launch_fire==False:
            launch_fire = True
            bullet_location = bar_x+21
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Shoot.mp3'))

    if moveBarLeft == True and bar_x>=5:
        bar_x -= 3
    elif moveBarRight == True and bar_x < 795-50:
        bar_x += 3
    if launch_fire == True:
        shoot-= 5
    else:
        bullet_location = bar_x+21

    enemy_x += enemy_direction_x*enemy_speed
    if HardMode: enemy_y += enemy_direction_y*enemy_speed
 
    if enemy_x<10 or enemy_x>750:
        enemy_direction_x*=-1
    if enemy_y<50 or enemy_y>100:
        enemy_direction_y*=-1
    if enemy_y >= 375:
        gameOver = True
    
    enemy_rt = pygame.Rect(enemy_x, enemy_y, 30, 30)
    fire_rt = pygame.Rect(bullet_location, shoot, 10, 30)

    if enemy_rt.colliderect(fire_rt):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('collision.mp3'))
        enemy_x = random.randint(10,550)
        enemy_direction_x = 1
        score+=1
        launch_fire = False
        shoot = bar_y
        enemy_speed += 0.25
        if score==3:
            HardMode = True
            
    elif shoot <= 0:
        shoot = bar_y
        life-=1
        launch_fire = False
        if life == 0:
            gameOver = True
    pygame.draw.ellipse(screen, (255,255,255), enemy_rt, 0)
    pygame.draw.ellipse(screen, (255,255,255), fire_rt, 0)
    score_txt = fnt.render (f'Score= {score}', True, (0,250,0))
    life_txt = fnt.render (f'Life= {life}', True, (0,250,0))
    instrct = fnt.render ('Shooting Game', True, (255,255,255))
    screen.blit (score_txt, (10,10))
    screen.blit (instrct, (300,5))
    screen.blit (life_txt, (650,10))
    screen.blit (spaceship, (bar_x+1,bar_y-2))
    pygame.display.update()

mixer.music.stop()
mixer.music.load('GameOver.mp3')

mixer.music.set_volume(0.6)
mixer.music.play()
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    gameOver_rect = pygame.Rect(225, 125, 300, 225)
    screen.blit (background, (0,0))
    gameover_txt = fnt.render(f'Game Over', True, (255,255,255))
    score_txt = fnt.render(f'Your Score = {score}', True, (255,255,255))
    screen.blit (gameover_txt, (300, 150))
    screen.blit (score_txt, (275, 250))

    pygame.draw.rect(screen, (0,0,0), gameOver_rect, 5 )
    
    pygame.display.update()
    
mixer.music.stop()