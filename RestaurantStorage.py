import random
import Restaurant

class RestaurantStorage:

	def __init__(self):
		self.categoryMap = {}
		self.allRestaurants = []

	def addRestaurant(restaurant):
		allRestaurants.append(restaurant.name)
		addHelper(restaurant)

	def addHelper(restaurant):
		if category in categoryMap.keys():
			currentInCategory = categoryMap[restaurant.category]
			for i in range(len(currentInCategory)):
				if restaurant.rating >= currentInCategory[i].rating:
					currentInCategory.insert(i,restaurant)
					categoryMap[restaurant.category] = currentInCategory
					return
			currentInCategory.append(restaurant)
			categoryMap[restaurant.category] = currentInCategory
			return
		else:
			categoryMap[restaurant.category] = [restaurant]

	def getAnyRestaurant():
		return random.choice(allRestaurants)

	def getByCategory(category):
		if category not in categoryMap.keys():
			return []
		return categoryMap[category]


