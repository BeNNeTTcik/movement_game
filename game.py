import pygame
import sys
#import cv2
import numpy as np
#import hailo
from collision import is_collision
from lives import lives

#player
player = 300
player_speed = 0.5

#obstacle
obstacle = 200
obstacle_speed = 0.2

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Movement")

running = True
while running:
    if is_collision(player, 300, obstacle, 300):
        lives -= 1
        if lives ==0:   
            print("Collision!\nGame Over!")
            running = False
        else:
            player = 300
            obstacle = 200
    
    score +=1
    print("Score: ", score)
    print("Lives: ", lives)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #movement player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player -= player_speed
    if keys[pygame.K_DOWN]:
        player += player_speed        
        
    #movement obstacle
    obstacle += obstacle_speed
    if obstacle > 1900 or obstacle <= 0:
        obstacle_speed *= -1
            
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 255, 255), (100, player, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle, 300, 50, 50))
    
    pygame.display.update()
pygame.quit()

