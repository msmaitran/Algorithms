#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ["rock", "paper", "scissors"]
  plays = []
  def combos(play, hand):
    if play == 0:
      plays.append(hand)
      return
    else:
      for option in rps:
        combos(play - 1, hand + [option])
  combos(n, [])
  return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')