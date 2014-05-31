from web import notfound

from actual import ActualNode

class MissingNode(ActualNode):
  def _POST(self):
    # TODO: maybe write file.
    raise NotImplementedError()

  def _GET(self):
    notfound()
    return "not found"

  def _PUT(self):
    return self._GET()

  def _DELETE(self):
    return self._GET()

  def resolve(self, path):
    return self