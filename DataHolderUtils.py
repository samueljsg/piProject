class TimeValueHolder(object):
    def __init__(self, value, time_in_millis):
        self.value = value
        self.time_in_millis = time_in_millis


def derivative(time_value_one: TimeValueHolder, time_value_two: TimeValueHolder) -> float:
    value_difference = time_value_two.value - time_value_one.value
    if value_difference == 0.0:
        return 0.0
    time_difference = (time_value_two.time_in_millis - time_value_one.time_in_millis) / 1000.0
    if time_difference == 0:
        return 0
    return value_difference / time_difference


def derivative(value_one: float, time_one: int, value_two: float, time_two: int) -> float:
    return derivative(TimeValueHolder(value_one, time_one), TimeValueHolder(value_two, time_two))


class FixedNumberArray(list):
    def __init__(self, array_size=30):
        self._max_size = array_size

    def append(self, item):
        if not isinstance(item, (float, int)):
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
        if not isinstance(key, int):
            raise TypeError("Key must be index")
        if not isinstance(value, (int, float)):
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
        try:
            # print("Time: ", time, " Value: ", value)
            # print(isinstance(time, (float, int)), type(value))
            self.value_array.append(value)
            self.time_array.append(time)
        except:
            print("Not allowed type")

    def get_average_value(self) -> float:
        return self.value_array.average()

    def get_derivative_first_two(self) -> TimeValueHolder:
        time_value_one = TimeValueHolder(self.value_array[0], self.time_array[0])
        time_value_two = TimeValueHolder(self.value_array[1], self.time_array[1])
        return TimeValueHolder(derivative(time_value_one, time_value_two),
                               (time_value_two.time_in_millis - time_value_one.time_in_millis) * 1000.0)
