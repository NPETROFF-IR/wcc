#USER DEFINED FUNCTIONS

#in plaing English: def (aks function) function_name(parameter1, parameter2, etc.):
#					_ _ _ _ 4 spaces then NAME and spell it out
#					return NAME

#####, part 2, Import statements should always be at the top of your file,
#####not in the body of the functions
import random

def draw_random_card():
	cards = [1,2,3,4,5,6,7,8,9,10,10,10,11]
	random.shuffle(cards)
	return cards.pop()

#Test the function:
print(draw_random_card()) #Expected: Random number b/n 1 & 11
print(draw_random_card()) #Expected: Random number b/n 1 & 11
print(draw_random_card()) #Expected: Random number b/n 1 & 11
print(draw_random_card()) #Expected: Random number b/n 1 & 11

def multiply (a,b):
	result = a * b
	return result
	
#Test the function:
solution=multiply(4,5) #Invoce multiply givinh it the argument of 4 and 5
print(solution) #Expected: 20

#Test the function in ONE line:
print(multiply(4,5)) #Expected: 20

#Test the function:
print(multiply(4,5)) #20
print(multiply(9,11)) #99
print(multiply(0,10)) #0
print(multiply(.5,9)) #4.5
print(multiply(-1, -55)) #55
print(multiply(3, 'Hello')) #'HelloHelloHello'

def isPositive(a):
	if a>0:
		return True
	else:
		return False

#Test the function:
print(isPositive(-14)) #Expected: False
print(isPositive(4)) #Expected: True
print(isPositive(-9.9)) #Expected: False
print(isPositive(9.9)) #Expected: True


##Non-fruitful functions:
##WHAT not-fruitful functions do: 
##send an email
##add an entry to a database
##write to a log file

def display_winner(winner, msg):
	if winner == 'Player':
		outcome = 'You win! '
	else:
		outcome = 'Computer wins! '
		
	print(outcome + '(' + msg + ')') ###PRINT MUST BE INDENTED!!!

#Test the function:
display_winner('Player', 'You were closest to 21') #Expected: 'You win! You were closest to 21'
display_winner('Computer', 'It was closest to 21') #Expected: 'Computer win! It was closest to 21'
display_winner('Computer', 'You busted') #Expected: 'Computer win! You busted'

def cube(a):
	product = a*a*a
	return product
solution1=cube(2)
print(solution1)

##Wrong syntax
#def isPositive(a):
#    return a > 0:
	
def mystery(x, y, z):
	product_mystery = x + z*y
	return product_mystery
    # ??? Your code here 

# Test this function:
print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def caltulateTip (p, q):
	product_tip =  p * q
	
	if q =='A':
	return product_tip =  p * .20
	
	elif q == 'B':
	return product_tip =  p * .18
	
	elif q == 'C':
	return product_tip =  p * .15
	
print (caltulateTip (30.50, 'C'))


