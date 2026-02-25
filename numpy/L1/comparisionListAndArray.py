import timeit

sizeOfList = list(range(10000))
l1 = sizeOfList
l2 = sizeOfList

execution_time = timeit.timeit(lambda: l1 + l2, number=1000)

print("Average time:", execution_time / 1000)
