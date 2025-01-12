# Input in words for value error.
# Input 0 (zero) for zero division error.
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
