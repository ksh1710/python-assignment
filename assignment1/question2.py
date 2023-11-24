numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    print(fact,end=',')