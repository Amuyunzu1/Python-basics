# simple guessing game
secret_number = 7
guess=int(input("Enter your guess!"))
while guess != secret_number:
    if guess < secret_number:
        print("Your guess is too low, try again.")
    else:
        print("Your guess is too high, try again.")
    guess=int(input("Enter your guess: "))
    print("congratulations! You guessed the correct number.")