import random
magic_numbers = [random.randint(0,9), random.randint(0,9)]
chances = 3
for attampt in range(chances): # range(chances) is 0,1,2
    print('This is an attampt{}'.format(attampt))
    user_number = int(input('Enter a number between 0 and 9:'))
    if user_number in magic_numbers:
        print('you got it right')
    if user_number not in magic_numbers:
        print("You didn't get it right")
        
    


