#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  combos = [1, 1, 2]
  if n < 3:
    total_combos = combos[n]
  else:
    for num_cookies in range(3, n):
      combos.append(combos[0] + combos[1] + combos[2])
      combos.pop(0)
    total_combos = sum(combos)
  return total_combos

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')