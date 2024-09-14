import random

def dealCards():
    """ Returns a  random card from the deck """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculateScore(cards) :
    """ Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, sysScore):
    if userScore == sysScore:
        return "\nDraw :/"
    elif userScore == 0:
        return "\nYou win :)"
    elif sysScore == 0:
        return "\nSystem Wins :("
    elif userScore > 21 :
        return "\nYou went over, You lose :("
    elif sysScore > 21 :
        return "\nSystem went over, You Win :)"
    elif userScore > sysScore :
        return "\nYou Win :)"
    else :
        return "\nYou lose :("

def playGame() :
    userCards = []
    sysCards = []
    userScore = -1
    sysScore = -1
    isGameOver = False

    for _ in range(2) :
        userCards.append(dealCards())
        sysCards.append(dealCards())

    while not isGameOver :
        userScore = calculateScore(userCards)
        sysScore = calculateScore(sysCards)
        print(f"Your Cards : {userCards} and your current score : {userScore}")
        print(f"System's First Card : {sysCards[0]}")

        if userScore == 0 or sysScore == 0 or userScore > 21 :
            isGameOver = True
        else :
            userChoice = input("Enter 'y' to get another card, 'n' to pass : ")
            if userChoice.lower() == "y" :
                userCards.append(dealCards())
                userScore = calculateScore(userCards)
            else :
                isGameOver = True

    while sysScore != 0 and sysScore < 17 :
        sysCards.append(dealCards())
        sysScore = calculateScore(sysCards)

    print(f"\nYour final cards : {userCards}, final Score : {userScore}")
    print(f"\nSystem final cards : {sysCards}, final Score : {sysScore}")
    print(compare(userScore , sysScore))

while input("Start the game of Blackjack (y/n) : ").lower() == 'y' :
    print("\n" * 15)
    playGame()