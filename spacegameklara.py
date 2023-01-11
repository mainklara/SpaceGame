import pygame
import os
from pygame.locals import *


pygame.init()

# FPS definieren
fps = pygame.time.Clock()

# Text als String bestimmen
text = ""

# Displaygröße einstellen
screen = pygame.display.set_mode((1366, 768))

# Titel für das Display festlegen
pygame.display.set_caption("IT Quizgame Alpha")

# Hintergrundbild festlegen
background = pygame.image.load('/Users/klaramueller/PycharmProjects/pythonProject/hintergrundspace.jpeg')
screen.blit(background, (0, 0))

# Größe der Planeten festlegen
planet1_width, planet1_height = 666, 450
planet2_width, planet2_height = 666, 375
planet3_width, planet3_height = 666, 375

# Bilder der Planeten raussuchen
planet1 = pygame.image.load('/Users/klaramueller/PycharmProjects/pythonProject/planet1.png')
planet1 = pygame.transform.scale(planet1, (planet1_width, planet1_height))
planet2 = pygame.image.load('/Users/klaramueller/PycharmProjects/pythonProject/planet2.png')
planet2 = pygame.transform.scale(planet2, (planet2_width, planet2_height))
planet3 = pygame.image.load('/Users/klaramueller/PycharmProjects/pythonProject/planet3.png')
planet3 = pygame.transform.scale(planet3, (planet3_width, planet3_height))

# Spielerposition und Spielerbewegung
VEL = 6

# Größe des Cursor festlegen
cursor_width, cursor_height = 60, 50

# Bild für den Cursor raussuchen
cursor = pygame.image.load('/Users/klaramueller/PycharmProjects/pythonProject/cursor.png')
cursor = pygame.transform.scale(cursor, (cursor_width, cursor_height))





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Position der Planeten festlegen
    screen.blit(planet1, (0, 0))
    screen.blit(planet2, (290, 80))
    screen.blit(planet3, (150, 300))

    # Position des Cursers
    screen.blit(cursor, (100, 100))


    # Bildschirm aktualisiert dauerhaft und FPS festgelegt
    pygame.display.flip()
    fps.tick(60)



pygame.quit()