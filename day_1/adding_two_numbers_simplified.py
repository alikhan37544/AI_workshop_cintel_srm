def get_number():
    x = input("Enter the first number: ")
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
    print("sum is", number_sum(x,y))
    print("difference is", number_subtract(x,y))
    print("product is", number_multiply(x,y))
    print("quotient is", number_divide(x,y))
