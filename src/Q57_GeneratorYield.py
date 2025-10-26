# Write a program to use a generator with yield.
print('Q57_GeneratorYield.py')

# Generator function for Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a  # yield returns value and pauses execution
        a, b = b, a + b
        count += 1

print("Fibonacci sequence (first 10 numbers):")
for num in fibonacci_generator(10):
    print(num, end=" ")

# Generator for squares
def square_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

print("\n\nSquares from 1 to 10:")
for square in square_generator(1, 10):
    print(square, end=" ")

# Generator for even numbers
def even_generator(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

print("\n\nEven numbers up to 20:")
for even in even_generator(20):
    print(even, end=" ")

# Generator for countdown
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("\n\nCountdown from 5:")
for num in countdown(5):
    print(num, end=" ")

# Using next() with generator
print("\n\nUsing next() with generator:")
gen = square_generator(1, 5)
print("First:", next(gen))
print("Second:", next(gen))
print("Third:", next(gen))
