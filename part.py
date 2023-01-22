import math


class PART:
    """ Base class for parts of stage rockets """
    def __init__(self,
                 name: str = '',
                 r_top: float = 0,
                 r_bottom: float = 0,
                 length: float = 0,
                 struct_mass: float = 0) -> None:
        self.name = name
        self.r_top = r_top
        self.r_bottom = r_bottom
        self.length = length
        self.struct_mass = struct_mass

    def __str__(self):
        return f'Part {self.name}:\n' \
               f'R top={self.r_top}\n' \
               f'R bottom={self.r_bottom}\n' \
               f'Length={self.length}\n' \
               f'Centroid={self.centroid()}\n' \
               f'Mass={self.mass()}\n'

    def mass(self) -> float:
        return self.struct_mass

    def centroid(self) -> float:
        r1, r2 = self.r_top, self.r_bottom
        h = self.length
        return h / 3 * (1 + r2 / (r1 + r2))


class PHO(PART):
    pass


class TankFuel(PART):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fuel_mass = 0
        self.fuel_density = 0

    def fill_tank(self,
                  fuel_mass: float = 0,
                  fuel_density: float = 0) -> None:
        if self.fuel_mass == 0:
            self.fuel_mass = fuel_mass
            self.fuel_density = fuel_density
        else:
            self.fuel_mass += fuel_mass

    def mass(self) -> float:
        return self.struct_mass + self.fuel_mass

    def fuel_geom_calc(self) -> (float, float, float):
        """
        Пока формула работает только для цилиндра

        :return:
        объем топлива, высота уровня топлива, центр масс топлива
        """
        if self.fuel_density == 0:
            return 0, 0, 0
        fuel_volume = self.fuel_mass / self.fuel_density
        fuel_height = fuel_volume / (math.pi * self.r_bottom**2)
        fuel_centroid = self.length - fuel_height
        return fuel_volume, fuel_height, fuel_centroid

    def centroid(self) -> float:
        struct_centroid = super().centroid()
        fuel_volume, fuel_height, fuel_centroid = self.fuel_geom_calc()
        return (struct_centroid * self.struct_mass + fuel_centroid * self.fuel_mass) / self.mass()

    def __str__(self):
        return f'Part {self.name}:\n' \
               f'R top={self.r_top} m \n' \
               f'R bottom={self.r_bottom} m\n' \
               f'Length={self.length} m\n' \
               f'Mass={self.mass()} kg\n' \
               f'within FuelMass={self.fuel_mass} kg\n' \
               f'Centroid={self.centroid()} m\n'


class TankOxi(PART):
    pass


class Engine(PART):
    pass


class Payload(PART):
    def centroid(self) -> float:
        return self.length / 2


class NoseCone(PART):
    pass
