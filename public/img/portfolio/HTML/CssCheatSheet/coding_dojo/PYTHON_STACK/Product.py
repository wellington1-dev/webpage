class Product:

	def __init__(self,price,item,weight,brand):
		self.price = price
		self.item = item
		self.weight = weight
		self.brand = brand
		self.status = "for sale" 

	def sell(self):
		self.status = "sold"
		print("sold")

	def reasons_for_return(self):
		if self.status == "defective":
			return defective

	def tax_added(self):
		tax = 0.12
		self.price=price + tax
		return self.price

	def displayInfo(self):
		print("the price is " + str(self.price)"\n" + " Item" + "\n" + str(self.item) +"\n"+ str(self.weight)+"\n"+ str(self.brand)+"\n"+ str(self.sell))
		return self

		

new_product = Product(500,"computer",15,"Microsoft")
new_product.displayInfo()
new_product.sell()
new_product.tax_added()


