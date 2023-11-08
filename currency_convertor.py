transactions_aed = [10.45, 23.75, 18.50, 19.50, 12.43, 15.55, 968.10, 50.55]

transactions_usd = []

for transactions in transactions_aed:
    itme_usd = transactions * 0.27
    print("Converting value", transactions)
    transactions_usd.append(itme_usd)

lst = [2, 4, 5, 6]

for number in lst:
        if number % 2 == 0:
            print(number *2)

print(transactions_usd)