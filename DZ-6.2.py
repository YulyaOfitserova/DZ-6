class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class Mass(Road):

    def __init__(self, _length, _width, mass, thickness):
        super().__init__(_length, _width)
        self.mass = mass
        self.thickness = thickness

    def mass_off_asphalt(self):
        return self._length * self._width * self.mass * self.thickness


asphalt = Mass(10, 10, 10, 10)
print(asphalt.mass_off_asphalt())
