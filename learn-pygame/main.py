import pygame
from sys import exit
from random import randint, choice
from player import Player
from obstacle import Obstacle
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
is_game_active = False
score = 0
start_time = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops=-1)

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphic/sky.png').convert()
ground_surface = pygame.image.load('graphic/ground.png').convert()
player_stand = pygame.transform.rotozoom(
    pygame.image.load('graphic/player/player_stand.png').convert_alpha(), 0, 2)
player_stand_rect = player_stand.get_rect(
    center=(SCREEN_WITH / 2, SCREEN_HEIGHT / 2))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


def display_score():
  current_time = int(pygame.time.get_ticks() / 1000) - start_time
  score_surface = game_font.render(f'{current_time}', False, (64, 64, 64))
  score_rect = score_surface.get_rect(center=(SCREEN_WITH / 2, 50))
  screen.blit(score_surface, score_rect)
  return current_time


def check_collisions():
  if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
    obstacle_group.empty()
    return False
  return True


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

    if is_game_active:
      if event.type == obstacle_timer:
        obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        is_game_active = True
        start_time = int(pygame.time.get_ticks() / 1000)

  if is_game_active:
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    score = display_score()
    player.draw(screen)
    player.update()
    obstacle_group.draw(screen)
    obstacle_group.update()
    is_game_active = check_collisions()
  else:
    screen.fill((94, 129, 162))
    screen.blit(player_stand, player_stand_rect)
    game_name = game_font.render("My game", False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center=(SCREEN_WITH / 2, 80))
    game_msg = game_font.render("Press space to run", False, (111, 196, 169))
    game_msg_rect = game_msg.get_rect(center=(SCREEN_WITH / 2, 320))
    score_msg = game_font.render(
        f'Your score: {score}', False, (111, 196, 169))
    score_msg_rect = score_msg.get_rect(center=(SCREEN_WITH / 2, 320))
    screen.blit(game_name, game_name_rect)
    if score == 0:
      screen.blit(game_msg, game_msg_rect)
    else:
      screen.blit(score_msg, score_msg_rect)

  pygame.display.update()
  clock.tick(60)
