from subprocess import Popen, PIPE
from sys import maxint
from web import ctx, data
import shlex
from os import access, X_OK
from os.path import isfile, join as J

def S(p):
  ps = p.split('/', 1)
  assert len(ps) > 0
  if len(ps) == 1:
    return (ps[0], None)
  else:
    return (ps[0], ps[1])

def execute(command, env, data):
  p = Popen(shlex.split(command), env = env, stdin = PIPE, stdout = PIPE, stderr = PIPE)
  out, err = p.communicate(data)
  return p.poll(), out, err

def wexecute(command, extra_env = dict()):
  env = ctx_env()
  env.update(extra_env)
  return execute(command, env, data())

def ctx_env():
  return dict(filter(lambda i: type(i[1]) == str, ctx.env.items()))

def is_exec_file(path):
  return isfile(path) and access(path, X_OK)