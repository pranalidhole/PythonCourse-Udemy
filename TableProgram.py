#ASk user to enter a number and then print table of the number
number = input('Enter number')
for i in range(1,11):
    output = int(number) * i
    line = str(number) + " x " + str(i) + " = " + str(output)
    print(line)