#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  num_batches = []
  for item in recipe:
    if not item in ingredients:
      return 0
    else:
      num_batches.append(ingredients[item] // recipe[item])
  return min(num_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))