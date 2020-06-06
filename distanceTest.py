from ExtendedDistanceSensor import ExtendedDistanceSensor
from DistanceVelocityHolder import DistanceVelocityHolder
from DataHolderUtils import FixedArrayTwoPoint, TimeValueHolder
from time import sleep

fixed_distance_arr = FixedArrayTwoPoint(30)
fixed_velocity_arr = FixedArrayTwoPoint(30)
fixed_acceleration_arr = FixedArrayTwoPoint(30)


def updated_distance(distance: float, time: int):
    holder = TimeValueHolder(distance, time)
    fixed_distance_arr.add(holder)
    try:
        fixed_velocity_arr.add(fixed_distance_arr.get_derivative_first_two())
    except:
        # This means the distance array isn't ready yet
        pass
    try:
        fixed_acceleration_arr.add(fixed_velocity_arr.get_derivative_first_two())
    except:
        # This means the distance array isn't ready yet
        pass


sensor = ExtendedDistanceSensor(echo=24, trigger=23)

# sensor.bind_to(fixed_distance_arr.add)
# sensor.bind_to(distance_updated)
sensor.bind_to(updated_distance)
while True:

    sleep(.200)
    try:
        print("Distance: ", fixed_distance_arr.get_average_value(), "cm ", "Velocity: ",
              fixed_velocity_arr.get_average_value(), "cm/s ",
              "Acceleration: ", fixed_acceleration_arr.get_average_value(), "cm/s^2")
    except:
        pass
