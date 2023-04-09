from math import pi


class RingFrame:
    """ Class for RingFrame (Shpangout) """
    def __init__(self,
                 name: str = '',
                 r: float = 0,
                 struct_mass: float = 0) -> None:
        self.name = name
        self.r = r
        self.struct_mass = struct_mass

    def __str__(self) -> str:
        return f'RingFrame {self.name}:\n' \
               f'Radius={self.r}\n' \
               f'Mass={self.mass()}\n'

    def mass(self) -> float:
        return self.struct_mass


class Bottom:
    """ Class for Bottoms (front and rear) Tanks """
    def __init__(self,
                 name: str = '',
                 r: float = 0,
                 rm: float = 0,
                 struct_mass: float = 0) -> None:
        """
        :param name: имя днища
        :param r: радиус стыкуемого отсека
        :param rm: радиус кривизны меридиана
        :param struct_mass: масса днища
        """
        self.name = name
        self.r = r
        self.rm = rm
        self.struct_mass = struct_mass

    def __str__(self) -> str:
        return f'TankBottom {self.name}:\n' \
               f'Radius={self.r}\n' \
               f'Mass={self.mass()}\n'

    def mass(self) -> float:
        return self.struct_mass

    def centroid(self) -> float:
        """
        Надо найти формулу расчета центра масс части сферической поверхности

        :return:
        """
        return 3/8 * self.rm


class PART:
    """ Base class for parts of stage rockets """
    def __init__(self,
                 name: str = '',
                 r_top: float = 0,
                 r_bottom: float = 0,
                 length: float = 0,
                 struct_mass: float = 0,
                 **kwargs) -> None:
        self.name = name
        self.r_top = r_top
        self.r_bottom = r_bottom
        self.length = length
        self.struct_mass = struct_mass

    def __str__(self) -> str:
        return f'Part {self.name}:\n' \
               f'R top={self.r_top}\n' \
               f'R bottom={self.r_bottom}\n' \
               f'Length={self.length}\n' \
               f'Centroid={self.centroid():.2f}\n' \
               f'Mass={self.mass()}\n'
# f'Centroid={self.centroid()}\n' \

    def mass(self) -> float:
        return self.struct_mass

    def centroid(self) -> float:
        r1, r2 = self.r_top, self.r_bottom
        h = self.length
        return h / 3 * (1 + r2 / (r1 + r2))


class PHO(PART):
    pass


class TankFuel(PART):
    # Класс для баков вообще, неважно горючего или окислителя
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fuel_mass = 0
        self.fuel_density = 0
        self.front_bottom_r = kwargs.get('front_bottom_r', 0)
        self.rear_bottom_m = kwargs.get('rear_bottom_r', 0)

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
        fuel_height = fuel_volume / (pi * self.r_bottom**2)
        fuel_centroid = self.length - fuel_height
        return fuel_volume, fuel_height, fuel_centroid

    def centroid(self) -> float:
        struct_centroid = super().centroid()
        fuel_volume, fuel_height, fuel_centroid = self.fuel_geom_calc()
        return (struct_centroid * self.struct_mass + fuel_centroid * self.fuel_mass) / self.mass()

    def __str__(self) -> str:
        return ''.join([super().__str__(), f'within FuelMass={self.fuel_mass} kg\n'])


class Engine(PART):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.trust = 0  # Тяга, Н
        self.impulse = 0  # Удельный импульс
        self.angle = 0  # Угол отклонения сопла (или вектора тяги?), град?рад?
        self.consumption_fuel = 0  # Массовый расход горючего кг/с
        self.consumption_oxi = 0  # Массовый расход окислителя кг/с
        self.tank_fuel = None  # Ссылка на бак горючего
        self.tank_oxi = None  # Ссылка на бак окислителя

    def associate_tank(self, tank_fuel: TankFuel, tank_oxi: TankFuel):
        self.tank_fuel = tank_fuel
        self.tank_oxi = tank_oxi

    def set_consumption(self, consumption_fuel: float = 0, consumption_oxi: float = 0) -> None:
        """
        стоит переработать чтобы бросать исключение, пока для отладки оставил вывод сообщение в консоль
        :param consumption_fuel:
        :param consumption_oxi:
        :return:
        """
        if self.tank_fuel and self.tank_oxi:
            self.consumption_fuel = consumption_fuel
            self.consumption_oxi = consumption_oxi
        else:
            print('before setting consumption need associate fuel and oxi tank to engine')

    def __str__(self) -> str:
        if self.tank_fuel and self.tank_oxi:
            return ''.join([super().__str__(), f'fuel={self.tank_fuel.name}\n', f'oxi={self.tank_oxi.name}\n'])
        return super().__str__()


class Payload(PART):
    def centroid(self) -> float:
        return self.length / 2


class NoseCone(PART):
    pass
