restaurants = RestaurantStorage()

i = raw_input("Welcome to Personal Restaurant Picker, tell me what you would like to do")

if i == "where should I eat":
	print(restaurants.getAnyRestaurant())

elif i == "add a restaurant":
	name = raw_input("What is the restaurant's name? ")
	rating = raw_input("How would you rate " + name + " out of 5? ")
	category = raw_input("What type of cuisine does " + name + " serve?")
	r = Restaurant(name, rating, category)
	restaurants.addRestaurant(r)


elif i == "get restaurant in category":
	category = raw_input("What type of cuisine do you want?")
	r = restaurants.getByCategory(category)
	if r == []:
		print("You don't have any restaurants in that category...you should get out more")
	else:
		for res in r:
			print(res.name + ": \t" + res.rating)
