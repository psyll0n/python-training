#! python3

import ascii_art


print(ascii_art.gavel)


# Compare the bids in the dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with bid of {highest_bid}")


# Save the data provided by the user into a dictionary {name: price}
bids = {}
continue_bidding = True

while continue_bidding:
    # Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price

    # Prompt that asks whether new bids need to be added
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n"
    ).lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)
