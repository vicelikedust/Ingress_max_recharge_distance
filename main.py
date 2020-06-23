from os import system, name

leveldist = [0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000,3250,3500,3750,4000]

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 

def calc():
	try:
		level = int(input('What is your player level? '))
		while level == 0 or level == 17:
			print(f"That is an invaild level \nLevel {level} doesn't exist")
			level = int(input('What is your player level? '))
	except ValueError:
		print('You entered an incorrect value, it must be a number.')
		level = int(input('What is your player level? '))
		while level == 0 or level == 17:
			print(f"That is an invaild level \nLevel {level} doesn't exist")
			level = int(input('What is your player level? '))
	
	try:
		distance = int(input('What is the distance in km? '))
	except ValueError:
		print('You entered an incorrect value, it must be a number.')
		distance = int(input('What is the distance in km? '))
	
	if distance > leveldist[level]:
		print(f'Portal is too far \nThe max distance for level {level} is {leveldist[level]}km')
	else:
		efficiency = 100 - (distance)/(5 * level)
		print(f'Recharge Efficiency is {round(efficiency,2)}{"%"}')

ans = 'yes'
if __name__ == "__main__":
    try:
        while ans == 'yes' or ans =='y':
            calc()
            ans = input('Do you want to calculate another one? ').lower()
            clear()
    except KeyboardInterrupt:
        pass
    print('\nProgram Closing...')
