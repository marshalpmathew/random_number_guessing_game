import random
import time
n = int(input("Enter a number between 1 and : "))
num = random.randint(1,n)
guess = int(input("Guess the number between 1 and {}: " .format(n)))
while guess != num :
    if guess < num:
        print("Your guess was low")
        time.sleep(1)
        guess = int(input("Guess the number between 1 and {}: '.format(n)"))
    if guess > num:
        print("Your guess is high")
        time.sleep(1)
        guess = int(input("Guess the number between 1 and {}: '.format(n)"))
        
print("Congratulations you guessed it! ")
