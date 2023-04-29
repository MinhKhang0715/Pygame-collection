import pygame
import os
from settings import SCREEN_WITDH, IMAGE_SIZE_DEFAULT, root_dir

class Shape(pygame.sprite.Sprite):
    image_paths = {
        "rock": os.path.join(root_dir, 'assets', 'rock.png'),
        "paper": os.path.join(root_dir, 'assets', 'paper.png'),
        "scissor": os.path.join(root_dir, 'assets', 'scissor.png')
    }
    def __init__(self, type: str = "rock", location = (0,0)):
        super().__init__()
        self.__type = type
        self.location = location
        self.image = pygame.transform.scale(
            pygame.image.load(Shape.image_paths[type]).convert_alpha(),
            (IMAGE_SIZE_DEFAULT, IMAGE_SIZE_DEFAULT))
        self.rect = self.image.get_rect(midbottom=self.location)
    
    @property
    def type(self):
        return self.__type

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)
