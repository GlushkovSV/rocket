class STAGE:
    def __init__(self):
        self.parts = list()

    def add_part(self, part):
        self.parts.append(part)

    def mass(self) -> float:
        """
        не python-way переписать. Возможно лучше так
        return sum(part.mass() for part in self.parts)

        :return:
        """
        total_mass = 0
        for part in self.parts:
            total_mass += part.mass()
        return total_mass

    def __str__(self):
        return '\n'.join(str(part) for part in self.parts)
