class PART:
    def __init__(self, r_top=0, r_bottom=0, length=0):
        self.r_top = r_top
        self.r_bottom = r_bottom
        self.length = length


class PHO(PART):
    def __init__(self,
                 r_top=0,
                 r_bottom=0,
                 length=0,
                 payload=0):
        super().__init__(r_top, r_bottom, length)
        self.payload = payload


class TankFuel(PART):
    def __init__(self,
                 r_top=0,
                 r_bottom=0,
                 length=0,
                 fuel_density=0):
        super().__init__(r_top, r_bottom, length)
        self.density = fuel_density


class TankOxi(PART):
    def __init__(self,
                 r_top=0,
                 r_bottom=0,
                 length=0,
                 oxi_density=0):
        super().__init__(r_top, r_bottom, length)
        self.density = oxi_density


class Engine(PART):
    def __init__(self, thrust=0, mass=0):
        super().__init__()
        self.thrust = thrust
        self.mass = mass


class PAYLOAD(PART):
    def __init__(self, mass=0):
        super().__init__()
        self.mass = mass
