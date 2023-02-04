__author__ = 'aman.rv'

import random

# Make RNG return consistent values for testing purposes.
random.seed(1)

"""
Toy class which generates monotonically increasing integers until the RNG
produces the maximum number in the defined range.
"""


class RandomIncreasingIterator:
    def __init__(self, increment_range):
        self._val = 0
        self._increment_range = increment_range

    def __iter__(self):
        return self

    def __next__(self):
        gap = random.randint(0, self._increment_range)
        if gap == self._increment_range:
            raise StopIteration()
        else:
            self._val += gap
            return self._val

    def __repr__(self):
        return f"{self.__class__.__name__}(increment_range={self._increment_range})"


def sort_streams(streams, n_streams):
    """
   streams: list[list], n parallel input streams of monotonically increasing integers
   n_streams: int, number of streams
   """

    # pos_dict: A dictionary to store the current pointer of each stream
    pos_dict = {}
    # total_entity_count: To store the sum of the count of integers in each stream
    total_entity_count = 0
    for i in range(n_streams):
        pos_dict[i] = 0
        total_entity_count += len(streams[i])

    while sum(pos_dict.values()) < total_entity_count:
        curr_smallest_number = float("inf")
        stream_with_smallest_number = 0

        # Loop through each stream and check the smallest integer at the current position of the pointer
        for i in range(n_streams):
            if pos_dict[i] < len(streams[i]) and curr_smallest_number > streams[i][pos_dict[i]]:
                curr_smallest_number = streams[i][pos_dict[i]]
                stream_with_smallest_number = i

        # Print the result and increment the pointer of the curr position by 1
        print(curr_smallest_number, end=" ")
        pos_dict[stream_with_smallest_number] += 1


if __name__ == '__main__':
    NUM_ITERATORS = 3
    inputs = [RandomIncreasingIterator(10) for _ in range(NUM_ITERATORS)]
    # Converting the streams of iterators into list dtypes for easy operations
    for i in range(NUM_ITERATORS):
        inputs[i] = list(inputs[i])

    print(inputs)
    sort_streams(inputs, NUM_ITERATORS)

    # # Feel free to start with small numbers, but what happens with large numbers?
    # NUM_ITERATORS = 1000
    # inputs = [RandomIncreasingIterator(100000) for _ in range(NUM_ITERATORS)]
    # for i in range(NUM_ITERATORS):
    #     inputs[i] = list(inputs[i])
    # print(inputs)
    # sort_streams(inputs, NUM_ITERATORS)
