import pygame
import time

pygame.init
pygame.mixer.music.load('a horror-sinister-power-rising-epic-dark- soundtracknocopyrightmusic98837.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)