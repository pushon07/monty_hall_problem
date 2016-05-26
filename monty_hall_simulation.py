__author__ = 'ASM Pushon'

"""
Simulation of Monty Hall problem in Python. It shows the simulated outcomes of winning the car
based on your decision of switching or not switching the initially selected door.
Usage: <python monty_hall_simulation.py>
"""

import copy
import random
import time

prob_stat = """Problem Statment:
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car;
behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors,
opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?"
Is it to your advantage to switch your choice? What would you do? Think about it.
"""

print prob_stat

choices = ['Car', 'Goat', 'Goat']
num_guess = 30700
num_correct_guess = 0
switch = False

time.sleep(3)
print "Please tell about your decision."
user_decision = raw_input("Enter 'y' to switch or 'n' to decline switching (Default is 'n'). ->") or 'n'
user_decision = user_decision.lower()

while not((user_decision == 'y') or (user_decision == 'n')):
	user_decision = raw_input("Please insert 'y' or 'n' here. ->")

if user_decision == 'y':
	switch = True
elif user_decision == 'n':
	switch = False

for _ in xrange(num_guess):
    random.shuffle(choices)
    possible_car_positions = [0, 1, 2]
    initial_guess_car_position = random.choice(possible_car_positions)
    
    #after showing one door with Goat
    car_actual_position = choices.index('Car')
    
    if initial_guess_car_position != car_actual_position:
        new_possible_car_positions = [initial_guess_car_position, car_actual_position]
    else:
		fake_car_positions = copy.copy(possible_car_positions)
		del fake_car_positions[car_actual_position]
		fake_car_position = random.choice(fake_car_positions)
		new_possible_car_positions = [initial_guess_car_position, fake_car_position]
	    

    if switch == False:
        #final_guess_car_position = initial_guess_car_position
        if initial_guess_car_position != car_actual_position:
        	new_possible_car_positions.remove(car_actual_position)
        else:
        	new_possible_car_positions.remove(fake_car_position)

        final_guess_car_position = new_possible_car_positions[0]
    
    else:   #if switch == True
        new_possible_car_positions.remove(initial_guess_car_position)
        final_guess_car_position = new_possible_car_positions[0]
    
    if choices[final_guess_car_position] == 'Car':
        num_correct_guess += 1
    
if switch == True:
	print "Since you switched the door, your chances of winning the car would be:"
else:
	print "Since you did not switch the door, your chances of winning the car would be:"

print "%.3f percent after running %d simulations." % ((100.0 * num_correct_guess / num_guess), num_guess)

