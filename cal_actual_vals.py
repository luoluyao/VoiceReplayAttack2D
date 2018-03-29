import numpy as np
import math

def actual_tdoa(x):
    '''
    calculate tdoa
    :param x:
    :return:
    '''
    length_of_side = 58
    length_of_diagonal = 82

    cos135 = -0.707

    p_p1_power2 = pow(length_of_side, 2) + pow(x, 2) - 2 * length_of_side * x * cos135
    p_p1 = pow(p_p1_power2, 0.5)
    p_p3 = p_p1

    result = []
    result.append(-length_of_diagonal)
    result.append(x - p_p1)
    result.append(x - p_p3)

    return result

def get_all_result(x):
    '''
    return all data
    :param x:
    :return:
    '''
    #distances = [0, -20, 2, 3] # need to calc
    distances = [0, 0, 0, 0]
    all_distances = [0 for i in range(12)]
    for i in range(len(distances)):
        dis_result = actual_tdoa(distances[i] + x)
        for j in range(3):
            all_distances[j * 4 + i] = round(dis_result[j],2)
    return all_distances

length_of_side = 58 * np.cos(0.25 * math.pi)

length_of_diagonal = 82

def cal_values(D, angle):

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


def main():
    # print "test", cal_values(200, 45)
    # print "cos45", np.cos(0.25 * math.pi)
    #distances = [100, 200, 300, 350, 400, 450, 500, 600, 800]
    # for dis in distances:
    #     print get_all_result(dis)
    # for i in range(100, 1000, 50):
    #     print str(i), get_all_result(i)
    # file_name = "angle_file"
    #file_name = "machine_file"
    file_name = "human_file"
    f = open(file_name, "w")

    # different distances and different angles
    # for angle in range(-89, 89, 10):
    #     f.write(str(angle))
    #     f.write("\n")
    #     for dis in range(100, 900, 100):
    #         res = cal_values(dis, angle)
    #         for r in res:
    #             f.write(str(round(r, 2)))
    #             f.write(" ")
    #         f.write("\n")
    #     f.write("\n")

    # machine file
    # for dis in range(100, 900, 50):
    #     res = cal_values(dis, 10)
    #     for j in  range(4):
    #         for r in res:
    #             f.write(str(round(r, 2)))
    #             f.write(" ")
    #     f.write("\n")

    # human file
    different_file_new = "different_file_new"
    different_file_name = "different_file_m1m2_p2-p1"
    corrcoeff_file_name = "corrcoeff_file"
    #corrcoeff_file_name = "corrcoeff_file_init"
    file_different = open(different_file_name, "w")
    file_corrcoeff = open(corrcoeff_file_name, "w")
    for angle in range(-90, 91, 5):
        f.write(str(angle))
        f.write("\n")
        file_different.write(str(angle))
        file_different.write(" ")
        file_corrcoeff.write(str(angle))
        file_corrcoeff.write(" ")
        for dis in range(100, 900, 50):
            machine_all_tdoa = []
            human_all_tdoa = []
            dis_phoneme = [0, 60, 0, 30]
            machine_dis_phoneme = [0, 0, 0, 0]
            for dis_p in dis_phoneme:
                res = cal_values(dis_p + dis, angle)
                print "res,angle,dis", angle,dis,res
                for r in res:
                    f.write(str(round(r, 2)))
                    f.write(" ")
                    human_all_tdoa.append(round(r, 2))
                f.write("\n")

            for m_dis_p in machine_dis_phoneme:
                m_res = cal_values(m_dis_p + dis, angle)
                for r in m_res:
                    machine_all_tdoa.append(round(r, 2))

            f.write("\n")
            f.write("\n")
            max_different = cal_values(dis_phoneme[1] + dis, angle)[0] - cal_values(dis, angle)[0]
            file_different.write(str(round(max_different, 2)))
            file_different.write(" ")
            print machine_all_tdoa
            print human_all_tdoa
            corrcoeff_value = np.corrcoef(machine_all_tdoa, human_all_tdoa)[0][1]
            file_corrcoeff.write(str(corrcoeff_value))
            file_corrcoeff.write(" ")

        f.write("\n")
        file_different.write("\n")
        file_corrcoeff.write("\n")
    file_different.close()
    # correlation coefficient
    f.close()

    # print get_all_result(185)
    # 100: 70
    # 200: 100
    # 300: 185
    # 500: 500 # wrong

def theory_value(dis):
    dd = [0, 50, 0, 25]
    result = []
    for d in dd:
        result.append(cal_values(dis + d, 40))
    results = []
    #print "dis:", dis, result
    for i in range(3):
        for j in range(1,4):
            results.append(round(result[j][i] - result[0][i],2))
    print results

def theory_value_angle(angle):
    dd = [0, 50, 0, 25]
    result = []
    for d in dd:
        result.append(cal_values(200 + d, angle))
    results = []
    print "angle:",angle, result
    for i in range(3):
        for j in range(1,4):
            results.append(round(result[j][i] - result[0][i],2))
    print results

if __name__ == '__main__':
    # main()
    # different distance
    for dis in range(100, 550, 50):
        theory_value(dis)
    # different angle
    # for angle in range(0, 181, 10):
    #     theory_value_angle(angle)
