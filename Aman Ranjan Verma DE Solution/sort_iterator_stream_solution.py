# import random
#
# # Make RNG return consistent values for testing purposes.
# random.seed(1)
#
# """
# Toy class which generates monotonically increasing integers until the RNG
# produces the maximum number in the defined range.
# """
#
#
# class RandomIncreasingIterator:
#     def __init__(self, increment_range):
#         self._val = 0
#         self._increment_range = increment_range
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         gap = random.randint(0, self._increment_range)
#         if gap == self._increment_range:
#             raise StopIteration()
#         else:
#             self._val += gap
#             return self._val
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}(increment_range={self._increment_range})"
#
#
# def sort_streams_optimised(streams, n_streams):
#     flag = 1
#     while flag != n_streams:
#         temp_list = []
#         for i in range(n_streams):
#             # check to stop looking at the
#             temp_list.append(streams[i]._val)
#         curr_smallest_num = min(temp_list)
#         curr_smallest_num_stream = temp_list.index(curr_smallest_num)
#         # print(f"s{curr_smallest_num_stream}-{curr_smallest_num}", end=" ")
#         print(curr_smallest_num, end=" ")
#         try:
#             streams[curr_smallest_num_stream].__next__()
#         except StopIteration:
#             flag += 1
#
#
# if __name__ == '__main__':
#     NUM_ITERATORS = 3
#     inputs = [RandomIncreasingIterator(10) for _ in range(NUM_ITERATORS)]
#
#     for i in range(NUM_ITERATORS):
#         inputs[i].__next__()
#
#     print(inputs)
#     sort_streams_optimised(inputs, NUM_ITERATORS)
#
#     # Feel free to start with small numbers, but what happens with large numbers?
#     # NUM_ITERATORS = 1000
#     # inputs = [RandomIncreasingIterator(100000) for _ in range(NUM_ITERATORS)]
#     #
#     # for i in range(NUM_ITERATORS):
#     #     inputs[i].__next__()
#     #
#     # print(inputs)
#     # sort_streams_optimised(inputs, NUM_ITERATORS)
#
#
# 1 -> 9
# 2 -> 11 -> 13
# 3 -> 10 -> 15
#
# job()
#     final_queue
#     10 -> 11 -> 9
# spark_stream -> consume -> validation and correction -> sink
#
# validation
#
#
#
