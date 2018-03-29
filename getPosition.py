import sys
import numpy as np
from math import sqrt
from math import isnan
from sympy import *

# triangle's three edges : 58, d , d
d = np.sqrt(58 * 58/2)

# data number for phoneme
phoneme_num = 4

def cal_position_multi(datas):
    '''
    Using cal_position to calculate all datas
    :param datas:
    :return:
    '''
    positions = []
    tmp = []
    count_num = 0
    for data in datas:
        print "count_num:", count_num
        tmp = []
        for d in data:
            r = cal_position(d[1], d[0], d[2])
            if r is not None and len(r) != 0:
                tmp.append(r)
            print "r:", r
        positions.append(tmp)
    return positions


def cal_position(r20, r21, r23):
    '''
    calculate the position using tdoa
    :param r12:
    :param r13:
    :param r14:
    :return: x, y, z, R
    '''
    r0 = Symbol('r0')
    r1 = Symbol('r1')
    r2 = Symbol('r2')
    r3 = Symbol('r3')
    #print r12,r13,r14
    result_r =  solve([r1 ** 2 + r3 ** 2 - r0 ** 2 - r2 ** 2,
             r21 - r2 + r1,
             r20 - r2 + r0,
             r23 - r2 + r3],
            [r0,r1,r2,r3])
    if len(result_r) == 0:
        print "[error]:solve failed"
        return
    r0 = result_r[0][0]
    r1 = result_r[0][1]
    r2 = result_r[0][2]
    r3 = result_r[0][3]

    x = (r2*r2 - r0*r0) / (4 * d)
    y = (r3*r3 - r1*r1) / (4 * d)
    R = sqrt(x*x + y*y)

    return round(x,2), round(y,2), round(R,2)

def main():
    str_name = "human"
    file_name = "log_" + str_name + "_80"
    file_name_write = "log_" + str_name + "_80_positions"

    count_wrong_data = 0
    count_all_data = 0
    data = read_file(file_name)
    print "data:", data
    datas = transform_data(data)
    print "datas:", datas
    position = cal_position_multi(datas)
    print "positions:", position
    f_write = open(file_name_write, "w")
    for p in position:
        for i in range(len(p)):
            f_write.write(str(i + 1))
            f_write.write(":")
            f_write.write(str(p[i]))
            f_write.write(" ")
        f_write.write("\n")
    f_write.close()
    print data
    print datas
    print position


def transform_data(datas):
    '''
    change data to formated data
    :param data:
    :return:
    '''
    result = []
    tmp = []
    for data in datas:
        for i in range(phoneme_num):
            tmp.append([d for d in data[i::phoneme_num]])
        result.append(tmp)
        tmp = []
    return result

def cmd_func(a, b):
    '''
    compare .wav name
    :param a:
    :param b:
    :return:
    '''
    return cmp(a, b)

def read_file(file_name):
    '''
    read file datas
    :param file_name:
    :return:
    '''
    file = open(file_name)
    test_data = file.readlines()
    line_count = 1
    datas = []
    tmp = []
    merge_tmp = []
    for t_data in test_data:
        t_data = t_data.strip()
        tmp.append(t_data)
        if (line_count % 3 == 0):
            tmp.sort(cmp=cmd_func)
            tmp = str(tmp).strip()
            tmp = tmp.replace('[', '')
            tmp = tmp.replace(']', '')
            tmp = tmp.replace('"', '')
            tmp_new = tmp.split(", ")
            for i in range(len(tmp_new)):
                if i % (phoneme_num + 2) == 0 or i % (phoneme_num + 2) == 1:
                    continue
                merge_tmp.append(float(tmp_new[i]))
            tmp = []
            datas.append(merge_tmp)
            merge_tmp = []
        line_count += 1
    file.close()
    return datas

if __name__ == "__main__":
    # main()

    ds = [[-82.0,  -46.85, -46.85]]
    #(10.04, -10.04, 14.2)

    ds = [[-80.0, -41.85, -41.85]]
    #(10.24, -10.24, 14.49)

    for dd in ds:
        print "dd", dd
        print "cal", cal_position(float(dd[1]), float(dd[0]), float(dd[2]))


# ['sound/log/test2.wav', 'sound/log/test3.wav', -15.94, -10.63, -15.94, -18.59]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -38.52, -42.5, -38.52, -41.17]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -17.27, -7.97, -17.27, -18.59]

# ['sound/log/test2.wav', 'sound/log/test0.wav', -75.7, -87.66, -57.11, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -38.52, -41.17, -38.52, -35.86]
# ['sound/log/test2.wav', 'sound/log/test3.wav', -39.84, -46.48, -42.5, -41.17]

# ['sound/log/test2.wav', 'sound/log/test3.wav', -37.19, -49.14, -37.19, -34.53]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -71.72, -85.0, -85.0, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -35.86, -42.5, -26.56, -35.86]