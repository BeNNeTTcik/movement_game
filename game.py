import pygame
import sys
#import cv2
import numpy as np
#import hailo

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 1792
screen_height = 1024
background = pygame.image.load("resources\\background.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movement")

# Platform dimensions
platform_width = 200
platform_height = 20
platform = pygame.Rect(350, 500, platform_width, platform_height)

#player dimensions
player_width = 50
player_height = 50

#layers 
back_layer = pygame.Surface((screen_width, screen_height))
back_layer.fill(background.get_at((0, 0)))  # Fill with the background color
mid_layer = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
top_layaer = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

# Set the frame rate
clock = pygame.time.Clock()

#screen.blit(background, (0, 0))
pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

pygame.quit()