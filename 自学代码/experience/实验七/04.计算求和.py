import timeit
import time


def calculate():
    sum = 0
    for i in range(1, 10001):
        sum += i
    print("计算结果为：", sum)


if __name__ == "__main__":
    # calculate()
    run_time = timeit.timeit(stmt=calculate, number=1)
    print('run_time: ', run_time)
