#!/usr/bin/python3

# Python 3 project to learn the fundamentals of pygame
# Author David A

import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Create Window
window = pygame.display.set_mode((800, 600))

# Background
# https://www.freepik.com/free-photos-vectors/star created by vectorpouch
background = pygame.image.load('bg1.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders By David A")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)  # "Icon made by Freepik from www.flaticon.com"

# Player
# "Icon made by Eucalyp from www.flaticon.com"
player_img = pygame.image.load('spacecraft1.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
# "Icon made by freepik from www.flaticon.com"
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 20

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('ufo.png'))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(2)
    enemy_y_change.append(40)

# Bullet
# Ready - the bullet is hidden on the screen
# Fire - the bullet is in motion
# "Icon made by freepik from www.flaticon.com"
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bellet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 10
score_y = 10

# Game Over Text
go_font = pygame.font.Font('freesansbold.ttf', 64)

# Renders the score with font and color to the window
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

# Renders Game Over text with font and color to the window
def game_over():
    end = go_font.render("GAME OVER...", True, (255, 255, 255))
    window.blit(end, (200, 250))

# Sets the position of the player with x and y cordinates
def player(x, y):
    window.blit(player_img, (x, y))


# Sets the position of the enemy with x and y cordinates
def enemy(x, y, i):
    window.blit(enemy_img[i], (x, y))

# Sets the position of the bullet with x and y cordinates
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (x + 16, y + 10))

# Detects collsion between enemy and bullet
def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) +
                         (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Listen for keystroke event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            if event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_SPACE:
                
                if bullet_state is "ready":
                    laser = pygame.mixer.Sound('laser.wav')
                    laser.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    # RGB BG color
    window.fill((50, 50, 50))

    # Background Image
    window.blit(background, (0, 0))

    # Checking boundries of player and enemy
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for i in range(num_of_enemies):

        # Game Over
        if enemy_y[i] > 440:
            for x in range(num_of_enemies):
                enemy_y[x] = 2000
            game_over()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -2
            enemy_y[i] += enemy_y_change[i]

        #  Bullet hit enemy
        hit = collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if hit:
            contact = mixer.Sound('explosion.wav')
            contact.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

   



    player(player_x, player_y)
    show_score(score_x, score_y)
    pygame.display.update()
