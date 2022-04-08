import pygame
import random as rd

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
clock.tick(10)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("while true: learn")

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

trash_speed = 1
timer = 0

can = pygame.image.load('can.png')
can = pygame.transform.scale(can, (50, 50))

playerImg = pygame.transform.scale(playerImg, (64, 100))

score = 0

running = True

items = []

timer = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def trash(x, y, item):
    screen.blit(item, (x, y))

while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    if timer < 300:
        timer += 1
    else:
        items.append({"x": rd.randint(20, 380), "y": 0})
        timer = 0
    for item in items:
        if item["y"] >= 800:
            items.remove(item)
        trash(item["x"], item["y"], can)
        item["y"] += trash_speed
        if abs(item["x"] - playerX) < 20 and abs(item["y"] - playerY) < 30:
            score += 1
            items.remove(item)

    player(playerX, playerY)
    text_surface = myfont.render("Puszki: " + str(score), False, (255, 255, 255))
    screen.blit(text_surface, (300, 30))
    timer += 1
    pygame.display.update()import pygame
import random as rd

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
clock.tick(10)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("while true: learn")

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

trash_speed = 1
timer = 0

can = pygame.image.load('can.png')
can = pygame.transform.scale(can, (50, 50))

playerImg = pygame.transform.scale(playerImg, (64, 100))

score = 0

running = True

items = []

timer = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def trash(x, y, item):
    screen.blit(item, (x, y))

while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    if timer < 300:
        timer += 1
    else:
        items.append({"x": rd.randint(20, 380), "y": 0})
        timer = 0
    for item in items:
        if item["y"] >= 800:
            items.remove(item)
        trash(item["x"], item["y"], can)
        item["y"] += trash_speed
        if abs(item["x"] - playerX) < 20 and abs(item["y"] - playerY) < 30:
            score += 1
            items.remove(item)

    player(playerX, playerY)
    text_surface = myfont.render("Puszki: " + str(score), False, (255, 255, 255))
    screen.blit(text_surface, (300, 30))
    timer += 1
    pygame.display.update()