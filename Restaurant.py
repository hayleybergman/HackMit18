"""
Restaurant class
"""

class Restaurant:
	def __init__(self):
		self.name = ""
		self.rating = 0
		self.category = ""
		# self.favorite_item = ""

	def __init__(self, name, rating, category):
		self.name = name
		self.rating = rating
		self.category = category

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_rating(self):
		return self.rating

	def set_rating(self, rating):
		self.rating = rating

	def get_category(self):
		return self.category

	def set_category(self, category):
		self.category = category

	def to_string(self):
		return self.name + ": \t" + str(self.rating)

    #updates restaurant information (rating and favorite item)
	def update(self, rating, favorite_item):
		self.rating = rating
		self.favorite_item = favorite_item
