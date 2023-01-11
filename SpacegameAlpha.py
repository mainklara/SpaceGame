import pygame
from pygame.locals import *
import os

pygame.init()

# FPS definieren
fps = pygame.time.Clock()

# Text der im Display erscheint als String definiert
text = ""

# Displaygröße einstellen
width = 798
height = 499
screen = pygame.display.set_mode((width, height))

# Titel für das Display festlegen
pygame.display.set_caption("IT Quizgame Alpha")

# Hintergrundbild festlegen
#background = pygame.image.load(os.path.join('Assets', 'backgroundquiz.jpg'))
#for element in range(1, 120, 1):
frame = 0
background1 = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/animatedstars1.png'))
background2 = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/animatedstars2.png'))
background1 = pygame.transform.scale(background1, (798, 499))
background2= pygame.transform.scale(background2, (798, 499))



# Größe der Planeten festlegen
planet1_width, planet1_height = 666, 500
planet2_width, planet2_height = 400, 220
regenbogen_width, regenbogen_height = 333, 187.5
diskokugel_width, diskokugel_height = 200, 240

# Bild der Planeten raussuchen
planet1 = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/planet1.png'))
planet1 = pygame.transform.scale(planet1, (planet1_width, planet1_height))
planet2 = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/computer1.png'))
planet2 = pygame.transform.scale(planet2, (planet2_width, planet2_height))
regenbogen = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/regenbogen.png'))
regenbogen = pygame.transform.scale(regenbogen, (regenbogen_width, regenbogen_height))
diskokugel = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/diskokugel.png'))
diskokugel = pygame.transform.scale(diskokugel, (diskokugel_width, diskokugel_height))

# Spielerposition und Spielerbewegung
VEL = 6

# Curser Größe festgelegt
cursor_width, cursor_height = 60, 50


# Bild des Cursers raussuchen
cursor = pygame.image.load(os.path.join('/Users/klaramueller/PycharmProjects/pythonProject/curser.png'))
cursor = pygame.transform.scale(cursor, (cursor_width, cursor_height))

# Richtunge für den cursor definieren
richtung_a = pygame.transform.rotate(pygame.transform.scale(cursor, (cursor_width, cursor_height)), 0)
richtung_b = pygame.transform.rotate(pygame.transform.scale(cursor, (cursor_width, cursor_height)), 90)
richtung_c = pygame.transform.rotate(pygame.transform.scale(cursor, (cursor_width, cursor_height)), 180)
richtung_d = pygame.transform.rotate(pygame.transform.scale(cursor, (cursor_width, cursor_height)), 270)
richtung_e = pygame.transform.rotate(pygame.transform.scale(cursor, (cursor_width, cursor_height)), 45)

# Keine Ahnung das muss anscheinend so
cursorposition =  pygame.Rect(100, 300, cursor_width, cursor_height)



# Schleife für das Programm
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Bewegung des cursors
    keys_pressed = pygame.key.get_pressed()
    rotate = pygame.transform.rotate
    if keys_pressed[pygame.K_DOWN] and cursorposition.y < height - 40:
        cursor = richtung_c
        cursorposition.y += VEL
    if keys_pressed[pygame.K_UP] and cursorposition.y > height - 510:
        cursor = richtung_a
        cursorposition.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and cursorposition.x < width - 41:
        cursor = richtung_d
        cursorposition.x += VEL
    if keys_pressed[pygame.K_LEFT] and cursorposition.x > width - 805:
        cursor = richtung_b
        cursorposition.x -= VEL

    # Unterprogramm für den Computer

    frame += 1


    if frame < 60:
        background = background1
    if frame >= 60:
        background = background2
    if frame == 120:
        frame = 0

    screen.blit(background, (0, 0))


    # Position der Planeten festlegen
    screen.blit(planet1, (0, 0))
    screen.blit(planet2, (440, 260))
    screen.blit(regenbogen, (130, 300))
    screen.blit(diskokugel, (390, 40))

    # Position des Cursers
    screen.blit(cursor, (cursorposition.x, cursorposition.y))

    # Bildschirm dauerhaft aktualisieren und FPS festgelegt
    pygame.display.flip()
    fps.tick(60)






pygame.quit()