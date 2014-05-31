from web import notfound

from actual import ActualNode

def __reply():
  notfound()
  return "not found"

class MissingNode(ActualNode):
  def _POST(self):
    # TODO: maybe write file.
    raise NotImplementedError()

  def _GET(self):    __reply()
  def _PUT(self):    __reply()
  def _DELETE(self): __reply()

  def _POST(self):
    # TODO
    raise NotImplementedError()

  def resolve(self, path):
    return self