import pygame
from random import choice, randint

WINDOW_WIDTH=480
WINDOW_HEIGHT=800
FRAMERATE=120

class BG(pygame.sprite.Sprite):
	def __init__(self,groups,scale_factor):
		super().__init__(groups)
		bg_image = pygame.image.load('./img/ambiente/background.png').convert()

		full_height = bg_image.get_height() * scale_factor
		full_width = bg_image.get_width() * scale_factor
		full_sized_image = pygame.transform.scale(bg_image,(full_width,full_height))
		
		self.image = pygame.Surface((full_width * 2,full_height))
		self.image.blit(full_sized_image,(0,0))
		self.image.blit(full_sized_image,(full_width,0))

		self.rect = self.image.get_rect(topleft = (0,0))
		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self,dt):
		self.pos.x -= 300 * dt
		if self.rect.centerx <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)
