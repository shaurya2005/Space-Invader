import pygame
import random
import math
from  pygame import  mixer

# Initialise pygame

pygame.init()

# Display screen
screen = pygame.display.set_mode((800, 800))

# Background
background = pygame.image.load('2352.jpg')

# Title and logo
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('halloween.png')
pygame.display.set_icon(icon)
backgroundd=mixer.Sound('background.wav')
backgroundd.play(-1)
# Player
PlayerImg = pygame.image.load('gaming.png')
playerX = 370.0
playerY = 680.0
player_change = 0

# Enemy
enemyImg =[]
enemyX = []
enemyY =[]
enemyX_change = []
enemyY_change = []
for i in range(6):
    enemyImg.append(pygame.image.load('transportation.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(100.0)
    enemyX_change.append(6)
    enemyY_change.append(50)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 680
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

gameover="Gameover"
ffont=pygame.font.Font('freesansbold.ttf',344)
texttX=200
ttextY=400

over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x,y):
    score=font.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))
def game_over(x,y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 0))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y,):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def detect_colission(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX - bulletX),2)) + math.pow((enemyY - bulletY),2))

    if distance <= 27:
        return True
    else:
        return False


# Events


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -9
            if event.key == pygame.K_RIGHT:
                player_change = 9
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            player_change = 0

    playerX += player_change

    # Player boundary
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)

        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"


    # Enemy boundary
    for i in range(6):

        if enemyY[i]>600:
            for j in range(6):

                enemyY[j]=2000
            game_over(texttX,ttextY)
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 9
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 735:
            enemyX_change[i] = -9
            enemyY[i] += enemyY_change[i]
        collision=detect_colission(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collisionn=mixer.Sound('explosion.wav')
            collisionn.play()
            # bulletY[i]=680
            bullet_state="ready"
            laser=mixer.Sound('laser.wav')
            laser.play()
            bulletY=680
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = 100.0
            score_value+=1

        enemy(enemyX[i], enemyY[i],i)
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
