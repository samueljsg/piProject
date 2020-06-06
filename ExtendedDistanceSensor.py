from gpiozero import DistanceSensor
import time


def current_time() -> int:
    return int(round(time.time() * 1000))


class ExtendedDistanceSensor(DistanceSensor, object):
    default_time_step = 0.00001

    def __init__(self, echo, trigger, max_distance=1):
        DistanceSensor.__init__(self, echo=echo, trigger=trigger, max_distance=max_distance)
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

    def _read(self):
        for callback in self._observers:
            sensor_value = super(ExtendedDistanceSensor, self)._read()
            if sensor_value is not None:
                callback(sensor_value * 100, current_time())
