numbers = []
number = input('Enter your number you want to input: ').split()
for num in number:
    numbers.append(float(num))
print('Here are the sum of all the number that you have input:', sum(numbers))
