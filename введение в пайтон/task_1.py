end = 1000000002
summ = 0
for i in range(0, end+1, 3):
    if (i % 10 != 4) or (i % 10 != 7):
        summ = summ + i
        print(summ)
