import pygame
from game import player, obstacle

def is_collision(player, obstacle):
    distance = ((player - obstacle)**2 + (player - obstacle)**2) ** 0.5
    return distance < 50