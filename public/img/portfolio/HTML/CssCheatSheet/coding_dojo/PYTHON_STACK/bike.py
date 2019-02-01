class Bike:
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print("the price is " + str(self.price) + "the max.speed\n" + str(self.max_speed) +"\n"+ str(self.miles))
		return self

	def ride(self):
		self.miles+=10
		print("Riding")
		# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10

		# print("the maximum speed is " + str(self.max_speed))

 # have it display "Reversing" on the screen and decrease the total miles ridden by 5...
	def reverse(self):
		self.miles-=5
		print("Reversing")




# new_user = User("Anna","anna@anna.com")

new_bike= Bike(200,30)
# This is 'instantiation' - creating an object from the class Blueprint

new_bike.displayInfo()
# this is calling a 'method' - a function accessible by class instances

new_bike.ride()
new_bike.reverse()
new_bike.displayInfo()




