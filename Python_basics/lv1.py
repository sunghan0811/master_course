# 행렬 곱셈
import numpy as np
a = np.matrix([[1, 2], [4, 5], [7, 8]]) # 2*3
b = np.matrix([[2, 0, 0], [0, 2, 0]]) # 3 * 2
a * b
b * a


def solution(arr1, arr2):
    a = np.matrix([[1, 2], [4, 5], [7, 8]]) # 2*3
    b = np.matrix([[2, 0, 0], [0, 2, 0]]) # 3 * 2
    answer = a * b
    return answer


