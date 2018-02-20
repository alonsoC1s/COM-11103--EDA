class Movie:
    def __init__(self, id, year, name):
        self.id = id
        self.year = year
        self.name = name

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return "{" + self.id.__str__() + ", " + self.year.__str__() + ", " + self.name.__str__() + "}"