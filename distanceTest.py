from ExtendedDistanceSensor import ExtendedDistanceSensor
from time import sleep
sensor = ExtendedDistanceSensor(echo=18, trigger=17)
while True:
    distance_velocity = sensor.get_distance_velocity()
    print("Distance: ", distance_velocity.distance, " Velocity: ", distance_velocity.velocity)
    sleep(100/1000000)