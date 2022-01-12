stocks = {"MSFT", "FB", "IBM", "FB"}
print(stocks) # {'MSFT', 'FB', 'IBM'} duplicate was removed

prices = {1, 2, 3, 4, 5, 3, 4, 2}
print(prices)

lottery_numbers = {(1, 2, 3), (4, 5, 6), (1, 2, 3)}
print(lottery_numbers)

# length w/o duplicates
print(len(stocks)) 
print(len(prices)) 
print(len(lottery_numbers))

print("MSFT" in stocks)
print("IBM" not in stocks)
print("GOOG" in stocks)
print("GOOG" not in stocks)

for number in prices:
    print(number)

print()

for numbers in lottery_numbers:
    for number in numbers:
        print(number)

squares = {number ** 2 for number in [-5, -4, -3, 3, 4, 5]}
print(squares) # 9, 16, 25 although not necessarily in that order. Duplicates are gone.
print(len(squares))