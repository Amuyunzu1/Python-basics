# check a number if it's even or odd
attempts= 4 # Maximum attempts allowed

while attempts > 0:
     number = int(input(f"Enter a number. You have {attempts} attempts left:"))
         # conditional checking
         # if the number is divisible by 2, then even
         # else number is odd
     if number%2==0:
         print(number, "is even.")
    
     else:
            print(number, "is odd.")

            attempts -= 4
            # Reduce remaining attempts
            
            if attempts == 0:
                 print(f"Goodbye.")