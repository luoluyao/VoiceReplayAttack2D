import numpy as np
import math


length_of_side = 58 * np.cos(0.25 * math.pi)

length_of_diagonal = 82 ##8.2cm

dd = [0, 50, 0, 25] # t:0, o:+5cm, l:0, i:+2.5cm


def cal_values(D, angle):
    '''
    :param D: distance
    :param angle: angle
    :return: three pairs microphone tdoa
    '''
    angle1 = angle
    angle2 = 90 - angle
    angle3 = 180 - angle1
    angle4 = 90 + angle1

    cos_angle1 = round(np.cos(math.pi / 180.0 * angle1), 6)
    cos_angle2 = round(np.cos(math.pi / 180.0 * angle2), 6)
    cos_angle3 = round(np.cos(math.pi / 180.0 * angle3), 6)
    cos_angle4 = round(np.cos(math.pi / 180.0 * angle4), 6)

    y1_power_2 = pow(D, 2) + pow(length_of_side, 2) - 2 * cos_angle1 * D * length_of_side
    y2_power_2 = pow(D, 2) + pow(length_of_side, 2) - 2 * cos_angle2 * D * length_of_side
    y3_power_2 = pow(D, 2) + pow(length_of_side, 2) - 2 * cos_angle3 * D * length_of_side
    y4_power_2 = pow(D, 2) + pow(length_of_side, 2) - 2 * cos_angle4 * D * length_of_side

    y1 = pow(y1_power_2, 0.5)
    y2 = pow(y2_power_2, 0.5)
    y3 = pow(y3_power_2, 0.5)
    y4 = pow(y4_power_2, 0.5)
    y12 = round(y1 - y2, 2)
    y13 = round(y1 - y3, 2)
    y14 = round(y1 - y4, 2)
    return [y12, y13, y14]


def theory_value_distance(dis):
    '''
    different distances
    :param dis:
    :return:
    '''
    dd = [0, 50, 0, 25]
    result = []
    for d in dd:
        result.append(cal_values(dis + d, 40))
    results = []
    for i in range(3):
        for j in range(1,4):
            results.append(round(result[j][i] - result[0][i],2))
    print results

def theory_value_angle(angle):
    '''
    calc different angle
    :param angle:
    :return:
    '''

    result = []
    for d in dd:
        result.append(cal_values(200 + d, angle))
    results = []

    for i in range(3):
        for j in range(1,4):
            results.append(round(result[j][i] - result[0][i],2))
    print results

def main():
    # different distance
    for dis in range(100, 550, 50):
        theory_value_distance(dis)

    # different angle
    # for angle in range(0, 181, 10):
    #     theory_value_angle(angle)

if __name__ == '__main__':
    main()
