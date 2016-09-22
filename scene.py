import pygame, player, gameobject

class Scene:
	def __init__(self, scene_path, player, scene_objects):
		self.scene_path = scene_path

		self.background = pygame.sprite.Sprite()
		self.background.image = pygame.image.load("assets/background.jpg")
		self.background.rect = self.background.image.get_rect()
		
		self.player = player;
		self.scene_objects = scene_objects

		self.scene_background = pygame.sprite.RenderPlain(self.background)
		self.scene_sprites = pygame.sprite.RenderPlain(self.player, self.scene_objects)

	def get_background(self):
		return self.scene_background

	def get_sprites(self):
		return self.scene_sprites

	def get_player(self):
		return self.player


