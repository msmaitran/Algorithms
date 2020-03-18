#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = -10
  for current_min_price_so_far in range(0, len(prices)):
    for current_max_price_so_far in range(current_min_price_so_far + 1, len(prices)):
      max_profit_so_far = prices[current_max_price_so_far] - prices[current_min_price_so_far]
      if max_profit_so_far > max_profit:
        max_profit = max_profit_so_far
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))