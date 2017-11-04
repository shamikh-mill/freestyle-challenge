# FreeStyle Fellows Engineering Challenge: Party Planner 

Link to GitHub: https://github.com/shamikh-mill/freestyle-challenge

## How it works 
Party Planner is a program that takes in inputs of a budget, a list of people and their favorite foods and drinks, and lists of food and drink prices to output the "plan", or the best way to allocate the given budget with the number of each food and drink to buy. The program implements the philosophy of greedy algorithms in that it's assuming that people are the most happy when they get the food or drinks that worth the most money. Thus, the program optimizes the party plan using prices. It assumes that each person wants both food and drink, and fairly allocates a portion of the main budget to each person. Then, it proceeds to buy the most of the most expensive good it can, and then proceeding the next most expensive good, until the budget is diminished. It does this for each person to end with a party plan that has the most of the most expensive preferred things possible, maximizing utility in the price sense. 



## Running this project
In the directory that contains the party_panner.py and the drinks.txt, files.txt, and people.txt files, simply run the following, entering the budget (an integer) of the party as a command line argument using --budget (or -b) like so: 

````
$ python party_planner.py --budget 300 

// Example Output: 
// Each person is allocated 100 to spend on their preferred foods.
// Food Plan: {'pasta': 32.0, 'french fries': 2.0, 'taco': 50.0}
// Drink Plan: {'soymilk': 32.0, 'pomegranate juice': 1.0, 'fruit punch': 28.0, 'lemonade': 2.0, 'chocolate milk': 1.0}
````



## Assumptions Made
For clean formatting and parsing, in my test cases I am assuming that the comma-delimited text files are specically only comma-related, i.e they say 'pizza,pasta' instead of 'pizza, pasta', like a csv file would. Spaces can still exist inside names of foods and drinks. 
I'm assuming the text files don't have newline or space characters at the end of the files in my test cases. 

## Details 
This program creates a "Party" class in Python using the file inputs and then constructs data structures (using methods) from the information to be able to output key information. The class is instatiated with
````
my_party = Party(args['budget'], 'people.txt', 'drinks.txt', 'food.txt') 
```` 


## Example Test Case 

Here's an example test case I used:

people.txt 

John Smith  
orange juice,apple juice,fruit punch,pomegranate juice,lemonade  
pizza,pasta,lasagna,french fries,tacos,baked potatoes  
Elliot Ro  
fruit punch,lemonade  
pizza,pasta,lasagna,french fries  
Samantha Tarl  
milkshakes,chocolate milk,soymilk  
hamburgers,hot dogs,tomatoes,tacos  
John Smith  
chocolate milk,soymilk  
hot dogs,tomatoes  


food.txt  
 
pizza:2.50  
pasta:3.00  
lasagna:2.75  
french fries:1.50  
taco:1.00  
baked potato:1.50  
hamburger:3.00  
hot dog:1.50  
tomato:.75   

drinks.txt   

orange juice:1.25  
apple juice:1.50  
fruit punch:1.75  
pomegranate juice:2.00  
lemonade:.50  
milkshakes:2.50  
chocolate milk:1.75  
soymilk:3.00  
