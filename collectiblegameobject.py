import gameobject

class CollectibleGameObject(gameobject.GameObject):

	def __init__(self, filename, x = 0, y = 0):
		gameobject.GameObject.__init__(self, filename, x, y)

	def interact(self):
		print "Interacting!"

