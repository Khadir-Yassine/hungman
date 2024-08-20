def hungman_game() :
    name = input('What is your name ? : ')
    print(f'Hello , {name}, It is time to play hangman')
    print('start guessing.....')
    #determine number of turns
    turn = 10
    #create a variable with an empty value
    guesses = ''
    # here we set the secret
    word = 'secret'

    while turn > 0 :
        failed = 0
        for char in word :
            if char in guesses :
                print(char)
            else :
                print('_') 
                failed += 1
        if failed == 0 :
            print('YOU WON !!')
            break
        guess = input('enter the character : ')
        guesses += guess
        if turn is not word :
            print('Wrong guess')
            turn -= 1
        print(f'You have {turn} more guesses')
        if turn == 0 :
            print('game is over')

hungman_game()

check = input ('do you want to play again yes or no : ').lower()
if check == 'yes'  :
    hungman_game()   


        
