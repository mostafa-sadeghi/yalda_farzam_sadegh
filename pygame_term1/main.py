import pygame

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cow_image = pygame.image.load("cow.png")
cow_rect = cow_image.get_rect(topleft=(0,0))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(cow_image, cow_rect)
    pygame.display.update()
