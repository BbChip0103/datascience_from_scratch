import numpy as np
import time

def check_time(func, arg):
    start_time = time.clock()
    func(arg)
    end_time = time.clock()
    return end_time - start_time

def sum_of_squares(v):
    return np.sum(v**2)

def partial_difference_quotient(f, v, i, h):
    w = np.array([v_j + (h if j == i else 0) for j, v_j in np.ndenumerate(v)])
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.000001):
    return np.array([partial_difference_quotient(f, v, i, h)
                     for i in np.arange(v.size)])

def partial_difference_quotient_2(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return [(i-j)/h for i, j in zip(f(w), f(v))]

def estimate_gradient_2(f, v, h=0.000001):
    return [partial_difference_quotient_2(f, v, i, h)
            for i in range(len(v))]


def test():
    test_point_1 = [1, 2, 3]
    test_point_2 = [2, 1, 8]
    test_point_3 = [0, 0, 0]

    result_use_numpy = estimate_gradient(lambda v:v**2, np.array(test_point_1))
    print(result_use_numpy)

    result_no_numpy = estimate_gradient_2(lambda v:[i**2 for i in v], test_point_1)
    print(result_no_numpy)

    # result_time = check_time(sum_of_squares, np.array(test_list))


if __name__=='__main__':
    test()