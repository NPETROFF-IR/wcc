meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
if chosen_option == 'a':
    percentage = .15;
elif chosen_option == 'b':
    percentage = .18;
elif chosen_option == 'c':
    percentage = .20;
else:
	print('You did not enter a valid option, defaulting to 20%.')
	percentage = .20

tip = meal_price * percentage
total_price = meal_price + tip
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))

#temp = int(raw_input('What is the temperature? '))

#print('You should bring the following items:')
#if temp <= 40:		#True value => Branch
    #print('Coat')	# 4 SPACES
    #print('Hat')	# 4 SPACES
    #print('Gloves')	# 4 SPACES

#elif temp <= 70:
    #print('Coat')
    #print('Hat')
#else:				#Think of it as the Default option
    #print('Nothing!')
	
print (' ')
print ('CHAINED CONDITIONALS')
age = int(raw_input('How old are you? '))
if age < 3:
    print('baby')
elif age < 16:
    print('child')
elif age < 18:
    print('adolescent')
elif age < 21:
    print('young adult')
else:
    print('adult')
	
age = int(raw_input('How old are you, two options? '))
if age < 18:
    print('child')
else:
    print('adult')

age = int(raw_input('How old are you, one cond? '))
if age > 75:
    print('retired')


print('Unchained CONDITIONALS')	
age = int(raw_input('How old are you? '))

if age > 16:
    print('You can drive')    
if age > 18:
    print('You can vote')
if age > 21:
    print('You can join the military')
if age > 75:
    print('You can retire')



