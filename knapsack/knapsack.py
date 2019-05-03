#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  # initialize sack of items which we'll fill up
  sack = []

  # new list of tuples with an extra index for value/weight ratio
  ratios = []

  # loop through items and fill up ratios list with value/weight ratios as well as info that's currently in the item
  for i in range(0, len(items)):
    ratios.append((i+1, items[i][1], (items[i][2] / items[i][1]), items[i][2]))
  
  # sort ratios list by the key in the tuple which defines the v/w ratio, then reverse it so largest is first
  sorted_ratios = sorted(ratios, key = lambda x: x[2])[::-1]

  
  # here we'll continue checking the first element of sorted_ratios and then removing it until sorted_ratios is empty
  while len(sorted_ratios) > 0:
    # if the weight of first item is less then our capacity
    if sorted_ratios[0][1] < capacity:
      # reduce capacity by weight of item
      capacity -= sorted_ratios[0][1]
      # add tuple of (item_index, item_value) to sack
      sack.append((sorted_ratios[0][0], sorted_ratios[0][3]))
      # get rid of first element of list
      sorted_ratios = sorted_ratios[1:]
    # weight of first item too much to carry
    else:
      # get rid of first element of list
      sorted_ratios = sorted_ratios[1:]
  

  chosen = []
  value = 0

  # loop through our tuples and just return the indexes we care about
  # also sum up the value of each chosen item
  for i in sack:
    chosen.append(i[0])
    value += i[1]
  

  return {'Value': value, 'Chosen': sorted(chosen)}

  
      
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')