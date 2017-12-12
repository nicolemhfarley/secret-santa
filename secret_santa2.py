### Draw secret santas from among pairs of spouses
import random

people = input("List people participating in secret santa, separated by commas: ")
print(people)
spouses = input("List spouses of participants in order, separated by commas: ")
print(spouses)

# split people and spouses into lists, removing empty spaces

people_list = people.split(",")
people_list = list(map(str.strip, people_list))
print(people_list)

spouse_list = spouses.split(",")
spouse_list = list(map(str.strip, spouse_list))
print(spouse_list)

# function to draw randomly from people and spouses list and pair them

def draw_name(list):
	global x
	x = random.choice(list)	
	return (x)

pairs = list(zip(people_list, spouse_list))
print(pairs)

# test to make sure secret santas aren't spouses or themselves.  
secret_santas_list = []
used_names = []
i = len(people_list)

while len(used_names) < i:
	for name in people_list:
		draw_name(spouse_list)	
		if (name, x) not in pairs and name != x and x not in secret_santas_list and name not in used_names:
			secret_santas_list.append(x)
			used_names.append(name)
			print(name + "'s secret santa is " + str(x))







		

