#Finds the sum of all the multiples of 3 and 5 from 1 to 999

total = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)
