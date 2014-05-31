from sys import maxint

from os.path import join as J

def S(p):
  ps = p.split('/', 1)
  assert len(ps) > 0
  if len(ps) == 1:
    return (ps[0], None)
  else:
    return (ps[0], ps[1])