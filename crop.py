class Crop:
    """A generic food crop"""

def __init__(self,growth_rate, light_needed, water_needed):
    self._growth = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._light_needed = light_needed 
    self._water_needed = water_needed
    self._status = "Seed"
    self._type = "Generic"

def main():
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_needed)
    print(new_crop._water_needed)
    new_crop2 = Crop(2,5,7)
    print(new_crop2._status)
    print(new_crop2._light_needed)
    print(new_crop2._water_needed)


main()
