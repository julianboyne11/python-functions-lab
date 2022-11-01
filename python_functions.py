#Challenge 1

from re import A


def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

# print(sum_to(10))

#Challenge 2

def largest(list):
  max = list[0]
  for n in list:
    if n > max:
      max = n
  return max

# print(largest([1, 2, 3, 4, 0]))

#Challenge 3

def occurrences(str1, substr2):
  return str1.count(substr2)
  # count = 0
  # for char in str1:
  #   if char == substr2:
  #     count += 1
  # return count

# print(occurrences('fleep floop', 'p'))

#Challenge 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(-1, 4))
