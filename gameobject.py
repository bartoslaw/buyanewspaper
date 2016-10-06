import pygame

class GameObject(pygame.sprite.Sprite):

	def __init__(self, filename, x = 0, y = 0, description = ""):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/" + filename)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.description = description

	def interact(self, callback):
		print self.description