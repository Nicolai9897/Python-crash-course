#10-6 Addition

print("a simple program to add two numbers together. please write the numbers you want to  add")
def addition():
    """simple function for adding two integers"""
    try:
        a = int(input("please write the first number: "))
        b = int(input("please write the second number: "))
    except ValueError:
        print("please only write integeres")
    else:
        print(f"the answer is: {a + b}")
#addition()


#10-7


def get_number_a():
    a = input("please write the first number: ")
    if a == 'q':
        return False
    else:
        try:
            float(a)
        except ValueError:
            print("please only write integeres")
        else:
            return float(a)

run = True
def addition3():
    while True:
        try:
            a = input("Plese write the first number")
            if a == 'q':
                break

            a = float(a)

            b = input("Plese write the second number")
            if b == 'q':
                break

            b = float(b)
        except ValueError:
            print("please only write integeres")
        else:
            sum = a + b
            print(f"the two numbers added together equals {sum}")
addition3()

__main__

