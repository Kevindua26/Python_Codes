# Write a program to use yield in a custom iterator.
print('Q56_YieldIterator.py')

# Custom iterator class using yield
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n  # yield pauses and returns value
            n -= 1

# Using the custom iterator
print("Countdown from 5:")
for num in CountDown(5):
    print(num, end=" ")

print("\n\nCountdown from 10:")
for num in CountDown(10):
    print(num, end=" ")

# Another example: Custom range iterator
class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

print("\n\nCustom Range from 1 to 10:")
for num in CustomRange(1, 11):
    print(num, end=" ")

# Example: Even numbers iterator
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        n = 0
        while n <= self.limit:
            yield n
            n += 2

print("\n\nEven numbers up to 20:")
for num in EvenNumbers(20):
    print(num, end=" ")
