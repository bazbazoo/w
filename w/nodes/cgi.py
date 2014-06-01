from subprocess import Popen, PIPE
from web import ctx, data

from common import protected
from node import Node

class CGINode(Node):
  def __init__(self, path, parent, rest = None):
    Node.__init__(self, path, parent)
    self.__rest = rest

  def resolve(self, path):
    assert self.__rest is None
    return self.__class__(self.path, self.parent, rest=path)

  @protected
  def __call__(self, method):
    cmd = [self.path, method, self.__rest or '']
    env = dict(filter(lambda i: type(i[1]) == str, ctx.env.items()))
    p = Popen(cmd, env = env, stdin = PIPE, stdout = PIPE, stderr = PIPE)
    out, err = p.communicate(data())
    print err
    return out
