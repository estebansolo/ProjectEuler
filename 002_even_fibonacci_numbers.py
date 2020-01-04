"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def even_fibonacci(numbers):
  a, b = 1, 2
  fibonacci = []
  for number in range(numbers):
    fibonacci.append(a)
    a, b = b, a + b

  even = [num for num in fibonacci if not num % 2]
  return sum(even)

assert even_fibonacci(10) == 44, "Expected 44"
assert even_fibonacci(18) == 3382, "Expected 3382"
assert even_fibonacci(23) == 60696, "Expected 60696"
assert even_fibonacci(43) == 350704366, "Expected 350704366"