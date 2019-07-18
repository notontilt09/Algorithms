#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # an array that holds the number of batches we can make per ingredient 
  multiples = []
  # loop through the recipe items
  for item in recipe:
    # if the recipe item isn't in ingredients return 0
    if item not in ingredients:
      return 0
    # otherwise append the max batches we can make just using that ingredient
    else:
      multiples.append( ingredients[item] // recipe[item] )
  
  # final answer is the minimum of the multiples array
  return (min(multiples))



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))