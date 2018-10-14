print('Hello, Django girls!')
if 3 > 2:
    print('It works!!')
if 5 > 2:
    print('5 is greater than 2')
else:
    print('5 is not greater than 2')
name = 'Saraf'
if name == 'Umayer' : 
    print('Hey Umayer!')
elif name == 'Saraf' :
    print('Hey Saraf!')
else :
    print ('Hey Anonymous!')
area = 40
if area < 20: 
    print('area is less than 20 meter square')
elif 10 <= area < 20: 
    print ('It is large')
elif 30 <= area < 40:
    print ('perfect for me!')
else: 
    print('I like it :)')
#Change the house if it is too big!
if area < 20 or area > 80:
    area = 50
    print("That's better!")

def hi ():
    print('Hey there!')
    print('How are you doing?')

hi()

def hi(name): 
    if name == 'Saraf':
        print('Hey Saraf!')
    elif name == 'Umayer':
        print('Hey Umayer!')
    else:
        print('Hey Anonymous!')

hi(name)
def hi (name):
    print('Hi '  +  name + '!')

hi( "Saraf" )

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range (1, 6) :
    print (i)
    


