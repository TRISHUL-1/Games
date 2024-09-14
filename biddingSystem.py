ans = "Y"
bidding_list = {}

def findHighsestBidder(bidding_list) :
    highest = 0
    winner = ""
    for bidder in bidding_list :
        amount = bidding_list[bidder]
        if amount > highest :
            highest = amount
            winner = bidder
    print(f"\nThe highest Bidder is {winner} with a bid of {highest}")

while ans.upper() == "Y" :
    name = input("Enter you Name : ")
    bid = int(input("Enter your bid : "))
    bidding_list[name] = bid
    ans = input("Want to add more players (Y/N) : ")
    if ans.upper() == "N" :
        ans = "N"
        findHighsestBidder(bidding_list)
    elif ans.upper() == "Y" :
        print("\n" * 10)