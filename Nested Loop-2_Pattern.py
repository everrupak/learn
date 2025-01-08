# Method-1
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print ("x" * x_count)

print("""

""")

# Method-2
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)


