import pygame
import time

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("ex21.mp3")
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
while pygame.mixer.music.get_busy():
    time.sleep(1)
