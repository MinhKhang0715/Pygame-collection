from pygame import sprite, image as pyimage
from random import randint


class Obstacle(sprite.Sprite):
  def __init__(self, type: str):
    super().__init__()
    if type == 'fly':
      fly_frame_1 = pyimage.load('graphic/fly/Fly1.png').convert_alpha()
      fly_frame_2 = pyimage.load('graphic/fly/Fly2.png').convert_alpha()
      self.frames = [fly_frame_1, fly_frame_2]
      y_pos = 210
    else:
      snail_frame_1 = pyimage.load('graphic/snail/snail1.png').convert_alpha()
      snail_frame_2 = pyimage.load('graphic/snail/snail2.png').convert_alpha()
      self.frames = [snail_frame_1, snail_frame_2]
      y_pos = 300

    self.animation_index = 0
    self.image = self.frames[self.animation_index]
    self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

  def animation(self):
    self.animation_index += 0.1
    if self.animation_index >= len(self.frames):
      self.animation_index = 0
    self.image = self.frames[int(self.animation_index)]

  def destroy(self):
    if self.rect.x <= -100:
      self.kill()

  def update(self):
    self.animation()
    self.rect.x -= 6
    self.destroy()
