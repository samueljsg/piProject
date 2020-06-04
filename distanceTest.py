from ExtendedDistanceSensor import ExtendedDistanceSensor
from DistanceVelocityHolder import DistanceVelocityHolder
from DataHolderUtils import FixedArrayTwoPoint
from time import sleep


def distance_updated(new_distance, time):
    if new_distance is not None:
        print("New distance: ", new_distance * 180.0)


sensor = ExtendedDistanceSensor(echo=24, trigger=23)
fixed_distance_arr = FixedArrayTwoPoint(30)
sensor.bind_to(fixed_distance_arr.add)
#sensor.bind_to(distance_updated)
while True:

    sleep(.200)
    try:
        print(fixed_distance_arr.get_derivative_first_two())
    except:
        pass
