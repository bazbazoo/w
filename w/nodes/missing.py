from os import remove
from web import notfound, data

from actual import ActualNode
from ..utils import J

class MissingNode(ActualNode):

  def _POST(self):
    done = False
    try:
      with open(self.path, 'wb') as f:
        f.write(data())
      done = True
    finally:
      try:
        done or remove(self.path)
      except OSError:
        pass

  def __reply(self):
    notfound()
    return "not found"

  def _GET(self):    return self.__reply()
  def _PUT(self):    return self.__reply()
  def _DELETE(self): return self.__reply()

  def resolve(self, path):
    if path is None: return self
    return MissingNode(J(self.path, path), self)