# Text based adventure game
import animations

animations.printStartingAnimation()
print('Oh no! You forgot your lunch at home! ')
print('What should you do? ')
print('[0] Oh well! It happens, right?')
print('[1] Get angry at yourself for forgetting everything all the time!')
print('[2] Can\'t think of a better opportunity for some tacos for lunch. ')
choice = int(input('Your choice is: '))

if choice == 0:
    print('You continue your day as happy as ever. Good job!')
elif choice == 1:
    print('Don\'t be so hard on yourself, buddy!')
elif choice == 2:
    print('Noon comes and you go for some tacos. How spicy should it be?')
    print('[0] Go soft on me today, Chef!')
    print('[1] Some chilli can\'t hurt!')
    print('[2] Do the \'Eat it the way the Chef likes it\' challenge!')
    choice = int(input('Your choice is: '))
    if choice == 0 or choice == 1:
        print('You eat some excellent tacos and have a great day.')
    else:
        print('You already regret your words as they leave your lips. You are no quitter, so you eat it all. You poor fool!')
else:
    print('You like breaking the rules, don\'t you? :)')