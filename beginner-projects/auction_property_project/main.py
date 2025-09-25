import art

name = r'''
   🔨💰 AUCTION HOUSE 💰🔨
   -----------------------
'''
print(name)
print(art.logo)

auction_data = {}

should_continue = "yes"

while should_continue == "yes":
    user_name = input("📝 Enter your name: ")
    try:
        user_bid = int(input("💵 Enter your bid: $"))
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")
        continue
    
    auction_data[user_name] = user_bid

    while True:
        should_continue = input("Type 'yes' ➡️ or 'no' ❌ if there are any other bidders: ").lower()
        if should_continue == "yes":
            print("\n" * 100)
            break
        elif should_continue == "no":
            print("\n" * 100)
            print("🔒 Auction closed. Calculating results... 📊")
            break
        else:
            print("\n" * 100)
            print("⚠️ Invalid choice!")
            continue

def find_highest_bidder(auction_data):
    highest_bid = 0
    winner = None
    for key in auction_data:
        if auction_data[key] > highest_bid:
            highest_bid = auction_data[key]
            winner = key
    # OR use max function
    # max(auction_data, key = auction_data.get)

    print(f"🏆 Winner is 🎉 {winner} with highest bid of 💰 ${highest_bid}")

find_highest_bidder(auction_data)
