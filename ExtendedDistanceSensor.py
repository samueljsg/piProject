from gpiozero import DistanceSensor
import DistanceVelocityHolder
from time import sleep


class ExtendedDistanceSensor(DistanceSensor):
    default_time_step = 0.00001

    def __init__(self, echo, trigger):
        DistanceSensor.__init(self, echo=echo, trigger=trigger)

    def get_average_distance(self, sample_size=5) -> float:
        distance_sum = 0
        for i in range(0, sample_size):
            distance_sum += self.distance * 180
        return distance_sum / sample_size

    def get_distance_velocity(self, time_step=default_time_step) -> DistanceVelocityHolder:
        distance1 = self.distance * 180
        sleep(time_step)
        distance2 = self.distance * 180
        velocity = distance2 - distance1 / time_step
        return DistanceVelocityHolder(distance2 - distance1 / 2, velocity)
