import random
import pygame
import os
from settings import SCREEN_WITDH, SCREEN_HEIGHT, root_dir, FRAME_RATE
from shape import Shape
from label import Label

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WITDH,SCREEN_HEIGHT))
pygame.display.set_caption("The rock-paper-scissors game")
choices = ["rock", "paper", "scissor"]

background = pygame.transform.scale(
    pygame.image.load(os.path.join(root_dir, 'assets', 'blue.png')).convert(),
    (SCREEN_WITDH,SCREEN_HEIGHT))

shape_group = pygame.sprite.Group()
shape_group.add([Shape("rock", location=(200,750)), 
                Shape("paper", location=(SCREEN_WITDH // 2, 750)), 
                Shape("scissor", location=(SCREEN_WITDH - 200, 750))])
player_status = Label(text="Player:", location=(200,50))
computer_status = Label(text="Computer:", location=(SCREEN_WITDH - 200,50))
restart_button = Label(text="Restart", location=(SCREEN_WITDH // 2,50))
status = Label(text="Let's play!", location=(SCREEN_WITDH // 2, SCREEN_HEIGHT // 2))
is_playing = False

win_conditions = {
    'rock': {'paper': 'Computer', 'scissor': 'Player'},
    'paper': {'scissor': 'Computer', 'rock': 'Player'},
    'scissor': {'rock': 'Computer', 'paper': 'Player'}
}

def update_all_status(status, computer_status, player_status):
    status.update()
    computer_status.update()
    player_status.update()

def main():
    player_point, computer_point = 0, 0
    while True:
        is_playing = True
        chosen_shape = Shape()
        computer_chosen_shape = Shape()
        while is_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button.text_rect.collidepoint(mouse_pos):
                        player_point, computer_point = 0, 0
                        shape_group.remove([chosen_shape, computer_chosen_shape])
                        computer_status.text = f'Computer: {computer_point}'
                        player_status.text = f'Player: {player_point}'
                        status.text = "Let's play!"
                        update_all_status(status, computer_status, player_status)
                        is_playing = False
                    clicked_shape = [s for s in shape_group if s.rect.collidepoint(mouse_pos)]
                    if not clicked_shape or not clicked_shape[0].is_clickable:
                        continue
                    else:
                        shape_group.remove([chosen_shape, computer_chosen_shape])
                        computer_choice = str(random.choice(choices))
                        chosen_shape = Shape(clicked_shape[0].type, location=(200, SCREEN_HEIGHT // 2), is_clickable=False)
                        computer_chosen_shape = Shape(computer_choice, location=(SCREEN_WITDH - 200, SCREEN_HEIGHT // 2), is_clickable=False)
                        shape_group.add(chosen_shape, computer_chosen_shape)
                        if clicked_shape[0].type == computer_choice:
                            status.text = "Draw!"
                        else:
                            winner = win_conditions[clicked_shape[0].type][computer_choice]
                            if winner == "Computer": computer_point += 1
                            if winner == "Player": player_point += 1
                            computer_status.text = f'Computer: {computer_point}'
                            player_status.text = f'Player: {player_point}'
                            status.text = f"{winner} wins!"
                        update_all_status(status, computer_status, player_status)

            screen.blit(background, (0,0))
            status.draw(screen)
            restart_button.draw(screen)
            computer_status.draw(screen)
            player_status.draw(screen)
            shape_group.draw(screen)
            shape_group.update()
            pygame.display.update()
            clock.tick(FRAME_RATE)

if __name__ == "__main__":
    main() 
