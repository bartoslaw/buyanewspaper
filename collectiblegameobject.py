import gameobject

class CollectibleGameObject(gameobject.GameObject):

	def __init__(self, filename, x = 0, y = 0, description = "", kind = ""):
		gameobject.GameObject.__init__(self, filename, x, y, description)
		self.kind = kind

	def interact(self, callback):
		gameobject.GameObject.interact(self, callback)
		callback(self.kind)
		self.kill()

