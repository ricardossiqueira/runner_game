import pygame


def collision_sprite(player, obstacle_group):
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


def display_score(start_time, font):
    score = pygame.time.get_ticks() // 1000 - start_time
    score_surf = font.render(f"Score: {score}", False, "#333333")
    score_rect = score_surf.get_rect(midright=(750, 50))
    return score_surf, score_rect, score


def display_text(text, pos, font, screen):
    text_surf = font.render(text, False, "#333333")
    text_rect = text_surf.get_rect(center=pos)
    screen.blit(text_surf, text_rect)