class Car:
	def __init__(self,price,fuel,speed,mileage):
		self.price =price
		self.fuel = fuel
		self.speed = speed
		self.mileage = mileage
		self.display_all()

	def display_all(self):
		print("Price: " + str(self.price) + "\n"+ "Speed: " + str(self.fuel) + "\n" + "Fuel: "+ str(self.speed)+ "\n"+ "Mileage: " + str(self.mileage)+ "\n")
		return self


new_Car = Car(200000, 300, "quite empty" , 100)
new_Car.display_all(tax_x)
# this is calling a 'method' - a function accessible by class instances

# new_car.price()
# new_bike.()
# new_bike.displayInfo()

