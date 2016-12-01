answer1_correct = True
answer2_correct = False

#print(1==1) #Expected output: True

#RATIONAL OPERATORS
#== Equal
#!= Does not equal
#> Greate than
#< Less than
#>= Greater than or equal
#<= Less than or equal

#print(1== ) #Expected output: 

print(1== 1) #Expected output: True
print(1>2 ) #Expected output: False
print(1>1 ) #Expected output: False
print(1>=1 ) #Expected output: TRUE!
print(2==2 ) #Expected output: True
print(2 != 2) #Expected output: False

print(' ')
print ('AGE')
age = 30
print(age > 30) #Expected outcome: False
print(10 < age) #Expected outcome: True
print(age > 10 + 20) #Expected outcome: False
print(age + 20 > 10) #Expected outcome: True

print( ' ')
print('STRINGS')
print('a' > 'z') # Expected outcome: False
print('z' > 'a') # Expected outcome: True
print('apples' > 'oranges') # Expected outcome: False
print('oranges' > 'apples') # Expected outcome: True
print('cat' > 'car') # Expected outcome: True
print('car' > 'cat') # Expected outcome: False

print(' ')
print('DIFFERENT TYPES OF DATA')
answer = int(raw_input('What is 1 + 1? ')) #convert String to Int!
print(answer==2)


print(' ')
print('LOGICAL OPERATORS')
age = 1
print(age > 12 and age < 19) # Expected outcome: False

age = 14
print(age > 12 and age < 19) # Expected outcome: True

age = 19
print(age > 12 and age < 19) # Expected outcome: False

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome: True

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome: False

age = -1
print(age > 12 and age < 19) # Expected outcome: False

age = 10
print(age > 25 and age < 15) # Expected outcome: False   
# Could the above expression ever be True?
#Yes, if we use the 'OR' operator, or switch places and use 'AND NOT';
age = 10
print(age > 25 or age < 15) # Expected outcome: True  
age = 10
print(age < 15 and not age > 25) # Expected outcome: True   


print(' ')
print('PAPER ROCK SCISSORS')
gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True

gesture = 'paper'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True

gesture = 'rock'
print(gesture == 'rock' and gesture == 'paper' or gesture == 'scissors') #False

print(' ')
print('Age gr 5 less 10 inclusive')
age = int(raw_input('How old are you? '))
print(age >= 5 and age<=10)

age = int(raw_input('How old are you? '))
print(age >= 5 and age<=10)

print(' ')
print('Age gr 5 less 10 non inclusive')
age = int(raw_input('How old are you? '))
print(age > 5 and age < 10)

age = int(raw_input('How old are you? '))
print(age > 5 and age < 10)







