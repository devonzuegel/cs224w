import matplotlib.pyplot as plt

# This flatten() method is inspired by a response to this StackOverflow post:
#   stackoverflow.com/questions/3204245/how-do-i-convert-a-tuple-of-tuples-to-a-
#   one-dimensional-list-using-list-comprehe
def flatten(l, ltypes=(list, tuple)):
  ltype, l, i = type(l), list(l), 0
  while i < len(l):
    while isinstance(l[i], ltypes):
      if not l[i]:
        l.pop(i)
        i -= 1
        break
      else:   l[i:i + 1] = l[i]
    i += 1
  return ltype(l)

# This method is derived from the approximate expression in 2g.
def q(r, q0):
  if r == 0:  return [q0]
  q_prev = flatten(q(r - 1, q0))
  q_last = q_prev[-1]
  if r == max_k - 1:  print 'q0 =', q0, '  =>   Q29 =', sum(q_prev)
  q_curr = (1 - (1 - p*q_last)**(n - 1)) * (1 - sum(q_prev))
  return flatten([q_prev, q_curr])

max_k = 30
n     = 10000
p     = 2.0 / n
q0_vals = [ (1.0/n)*(10**i) for i in xrange(0, 4) ]

for i, q0 in enumerate(q0_vals):
  plt.plot(range(0, max_k), q(max_k - 1, q0))
plt.savefig('./images/2i-plot.png')