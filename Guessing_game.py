
number_of_guesses=1
print("Number of Guesses is Limited to just 9")
while number_of_guesses<=9:
    guess_number=int(input("Enter the number\n"))
    if guess_number<18:
        print("Enter a Number Greater than this")
    elif guess_number>18:
        print("Enter a Number less than this")
    else:
        print("You Won\n")
        print("Congrats\n")
        print("You took", number_of_guesses, "Guess to finish the game")
        break
    print(9-number_of_guesses,"Number of Guesses Left")
    number_of_guesses=number_of_guesses+1
if number_of_guesses>9:
    print("Game Over")
    print("Thank you for playing")