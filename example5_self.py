class Car:
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
Honda = Car()
carname = input("car name: ")
Honda.setName(carname)
print("Honda car name:", Honda.getName())
