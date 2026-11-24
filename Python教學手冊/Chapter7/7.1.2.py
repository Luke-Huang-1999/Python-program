class Sphere:
    def __init__(self, r):
        self.rad = r

    def volume(self):
        return 4 * 3.14 * self.rad**3 / 3

    def surface_area(self):
        return 4 * 3.14 * self.rad**2

s0 = Sphere(2)
print(s0.volume())
print(s0.surface_area())