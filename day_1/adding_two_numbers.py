# Program to add 2 numbers

def get_number():
	x = input("Enter the first number: ")

	while type(x) != int:
		try:
			x = int(x)
		except:
			print("Please enter an int")
			x = input("Enter the first number: ")

	y = input("Ente the second number: ")

	while type(y) != int:
		try:
			y = int(y)
		except:
			print("Please enter an int")
			y = input("Enter the second number: ")

	return x,y

def number_sum(x,y):
	number_sum = x + y
	return number_sum

def number_subtract(x,y):
	number_subtract = x - y
	return number_subtract

def number_multiply(x,y):
	number_multiply = x * y
	return number_multiply

def number_divide(x,y):
	number_divide = x / y
	return number_divide

if __name__ == "__main__":
	x,y = get_number()
	print("The sum of {} and {} is {}".format(x,y,number_sum(x,y)))
	print("The difference of {} and {} is {}".format(x,y,number_subtract(x,y)))
	print("The product of {} and {} is {}".format(x,y,number_multiply(x,y)))
	print("The quotient of {} and {} is {}".format(x,y,number_divide(x,y)))
