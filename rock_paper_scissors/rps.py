#!/usr/bin/python

import sys
from time import time 

def rock_paper_scissors(n):
  result = []
  options = [['rock'], ['paper'], ['scissors']]

  
  if n == 0:
    return [[]]
  elif n == 1:
    return options
  else:
    rps1 = rock_paper_scissors(n-1)
    for i in range(len(options)):
      for j in range(3**(n-1)):
        result += [options[i] + rps1[j]]
    return result

start = time()
rock_paper_scissors(6)
end = time()
print(end - start)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')