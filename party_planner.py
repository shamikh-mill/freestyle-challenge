import argparse
from operator import itemgetter


ap = argparse.ArgumentParser(description='Calculate optimal foods and drinks to buy with given budget.')

ap.add_argument("-b", "--budget", type=int, default= "300",
help="Budget for the party as an integer. Ex: 300")
args = vars(ap.parse_args())

class Party: 
	def __init__(self, budget, people_file, drink_file, food_file):
		"""
		Constructor for party class. 
		:param budget: user input integer
		:param people_file: filename of people information file 
		:param food_file: filename of food information file
		:param drink_file: filename of drink information file
		"""
		self.budget = budget 
		self.people = people_file
		self.drinks = drink_file 
		self.food = food_file 
		self.party_plan = {} # reference to accepted or rejected status

	def read_people_info(self):
		"""
		Read in data from people, food and drinks files 
		"""
		with open(self.people) as p: # names not unique -> make into set 
			peoplelist = p.readlines()
		peoplelist = [x.strip() for x in peoplelist]

		people_dict = {}  # dictionary takes care of non-unique name problem 
		for i in range(0, len(peoplelist), 3): 
			if peoplelist[i] not in people_dict:
				people_dict[peoplelist[i]] = peoplelist[i + 1].split(',') , peoplelist[i + 2].split(',')   # each person mapped to a tuple of (drinks, food)  
			else: 
				people_dict[peoplelist[i]] = people_dict[peoplelist[i]][0] + peoplelist[i + 1].split(','), people_dict[peoplelist[i]][1] + peoplelist[i + 2].split(',')
		return people_dict 

	def read_prices(self, type):
		if type == 'food': 
			with open(self.food) as f: # names not unique -> make into set 
				prices = f.readlines()
		if type == 'drinks': 
			with open(self.drinks) as f: # names not unique -> make into set 
				prices = f.readlines()
				
		prices = [x.strip().split(':') for x in prices]
		prices = [x for x in prices if len(x) > 1] # remove space characters 

		dict = {}
		for x in prices: 
			dict[x[0]] = float(x[1]) 

		return sorted(dict.items(), key=itemgetter(1), reverse = True) # sorted from highest to lowest 

	def plan(self, people, food, drinks):
		num_people = len(people.keys())
		share_per_person = self.budget/num_people 
		print ('Each person is allocated', share_per_person, 'to spend on their preferred foods.')

		plan = {}
		for person in people: 
			


		return 




if __name__ == '__main__':
	my_party = Party(args['budget'], 'people.txt', 'drinks.txt', 'food.txt') #initialize with filenames in current directory, budget is input from terminal as argument 
	people_info = my_party.read_people_info()
	drink_info = my_party.read_prices('drinks')
	food_info = my_party.read_prices('food')

	print ('Budget:', my_party.budget)
	print ('Info about people:', people_info )
	print ('Prices of drinks:', drink_info)
	print ('Prices of foods:', food_info)

	my_party.plan(people_info, drink_info, food_info) 


	# divide budget by the number of people to see how much should be spend on each person, and assume that the more expensive things make people the most happy 
	# allocate budget/n for each of the n people 
	# buy favorite drink, favorite food together to avoid a trivial solution in which we just buy as much of the most expensive thing as we can 
	# once that's no longer affordable, buy lower priced items. For diversity, more than half of the food cannot be used for the same combination 



