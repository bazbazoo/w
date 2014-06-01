from web import notfound

from actual import ActualNode

class MissingNode(ActualNode):
  def _POST(self):
    # TODO: maybe write file.
    raise NotImplementedError()

  def __reply(self):
    notfound()
    return "not found"

  def _GET(self):    return self.__reply()
  def _PUT(self):    return self.__reply()
  def _DELETE(self): return self.__reply()

  def _POST(self):
    # TODO
    raise NotImplementedError()

  def resolve(self, path):
    return self