from pygame import font, surface

font.init()
game_font = font.Font('Pixeltype.ttf', 50)

class Label:
    def __init__(self, text = "", location = (0,0), foreground = (255,255,255)):
        self.text = text
        self.fg = foreground
        self.font = game_font
        self.text_surf = self.font.render(self.text, False, self.fg)
        self.text_rect = self.text_surf.get_rect(center = location)
    
    def draw(self, screen: surface.Surface):
        screen.blit(self.text_surf, self.text_rect)

    def update(self):
        self.text_surf = game_font.render(self.text, False, self.fg)
        self.text_surf.blit(self.text_surf, self.text_rect)