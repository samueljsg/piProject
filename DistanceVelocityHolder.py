from queue import Queue
from DataHolderUtils import TimeDistanceHolder, FixedNumberArray


class DistanceVelocityHolder:
    def __init__(self, array_size=30):
        self.dis_time_queue = Queue(maxsize=array_size)
        self.vel_queue = Queue(maxsize=array_size)
        self.acc_queue = Queue(maxsize=array_size)

    def updateDistance(self, distance, time_in_millis) -> TimeDistanceHolder:
        self.dis_time_queue.put_nowait(TimeDistanceHolder(distance, time_in_millis))
