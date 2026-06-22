guess = 0
tries = 0
max_tries = 5

while guess != 777 and tries < max_tries:
    guess = int(input("Guess the number: "))
    tries += 1
    
    if guess == 777:
        print("Correct!")
    elif tries < max_tries:
        print(f"Incorrect! You have {max_tries - tries} tries left.")
    else:
        print("Incorrect! Game over. You've run out of tries.")
