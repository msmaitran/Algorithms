#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  permutation = [1, 1, 2]
  if n < 3:
    eating_cookies = permutation[n]
  else:
    for num_cookies in range(3, n):
      permutation.append(permutation[0] + permutation[1] + permutation[2])
      permutation.pop(0)
    eating_cookies = sum(permutation)
  return eating_cookies

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')