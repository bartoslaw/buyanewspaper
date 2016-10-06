import pygame, math, collectiblegameobject
from collections import namedtuple

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/player.png")
		self.original_image = self.image

		self.rect = self.image.get_rect()
		self.speed = 5
		self.dx = 0
		self.dy = 0
		self.is_interacting = False

	def handle_input(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				self.dy = -self.speed
				self.rotate(90)
			if event.key == pygame.K_s:
				self.dy = self.speed
				self.rotate(270)
			if event.key == pygame.K_a:
				self.dx = -self.speed
				self.rotate(180)
			if event.key == pygame.K_d:
				self.dx = self.speed
				self.rotate(0)
			if event.key == pygame.K_e:
				self.is_interacting = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				self.dy = 0
			if event.key == pygame.K_s:
				self.dy = 0
			if event.key == pygame.K_a:
				self.dx = 0
			if event.key == pygame.K_d:
				self.dx = 0
			if event.key == pygame.K_e:
				self.is_interacting = False

	def update(self, collided_sprites = []):
		self.handle_collision(self.dx, self.dy, collided_sprites)
		if self.is_interacting:
			for target in collided_sprites:
				if target != self and isinstance(target, collectiblegameobject.CollectibleGameObject):
					target.interact() #to think of a better way

	def rotate(self, angle = 90):
		self.image, self.rect = self.rot_center(angle)

	def rot_center(self, angle = 90):
		self.rot_image = pygame.transform.rotate(self.original_image, angle)
		self.rot_rect = self.rot_image.get_rect(center = self.rect.center)
		return self.rot_image, self.rot_rect

	def handle_collision(self, dx, dy, collided_sprites = []):
		for other in collided_sprites:
			if other != self and not isinstance(other, collectiblegameobject.CollectibleGameObject):
				(awayDx, awayDy) = self.move_after_collision(other, -1)
				resistance = self.speed * 2
				dx = dx + resistance * (awayDx)
				dy = dy + resistance * (awayDy)
		self.rect.move_ip(dx, dy)

	def move_after_collision(self, other, speed):                                   
		dx = other.rect.x - self.rect.x
		dy = other.rect.y - self.rect.y
		if abs(dx) > abs(dy):
			if dx > 0:
				return (+speed, 0)
			else:
				return (-speed, 0)
		else:
			if dy > 0:
				return (0, +speed)
			else:
				return (0, -speed)


  
			
