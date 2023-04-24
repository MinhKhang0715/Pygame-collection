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
computer_status = Label(text="Player:", location=(200,50))
player_status = Label(text="Computer:", location=(SCREEN_WITDH - 200,50))
status = Label(text="Let's play!", location=(SCREEN_WITDH // 2, SCREEN_HEIGHT // 2))
is_playing = False

win_conditions = {
    'rock': {'paper': 'Computer', 'scissor': 'Player'},
    'paper': {'scissor': 'Computer', 'rock': 'Player'},
    'scissor': {'rock': 'Computer', 'paper': 'Player'}
}

def main():
    while True:
        chosen_shape = Shape()
        computer_chosen_shape = Shape()
        is_playing = True
        while is_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_shape = [s for s in shape_group if s.rect.collidepoint(mouse_pos)]
                    if len(clicked_shape) == 0:
                        continue
                    else:
                        computer_choice = str(random.choice(choices))
                        chosen_shape = Shape(clicked_shape[0].type, location=(200, SCREEN_HEIGHT // 2))
                        computer_chosen_shape = Shape(computer_choice, location=(SCREEN_WITDH - 200, SCREEN_HEIGHT // 2))
                        if clicked_shape[0].type == computer_choice:
                            status.text = "Draw!"
                        else:
                            winner = win_conditions[clicked_shape[0].type][computer_choice]
                            status.text = f"{winner} wins!"
                        status.update()

            screen.blit(background, (0,0))
            status.draw(screen)
            computer_status.draw(screen)
            player_status.draw(screen)
            chosen_shape.draw(screen)
            computer_chosen_shape.draw(screen)
            shape_group.draw(screen)
            shape_group.update()
            pygame.display.update()
            clock.tick(FRAME_RATE)

if __name__ == "__main__":
    main() 
