import operator
from collections import defaultdict


num_pos, num_neg = 0, 0

with open('./data/epinion_signed.txt') as f:
  for line in f:
    tokens = line.split()
    if not tokens[0].isdigit():    continue
    _, _, sign = tokens
    if int(sign) > 0:     num_pos += 1
    elif int(sign) < 0:   num_neg += 1

print num_pos
print num_neg