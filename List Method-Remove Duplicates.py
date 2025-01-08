numbers = [1, 2, 4, 5, 7, 4, 2, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

