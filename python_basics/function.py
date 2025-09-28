# Default arguments
def my_func(x, y=10):
    print("x: ", x)
    print("y: ", y)


my_func(5)


# Keyword arguments
def student(fname, lname):
    print(fname, lname)


student(fname='QA', lname='Tester')
student(lname='Soft', fname='Developer')


# Positional arguments
def name_age(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
name_age("Suraj", 27)

print("\nCase-2:")
name_age(27, "Suraj")


# Arbitrary arguments
def my_fun(*args):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)


def my_fun2(**kwargs):
    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


# Function call with args
my_fun('Hey', 2)

# Function call with kwargs
my_fun2(first='Geeks', mid='for', last='Geeks')


# Return statement
def multiply(x: int) -> int:
    answer = x * 2
    return answer


print(multiply(10))


# Return function
def square_value(num: int) -> int:  # Provides hints to parameter and return type
    """This function returns the square
    value of the entered number"""
    return num ** 2


print(square_value(2))
print(square_value(-4))
