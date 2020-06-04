

class TimeValueHolder(object):
    def __init__(self, value, time_in_millis):
        self.value = value
        self.time_in_millis = time_in_millis


def derivative(time_value_one: TimeValueHolder, time_value_two: TimeValueHolder):
    value_difference = time_value_two.value - time_value_one.value
    if value_difference == 0.0:
        return 0.0
    time_difference = (time_value_two.time_in_millis - time_value_one.time_in_millis) / 1000.0
    if time_difference == 0:
        return 0
    return value_difference/time_difference


class FixedNumberArray(list):
    def __init__(self, array_size=30):
        self._max_size = array_size

    def append(self, item):
        if (not type(item) is float) or (not type(item) is int):
            raise TypeError("Only floats and ints are allowed")
        list.append(self, item)
        if len(self) > self._max_size:
            del self[0]

    def insert(self, __index: int, __object: float or int) -> None:
        if __index > self._max_size:
            raise OverflowError("Index must be " + self._max_size + " or less")
        self[__index] = __object

    def extend(self, __iterable: [float or int]) -> None:
        for item in __iterable:
            self.append(item)

    def __setitem__(self, key, value):
        if not type(key) is int:
            raise TypeError("Key must be index")
        if (not type(value) is float) or (not type(value) is int):
            raise TypeError("Value must be a float or int")
        self[key] = value

    def average(self) -> float:
        if len(self) == 0:
            raise IndexError("There are no values in the list")
        else:
            temp_var = 0.0
            for i in range(len(self)):
                temp_var += self[i]
            return temp_var / len(self)


class FixedArrayTwoPoint:
    def __init__(self, array_size=30):
        self._max_size = array_size
        self.value_array = FixedNumberArray(array_size)
        self.time_array = FixedNumberArray(array_size)

    def add(self, time_value_holder: TimeValueHolder):
        self.value_array.append(time_value_holder.value)
        self.time_array.append(time_value_holder.time_in_millis)

    def add(self, value: float, time: int):
        self.value_array.append(value)
        self.time_array.append(time)
        print("Time: ", time, " Value: ", value)
