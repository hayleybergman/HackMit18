from RestaurantStorage import RestaurantStorage
from Restaurant import Restaurant

restaurants = RestaurantStorage()
r1 = Restaurant("pep", 5, "thai")
restaurants.addRestaurant(r1)

i = input("Welcome to Personal Restaurant Picker, tell me what you would like to do: ")
running = True

while running:

	if i == "where should I eat":
		print(restaurants.getAnyRestaurant().to_string())

	elif i == "add a restaurant":
		name = input("What is the restaurant's name? ")
		rating = float(input("How would you rate " + name + " out of 5? "))
		category = input("What type of cuisine does " + name + " serve?")
		r = Restaurant(name, rating, category)
		restaurants.addRestaurant(r)


	elif i == "get restaurant in category":
		category = input("What type of cuisine do you want?")
		r = restaurants.getByCategory(category)
		if r == []:
			print("You don't have any restaurants in that category...you should get out more")
		else:
			for res in r:
				print(res.to_string())

	elif i == "quit":
		running = False
