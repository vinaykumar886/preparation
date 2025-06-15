# Day 1: Python Functional Programming Challenges

from functools import reduce

# Challenge 1: Square of even numbers
nums = [1, 2, 3, 4, 5, 6]
a = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
print("Squares of even numbers:", a)  

# Output: [4, 16, 36]

# Challenge 2: Count names that start with 'A'
nums = ['Ankit', 'Bob', 'Alice', 'Arjun', 'Charlie', 'Arya']
a = list(filter(lambda x: x[0] == 'A', nums))
print("Count of names starting with 'A':", len(a))  

# Output: 4

# Challenge 3: Product of all numbers using reduce
nums = [2, 3, 4, 5]
a = reduce(lambda x, y: x * y, nums)
print("Product of all numbers:", a)  

# Output: 120

# Challenge 4: Convert integers to strings
nums = [1, 2, 3, 4]
a = list(map(lambda x: str(x), nums))
print("Strings:", a)  

# Output: ['1', '2', '3', '4']

# Challenge 5: Capitalize each name in the list
names = ['vinay', 'zayen', 'brother', 'python']
a = list(map(lambda a: a.capitalize(), names))
print("Capitalized Names:", a)  

# Output: ['Vinay', 'Zayen', 'Brother', 'Python']
