#!/usr/bin/python

import sys
from time import time

def making_change(amount, denominations, cache=None):
  if cache == None:
    cache = [0 for i in range(amount+1)]
  
  cache[0] = 1
  
  for i in denominations:
    for higher_amount in range(i, amount+1):
      diff = higher_amount - i
      cache[higher_amount] += cache[diff] 
  
  return cache[amount]

start = time()
print(making_change(12, [1, 5, 10, 25, 50]))
end = time()
print('time', end - start)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")