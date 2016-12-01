import random

#										J	Q	K	A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(' ')
#print(cards) # To see the list before being shuffled

random.shuffle(cards)

#print(' ')
#print(cards) # To see the list after being shuffled
#print (' ')

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Your card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

#print(cards) # To see the list after two cards have been popped off.

#Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card2 = cards.pop();
else:
    player_card2 = 0;
	
computer_card2 = cards.pop()
print('Your card: ' + str(player_card2))
print('Computer card: ' + str(computer_card2))

print('\nYou now have: ' + str(player_card1) + ' and ' + str(player_card2))
print ('Computer now has ' + str(computer_card1) + ' and ' + str(computer_card2))
print('\nPress `s` for Stay or `h` for Hit: ')

#Round 3
decision = raw_input ('\nIf you want to stay type `s`, if you want to hit type `h`: ')
round3_computer = int(computer_card1) + int(computer_card2)

if decision == 'h':
    player_card3 = cards.pop();
else:
    player_card3 = 0;
if round3_computer <= 16:
    computer_card3 = cards.pop()
elif round3_computer > 16:
    computer_card3 = 0

print('\nYout cards: ' + str(player_card1) + ' , ' + str(player_card2) + ' , ' + str(player_card3))
print('Computer cards: ' + str(computer_card1) + ' , ' + str(computer_card2) + ' , ' + str(computer_card3))

#Final Steps
player_total = int(player_card1) + int(player_card2) + int(player_card3)
comp_total = int(computer_card1) + int(computer_card2) + int(computer_card3)
print('\nGame over! Player total: ' + str(player_total) + ' Computer total: ' + str(comp_total))

if player_total > 21 and comp_total > 21:
    print('\nTie! Both Player and Computer busted!')
elif player_total == comp_total:
    print('\nTie!')
elif comp_total > 21:
    print('\nPlayer won, Computer busted!')
elif player_total > 21:
    print('\nComputer won, Player busted!')
elif player_total > comp_total:
    print('\nPlayer won, closer to 21!')
else:
    print('\nComputer won, closer to 21!')
	