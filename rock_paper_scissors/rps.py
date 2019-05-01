#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  result = []
  options = [['rock'], ['paper'], ['scissors']]

  
  if n == 0:
    return [[]]
  elif n == 1:
    return options
  else:
    for i in range(len(options)):
      for j in range(len(rock_paper_scissors(n-1))):
        result += [options[i] + rock_paper_scissors(n-1)[j]]
    return result



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')