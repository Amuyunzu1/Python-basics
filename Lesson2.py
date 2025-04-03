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

    # number guessing game with limited attempts
secret_number = 7 # Set a secret number
attempts= 5 # Maximum attempts allowed

while attempts > 0:
     guess = int(input(f"Guess the number (1-10). You have {attempts} attempts left:"))

     if guess == secret_number:
         print("Congratulations! You guessed the number: ")
         break # Exit loop if guessed correctly:
     elif guess < secret_number:
         print("Too low! Try again.")
     else:
            print("Too high! Try again.")

            attempts -= 5
            # Reduce remaining attempts
            if attempts == 0:
                 print(f"Sorry,you've used all your attempts. The correct number was {secret_number}.")