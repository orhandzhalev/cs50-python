amount = 50
accepted_coins = [25, 10, 5]

while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert coin: "))

    if coin in accepted_coins:
        amount -= coin
change = abs(amount)
print(f"Change: {change}")