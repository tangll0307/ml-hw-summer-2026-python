class NumberStorage:
    """Handles data initialization, insertion, and search for a list of numbers."""

    def __init__(self):
        # Data initialization
        self.numbers = []

    def insert(self, value):
        # Data insertion
        self.numbers.append(value)

    def search(self, value):
        # Data search: returns 1-based index if found, otherwise -1
        if value in self.numbers:
            return self.numbers.index(value) + 1
        return -1
