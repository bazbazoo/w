from errno import EACCES, ENOTDIR

from web import forbidden, internalerror

def protect(what, *a, **kw):
  try:
    return what(*a, **kw) or ""
  except (IOError, OSError) as e:
    if e.errno in [EACCES, ENOTDIR]:
      forbidden()
    else:
      internalerror()
    return str(e)

def protected(what):
  return lambda *a, **kw: protect(what, *a, **kw)