import random
import Restaurant

class RestaurantStorage:

	def __init__(self):
		self.categoryMap = {}
		self.allRestaurants = []

	def addRestaurant(self, restaurant):
		self.allRestaurants.append(restaurant.name)
		self.addHelper(restaurant)

	def addHelper(self, restaurant):
		if restaurant.category in self.categoryMap.keys():
			currentInCategory = self.categoryMap[restaurant.category]
			for i in range(len(currentInCategory)):
				if restaurant.rating >= currentInCategory[i].rating:
					currentInCategory.insert(i,restaurant)
					self.categoryMap[restaurant.category] = currentInCategory
					return
			currentInCategory.append(restaurant)
			self.categoryMap[restaurant.category] = currentInCategory
			return
		else:
			self.categoryMap[restaurant.category] = [restaurant]

	def getAnyRestaurant(self):
		return random.choice(self.allRestaurants)

	def getByCategory(self, category):
		if category not in self.categoryMap.keys():
			return []
		return self.categoryMap[category]


