import art

#HINT: You can call clear() to clear the output in the console.
print(art.logo)

bidder = {}
moreBids = False

def findHighestBid(bid_record):
    highBid = 0
    winner = ""
    for bidders in bid_record:
        bidAmount = bid_record[bidders]
        if bidAmount > highBid:
            highBid = bidAmount
            winner = bidders
    print(f"Winner is {winner} with a bid of ${highBid} ")


while not moreBids:
    name = input("What is your name?: ")
    bid = int(input("What would you like to bid?: $ "))
    bidder[name] = bid
    additionalBidders = input("Are there more bidders? yes / no? \n").lower()
    if additionalBidders == "no":
        moreBids = True
        findHighestBid(bidder)
    elif additionalBidders == "yes":
        art.clear()


