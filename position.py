class Position:
    def __init__(self, makes, misses, pos_name, misses_type):
        self.makes = makes
        self.misses = misses
        self.pos_name = pos_name
        self.misses_type = misses_type

    def shooting_percentage(self):
        return (self.makes / self.misses) * 100

