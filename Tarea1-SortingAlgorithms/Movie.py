class Movie:
    def __init__(self, id, year, name):
        self.id = id
        self.year = year
        self.name = name

    def __eq__(self, other):
        if self.id < other.id:
            return -1
        else:
            return 1

    def __str__(self):
        return "{" + self.id.__str__() + ", " + self.year.__str__() + ", " + self.name.__str__() + "}"