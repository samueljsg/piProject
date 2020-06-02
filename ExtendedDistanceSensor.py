from gpiozero import DistanceSensor
from DistanceVelocityHolder import DistanceVelocityHolder
from time import sleep


class ExtendedDistanceSensor(DistanceSensor, object):
    default_time_step = 0.00001

    def __init__(self, echo, trigger):
        DistanceSensor.__init__(self, echo=echo, trigger=trigger)
        self._observers = []

    @property
    def distance(self):
        """
        Returns the current distance measured by the sensor in meters. Note
        that this property will have a value between 0 and
        :attr:`max_distance`.
        """
        return self.value * self._max_distance

    @distance.setter
    def distance(self, new_value):
        self.distance = new_value
        for callback in self._observers:
            callback(self.distance)

    @property
    def value(self):
        """
        Returns a value between 0, indicating the reflector is either touching
        the sensor or is sufficiently near that the sensor can't tell the
        difference, and 1, indicating the reflector is at or beyond the
        specified *max_distance*.
        """
        return super(ExtendedDistanceSensor, self).value

    @DistanceSensor.value.setter
    def value(self, new_value):
        self.value = new_value
        for callback in self._observers:
            callback(self.value)

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
