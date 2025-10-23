# Write a program to create iterators.

print("=== Iterator 1: Custom Counter Iterator ===\n")

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

# Using Counter iterator
counter = Counter(1, 10)
print("Counter from 1 to 10:")
for num in counter:
    print(num, end=" ")

print("\n\n=== Iterator 2: Reverse Iterator ===\n")

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Using Reverse iterator
rev = Reverse("Python")
print("Reverse of 'Python':")
for char in rev:
    print(char, end=" ")

print("\n\n=== Iterator 3: Even Numbers Iterator ===\n")

class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        result = self.num
        self.num += 2
        return result

# Using EvenIterator
evens = EvenIterator(20)
print("Even numbers up to 20:")
for num in evens:
    print(num, end=" ")

print("\n\n=== Iterator 4: Fibonacci Iterator ===\n")

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

# Using FibonacciIterator
fib = FibonacciIterator(10)
print("First 10 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")

print('\n\nThis code is written and executed by Kaivalaya Dua 0231BCA205')
