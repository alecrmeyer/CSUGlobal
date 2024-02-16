import sys
num_string = input("Please enter 2 numbers with a space between them: ")
num_arr = num_string.split(' ')

try:
    num1 = float(num_arr[0])
    num2 = float(num_arr[1])
except:
    print("Invalid input")
    sys.exit(1)

input_prod = num1 * num2
input_quo = num1 / num2
print("Product: " + str(input_prod))
print("Quotient: " + str(input_quo))