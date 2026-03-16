class Guitar:
    def __init__(self, Name ="", Year = 0, Cost = 0):
        self.Name = Name
        self.Year = Year
        self.Cost = Cost

    def __str__(self):
        return f"{self.Name}, year:{self.Year},cost:{self.Cost}"

    def __lt__(self, other):
        """Compare two guitars by year - allows guitars.sort() to work."""
        return self.Year < other.Year