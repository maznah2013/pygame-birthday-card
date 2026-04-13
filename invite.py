import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600
CENTER_X=300
CENTER_Y=300

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Easter Invite!")

img1=pygame.image.load("bg1.jpg")
image1=pygame.transform.scale(img1, (WIDTH, HEIGHT))

running=True

while running:
    font1=pygame.font.SysFont("Comic Sans MS", 38)
    text1=font1.render("HAPPY EASTER!", True, ("#7871AA"))
    text1_rect=text1.get_rect(center=(CENTER_X, CENTER_Y-50))
    screen.fill("white")
    screen.blit(image1, (0,0))
    screen.blit(text1, text1_rect)
    pygame.display.update()
    time.sleep(3)

    img2=pygame.image.load("bg2.jpg")
    image2=pygame.transform.scale(img2, (WIDTH, HEIGHT))
    font2=pygame.font.SysFont("Indie Flower", 38)
    text2=font2.render("HOPE YOU HAVE A GREAT EASTER!", True, ("#AA9FB1"))
    text2_rect=text2.get_rect(center=(CENTER_X, CENTER_Y-50))
    screen.fill("white")
    screen.blit(image2, (0,0))
    screen.blit(text2, text2_rect)
    pygame.display.update()
    time.sleep(3)

    img3=pygame.image.load("bg3.jpg")
    image3=pygame.transform.scale(img3, (WIDTH, HEIGHT))
    font3=pygame.font.SysFont("Nunito", 38)
    text3=font3.render("WISHING YOU A WONDERFUL EASTER!", True, ("#C9B1BD"))
    text3_rect=text3.get_rect(center=(CENTER_X, CENTER_Y-50))
    screen.fill("white")
    screen.blit(image3, (0,0))
    screen.blit(text3, text3_rect)
    pygame.display.update()
    time.sleep(3)

pygame.quit()

