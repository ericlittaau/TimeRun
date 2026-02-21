import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(50, 500)
player_speed = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_a]:
        player_pos.x -= player_speed
    if keys [pygame.K_d]:
        player_pos.x += player_speed
    screen.fill("brown")
    pygame.draw.rect(screen, "blue", (player_pos.x, player_pos.y, 40, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()