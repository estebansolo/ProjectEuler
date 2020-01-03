def multiples(number):
  """
  The range function returns range object, It is a sequence of integers,
  I use list comprehension to create a list just after valite the numbers
  """
  
  numbers = [
    num for num in range(number)
    if not num % 3 or not num % 5
  ]
  
  """
  The sum function takes an iterable and returns the sum of the items.
  """
  return sum(numbers)

assert multiples(1000) == 233168, "Excepted 233168"
assert multiples(49) == 543, "Excepted 543"
assert multiples(19564) == 89301183, "Excepted 89301183"
assert multiples(8456) == 16687353, "Excepted 16687353"
