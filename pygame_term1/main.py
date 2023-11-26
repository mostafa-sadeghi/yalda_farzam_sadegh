import pygame

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cow_image = pygame.image.load("cow.png")
cow_rect = cow_image.get_rect(bottomright=(SCREEN_WIDTH,SCREEN_HEIGHT))

font72 = pygame.font.Font("myfont.otf",72)
font32 = pygame.font.Font("myfont.otf",32)

title_text = font32.render("Cow Game", True, (240,30,197))
title_rect = title_text.get_rect(centerx = SCREEN_WIDTH/2 , top = 0)
# یک متغیر برای امتیاز تعریف کنید و در قسمت بالا و چپ صفحه نمایش دهید
# یک متغیر برای جان گاو تعریف کنید و در بالا و سمت راست صفحه قرار دهید

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # cow movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and cow_rect.top > 0:
        cow_rect.y -= 5
    if keys[pygame.K_DOWN] and cow_rect.bottom < SCREEN_HEIGHT:
        cow_rect.y += 5

    screen.fill((0,0,0))
    screen.blit(cow_image, cow_rect)
    screen.blit(title_text, title_rect)
    pygame.display.update()
    clock.tick(FPS)
