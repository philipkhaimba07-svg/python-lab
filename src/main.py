from utils import square, is_even, celsius_to_fahrenheit, greet

name = input("What is your name? ")
print(greet(name))

n = float(input("Enter a number: "))
print(f"Square: {square(n)}")

if n == int(n):
    print("Even" if is_even(int(n)) else "Odd")
else:
    print("Not a whole number, so even/odd does not apply")

print(f"Fahrenheit: {celsius_to_fahrenheit(n)}")