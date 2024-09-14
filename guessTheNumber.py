from random import randint

def difficulty() :

    """ Based on the choosen difficulty assigns the number of attempts """

    chooseDifficulty = input("Choose a dificulty. type 'easy' or 'hard' : ")
    if chooseDifficulty.lower() == 'easy' :
        return 10
    else :
        return 5

def checkAns(userInput, randomNo) :

    """ Compares the user input and the system generated number """

    if userInput > randomNo :
        print("Too High")
    elif userInput < randomNo :
        print("Too Low")
    

def playGame():

    """ Launches the game """

    # randomNo = random.choice(range(1,101))

    randomNo = randint(1, 100)

    userAttempts = difficulty()

    print("I'm thinking of a number between 1 and 100.")

    while userAttempts != 0 :
        print(f"Now you have {userAttempts} attempts to guess the number.")
        userInput = int(input("Make a guess : "))
        if userInput == randomNo :
            print(f"\nYou guessed it! The correct number is {randomNo}")
            break
        else :
            checkAns(userInput, randomNo)
            userAttempts -= 1
            if userAttempts == 0 :
                print("You ran out of attempts")

while input("Want to play Guess The Number (y/n) : ").lower() == "y" :
    playGame()

print("\n" *20)