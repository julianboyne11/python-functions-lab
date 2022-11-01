#Challenge 1

from re import A


def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(10))

#Challenge 2

def largest(list):
  max = list[0]
  for n in list:
    if n > max:
      max = n
  return max

print(largest([1, 2, 3, 4, 0]))
