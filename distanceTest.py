from ExtendedDistanceSensor import ExtendedDistanceSensor
from DistanceVelocityHolder import DistanceVelocityHolder
from time import sleep


def distance_updated(new_distance):
    print("New distance: ", new_distance)


sensor = ExtendedDistanceSensor(echo=24, trigger=23)
sensor.bind_to(distance_updated)
while True:
    # distance_velocity = sensor.get_distance_velocity()
    #print("Distance: ", distance_velocity.distance, " Velocity: ", distance_velocity.velocity)
    #print(sensor.distance)
    #print("Hello")
    sleep(1)
