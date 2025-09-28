# 1st Example: General try except example

x = 3 / 0
print(x)

try:
    # Code that may raise an exception
    x = 3 / 0
    print(x)
except:  # Uses a bare except which is not a good practice
    # exception occurs, if code under try throws error
    print("An exception occurred.")


# 2nd Example: Try Except with a specific error to catch
def divide(a, b):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = a // b
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero ")


# Look at parameters and note the working of Program
divide(3, "a")  # TODO: Change 1 value to a string and check if error is handled


# 3rd Example: Cathing the exception
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ", e)


divide(3, "GFG")
divide(3, 0)

# 4th Example: Else clause
try:
    x = 1 / 0  # TODO: Change second number to 0 to reach except
    print("Try executed without exception.")
except:
    print("Except is reached and else not executed.")
else:
    print("Else is reached.")

# 5th Example: Finally
try:
    x = 1 / 0  # TODO: Change second number to 0 to reach except
    print("Try executed without exception.")
except:
    print("Except is reached and else not executed.")
else:
    print("Else is reached.")
finally:
    print("I am reached regardless of what happens above.")
