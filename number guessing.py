import random
def number_guessing_game():
    print("welcome to the number guessing game 🎱")
    print("Think of a number between 1 and 100😉")
    
    
    
    secret_num= random.randint(1,100)
    attempts = 0

    while True:
        try:
            # Get input from the user and convert it to an integer
            guess= int(input("\n Enter your guess:"))
            attempts+=1

            #checks the users guess against the secret number
            if guess<secret_num:
                print("Too low! Try a higher number:")
            if guess>secret_num:
                print("Too high! Try a lower number")
            else:
                print(f"\n🎊 congratulations you guess the number in {attempts} attempts!")
                break # exit the loop since the game is won
        except ValueError:
            print("invalid input.please enter a valid whole number!")

#Run the game
number_guessing_game()