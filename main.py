import pygame
from sys import exit
from random import choice

from classes import Player, Obstacle
from functions.helpers import collision_sprite, display_score, display_text

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
pixel_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

# Music
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Background
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

# Intro screen
player_stand = pygame.image.load(
    "graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(
                    Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        score_surf, score_rect, score = display_score(start_time, pixel_font)
        pygame.draw.rect(screen, "#c0e8ec", score_rect)
        screen.blit(score_surf, score_rect)

        # Player
        player.draw(screen)
        player.update()

        # Obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collision
        game_active = collision_sprite(player, obstacle_group)

    else:
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)

        if score:
            display_text(f'Score: {score}', (400, 50), pixel_font, screen)
        else:
            display_text("Runner", (400, 50), pixel_font, screen)

        display_text("Press space to play", (400, 350), pixel_font, screen)

    pygame.display.update()
    clock.tick(60)
