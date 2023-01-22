# import math as m
# import matplotlib.pyplot as plt
# import numpy as np


import part
import stage
# import rocket

# Создаем 2 ступень по отсекам
stage2 = stage.STAGE()

# Создаем головной обтекатель
nose_cone = part.NoseCone(name="GO", r_top=0, r_bottom=1.7, length=0.5, struct_mass=500)
stage2.add_part(nose_cone)
print(nose_cone)

# создаем полезную нагрузку
payload = part.Payload(name="KA", struct_mass=1000, length=1)
stage2.add_part(payload)
print(payload)

# Переходной отсек
pho2 = part.PHO(name='PhO_2_stage',
                r_top=1.5,
                r_bottom=1.5,
                length=1.25,
                struct_mass=1200)
stage2.add_part(pho2)
print(pho2)

# Бак горючего
tank_fuel_2_stage = part.TankFuel(name='TankFuel_2_stage',
                                  r_top=1.5, r_bottom=1.5,
                                  length=7,
                                  struct_mass=2000)
stage2.add_part(tank_fuel_2_stage)
tank_fuel_2_stage.fill_tank(fuel_mass=5000, fuel_density=440)
print(tank_fuel_2_stage)

print(stage2.mass())
print(stage2)
