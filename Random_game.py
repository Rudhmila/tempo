import random

print("----------------------")
print("Welcome To Random Guessing Game!")
print("Guess a random number, 3 time is your chance")

u = int(input("Guess a number: "))

count = 0

ran = random.randint(1,15)
while count < 3:
    if u < ran:
        print("Too low")    
    elif u > ran:
        print("Too high")
    
    count += 1
    u = int(input("Guess a number: "))
    if count == 3:
        print(f"Out of trails! The answer was: {ran}")
        break
else:
    print(f"Contrats! You guess the right number : {ran}")