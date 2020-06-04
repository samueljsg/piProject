from gpiozero import DistanceSensor
from DistanceVelocityHolder import DistanceVelocityHolder
from time import sleep, time


def current_time() -> int:
    return int(round(time.time() * 1000))


class ExtendedDistanceSensor(DistanceSensor, object):
    default_time_step = 0.00001

    def __init__(self, echo, trigger):
        DistanceSensor.__init__(self, echo=echo, trigger=trigger)
        self._observers = []

    def bind_to(self, callback):
        self._observers.append(callback)

    def unregister_from(self, callback):
        try:
            self._observers.remove(callback)
        except:
            print("No observer existed")

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

    def _read(self):
        for callback in self._observers:
            callback(super(ExtendedDistanceSensor, self)._read(), current_time())
