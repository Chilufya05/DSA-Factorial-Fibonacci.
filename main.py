Python Code:
def print_fibonacci(n):
a, b = 0, 1
for _ in range(n):
print(a, end=" ")
a, b = b, a + b


Python Code:
def calculate_factorial(n):
if n == 0 or n == 1:
return 1
else:
return n * calculate_factorial(n - 1)
