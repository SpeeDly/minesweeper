class Block():

    def __init__(self, coords=None):
        self.coords = coords
        self.value = 0
        self.is_visible = False
        self.display = None
        self.marked = False

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def reveal(self):
        self.is_visible = True
        return self.get_value()

    def make_bomb(self):
        self.value = -1

    def is_bomb(self):
        return self.value == -1

    def is_marked(self):
        return self.marked

    def increase(self, number=1):
        if not self.is_bomb():
            self.value += number

    def get_coords(self):
        return self.coords

    def toggle_mark(self):
        if self.marked:
            self.marked = False
        else:
            self.marked = True

    def refresh(self):
        self.display and self.display(self)

    def reset(self):
        self.value = 0
        self.is_visible = False
        self.marked = False

    def __repr__(self):
        if self.is_marked():
            return 'X'
        if self.is_bomb():
            return 'B'
        return str(self.get_value())
