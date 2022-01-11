import random

def is_valid(num):
    if 1 <= num <= 100:
        return True
    else:
        return False

def answer():
    print("Do you want to play again? y = yes, n = no")
    s = input()
    if s == "y":
        print("Okeeey, let\'s go!")
        print("The number is guessed, enter your variant")
        num_guess()
    else:
        print("Thank you for playing Numerical Guess. See you later ...")

def num_guess():
    random_number = random.randint(1, 100)
    count = 0
    flag = False

    while flag == False:
        user_number = int(input())
        if is_valid(user_number) == False:
            print("Or maybe we will enter an integer from 1 to 100?")
        elif user_number < random_number:
            count += 1
            print("Your number is less than expected, try again")
        elif user_number > random_number:
            flag = False
            count += 1
            print("Your number is greater than expected, try again")
        elif user_number == random_number:
            count += 1
            print("You guessed it, congratulations!")
            print("The number of your attempts:", count)
            flag = True
            answer()
        

print("Welcome to Numerical Guess")
print("The number is guessed, enter your variant")
num_guess()
