import pygame, scene, player, gameobject, collectiblegameobject
from pygame.locals import *
 
class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 720, 720
        self.background = pygame.Surface(self.size)
        self.scenes = ["some_path", "some_other_path", "etc_you_get_the_idea"]
        self.current_scene = scene.Scene(self.scenes[0], player.Player(), [collectiblegameobject.CollectibleGameObject("key.png", 0, 0), gameobject.GameObject("bed.png", 150, 150), gameobject.GameObject("desk.png", 350, 300)])

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

       	self.background = self.background.convert()
       	self.background.fill((250, 250, 250))
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_logic(self):
        self.current_scene.get_sprites().update()
        collided_sprites = pygame.sprite.spritecollide(self.current_scene.get_player(), self.current_scene.get_sprites(), False)
        self.current_scene.get_player().update(collided_sprites)
        print len(collided_sprites)

    def on_render(self):
    	self._display_surf.blit(self.background, (0, 0))
    	self.current_scene.get_background().draw(self._display_surf)
    	self.current_scene.get_sprites().draw(self._display_surf)
    	pygame.display.flip()
        
    def on_cleanup(self): 
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.on_cleanup()
                else:
                    self.on_event(event)
                    self.current_scene.get_player().handle_input(event)
            self.on_logic()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()

