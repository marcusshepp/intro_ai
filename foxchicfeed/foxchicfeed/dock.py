class Dock():

    def __init__(self, items, side):
        self.items = items
        self.side = side

    def _has(self, name):
        # checks if dock has that item
        if len(self.items) > 0:
            print self.side
            print self.items[0].name
            print self.items[1].name
            print self.items[2].name
            if self.items[0].name == name:
                return True
            if self.items[1].name == name:
                return True
            if self.items[2].name == name:
                return True
            else: return False
        else: return False

    def valid_state(self):
        # print self.items[0].name
        # print self.items[1].name
        # print self.items[2].name

        if self._has("chicken") and self._has("fox"):
            return False
        if self._has("feed") and self._has("chicken"):
            return False
        if self._has("fox") and self._has("feed") and not self._has("chicken"):
            return True
        return "no logic hit"

    def remove(self, item):
        if self._has(item):
            self.items.remove(item)

    def add(self, item):
        if not self._has(item):
            self.items.append(item)
