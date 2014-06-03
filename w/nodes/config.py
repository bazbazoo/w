from os.path import isdir

from ..utils import J

class __Config(object):
  pass

def load_config(path, parent_config = None):
  if not isdir(J(path, '.w')): return parent_config
  return __Config()