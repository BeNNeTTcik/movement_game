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
background_color = pygame.image.load("resources\\background.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movement")

# Set the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (black in this case)
    #screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)