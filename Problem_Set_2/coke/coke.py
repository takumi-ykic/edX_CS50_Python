amount = 50
print("Amount Due:", amount)
while amount > 0:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        if coin < amount:
            amount -= coin
            print("Amount Due:", amount)
        else:
            print("Change Owed:", coin - amount)
            break
    else:
        print("Amount Due:", amount)




