import numpy as np
import time

def check_time(func, arg):
    start_time = time.clock()
    func(arg)
    end_time = time.clock()
    return end_time - start_time

def sum_of_squares(v):
    return np.sum(v**2)

def sum_of_squares_2(v):
    return sum([numb**2 for numb in v])

def test():
    test_list = list(range(1, 1000001))

    result_time = check_time(sum_of_squares, np.array(test_list))
    print(result_time, 'sec')

    result_time = check_time(sum_of_squares_2, test_list)
    print(result_time, 'sec')


if __name__=='__main__':
    test()