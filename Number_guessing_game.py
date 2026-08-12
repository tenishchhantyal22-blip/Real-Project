import random
number_to_guess = random.randint(1, 1000)
while True:
    try:
        guess = int(input("Guess the number between 1 and 1000: "))
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("To Low!")
        else:
            print("Congratulation! you guessed the number.")
            break
    except ValueError:
        print("Please enter a valid numebr")




