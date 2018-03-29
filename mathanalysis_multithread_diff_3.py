import cal_actual_vals as cav
import numpy as np

def read_and_cal_avg():

    test_file_name = "different_samplerate/log_sample48k_merge"
    test_file_name_diff = test_file_name + "_diff"

    file = open(test_file_name)
    file_diff = open(test_file_name_diff, "w")
    '''
    diff
    '''
    test_corrcoeff_file_name = test_file_name_diff + "_corrcoeff"
    file_corr = open(test_corrcoeff_file_name, "w")

    '''
    diff corrcoeff
    '''
    test_diff_corrcoeff_file_name = test_corrcoeff_file_name + "_diff"
    file_corr_diff = open(test_diff_corrcoeff_file_name, "w")

    '''
    diff distances
    '''
    test_diff_dis_corrcoeff_file = test_diff_corrcoeff_file_name + "_dis_40angle"
    file_diff_dis_corrcoeff = open(test_diff_dis_corrcoeff_file, "w")

    '''
    diff angles
    '''
    test_diff_angle_corrcoeff_file = test_diff_corrcoeff_file_name + "_angle"
    file_diff_angle_corrcoeff = open(test_diff_angle_corrcoeff_file, "w")

    # arrays = [0.94, 0.0, 0.53, 0.0, 0.0, 0.0, 0.94, 0.0, 0.53]
    # arrays = [0.82, 0.0, 0.45, 0.0, 0.0, 0.0, 0.82, 0.0, 0.45]

    # different distance 0 angle
    arrays = [
        [2.58, 0.0, 1.53, 0.0, 0.0, 0.0, 2.58, 0.0, 1.53],
        [1.35, 0.0, 0.77, 0.0, 0.0, 0.0, 1.35, 0.0, 0.77],
        [0.82, 0.0, 0.45, 0.0, 0.0, 0.0, 0.82, 0.0, 0.45],
        [0.55, 0.0, 0.3, 0.0, 0.0, 0.0, 0.55, 0.0, 0.3],
        [0.39, 0.0, 0.21, 0.0, 0.0, 0.0, 0.39, 0.0, 0.21],
        [0.3, 0.0, 0.16, 0.0, 0.0, 0.0, 0.3, 0.0, 0.16],
        [0.23, 0.0, 0.12, 0.0, 0.0, 0.0, 0.23, 0.0, 0.12],
        [0.19, 0.0, 0.1, 0.0, 0.0, 0.0, 0.19, 0.0, 0.1],
        [0.15, 0.0, 0.08, 0.0, 0.0, 0.0, 0.15, 0.0, 0.08]]
    # different distance 40 angle
    arrays = [
    [0.49, 0.0, 0.28, -1.28, 0.0, -0.84, -0.93, 0.0, -0.63],
    [0.26, 0.0, 0.15, -0.44, 0.0, -0.27, -0.24, 0.0, -0.16],
    [0.16, 0.0, 0.09, -0.2, 0.0, -0.12, -0.08, 0.0, -0.05],
    [0.11, 0.0, 0.06, -0.11, 0.0, -0.06, -0.02, 0.0, -0.01],
    [0.07, 0.0, 0.04, -0.07, 0.0, -0.04, 0.0, 0.0, 0.0],
    [0.06, 0.0, 0.03, -0.04, 0.0, -0.02, 0.01, 0.0, 0.0],
    [0.04, 0.0, 0.02, -0.03, 0.0, -0.01, 0.01, 0.0, 0.0],
    [0.04, 0.0, 0.02, -0.02, 0.0, -0.01, 0.0, 0.0, 0.0],
    [0.02, 0.0, 0.01, -0.01, 0.0, 0.0, 0.01, 0.0, 0.01]
    ]


    # different angle 0 ~ 90
    # arrays = [
    #     [0.82, 0.0, 0.45, 0.0, 0.0, 0.0, 0.82, 0.0, 0.45],
    #     [0.81, 0.0, 0.45, -0.02, 0.0, -0.02, 0.71, 0.0, 0.39],
    #     [0.68, 0.0, 0.37, -0.07, 0.0, -0.04, 0.5, 0.0, 0.27],
    #     [0.45, 0.0, 0.25, -0.14, 0.0, -0.08, 0.22, 0.0, 0.12],
    #     [0.16, 0.0, 0.09, -0.2, 0.0, -0.12, -0.08, 0.0, -0.05],
    #     [-0.16, 0.0, -0.09, -0.24, 0.0, -0.14, -0.36, 0.0, -0.2],
    #     [-0.45, 0.0, -0.25, -0.23, 0.0, -0.14, -0.6, 0.0, -0.34],
    #     [-0.68, 0.0, -0.37, -0.19, 0.0, -0.11, -0.75, 0.0, -0.42],
    #     [-0.81, 0.0, -0.45, -0.1, 0.0, -0.06, -0.83, 0.0, -0.46],
    #     [-0.82, 0.0, -0.45, 0.0, 0.0, 0.0, -0.82, 0.0, -0.45],
    # ]
    # different angle 0 ~ 180
    # arrays = [
    #     [0.82, 0.0, 0.45, 0.0, 0.0, 0.0, 0.82, 0.0, 0.45],
    #     [0.81, 0.0, 0.45, -0.02, 0.0, -0.02, 0.71, 0.0, 0.39],
    #     [0.68, 0.0, 0.37, -0.07, 0.0, -0.04, 0.5, 0.0, 0.27],
    #     [0.45, 0.0, 0.25, -0.14, 0.0, -0.08, 0.22, 0.0, 0.12],
    #     [0.16, 0.0, 0.09, -0.2, 0.0, -0.12, -0.08, 0.0, -0.05],
    #     [-0.16, 0.0, -0.09, -0.24, 0.0, -0.14, -0.36, 0.0, -0.2],
    #     [-0.45, 0.0, -0.25, -0.23, 0.0, -0.14, -0.6, 0.0, -0.34],
    #     [-0.68, 0.0, -0.37, -0.19, 0.0, -0.11, -0.75, 0.0, -0.42],
    #     [-0.81, 0.0, -0.45, -0.1, 0.0, -0.06, -0.83, 0.0, -0.46],
    #     [-0.82, 0.0, -0.45, 0.0, 0.0, 0.0, -0.82, 0.0, -0.45],
    #     [-0.71, 0.0, -0.39, 0.1, 0.0, 0.06, -0.73, 0.0, -0.41],
    #     [-0.5, 0.0, -0.27, 0.19, 0.0, 0.11, -0.57, 0.0, -0.32],
    #     [-0.22, 0.0, -0.12, 0.23, 0.0, 0.14, -0.37, 0.0, -0.2],
    #     [0.08, 0.0, 0.05, 0.24, 0.0, 0.14, -0.13, 0.0, -0.07],
    #     [0.36, 0.0, 0.2, 0.2, 0.0, 0.12, 0.13, 0.0, 0.07],
    #     [0.6, 0.0, 0.34, 0.14, 0.0, 0.08, 0.37, 0.0, 0.2],
    #     [0.75, 0.0, 0.42, 0.07, 0.0, 0.04, 0.57, 0.0, 0.32],
    #     [0.83, 0.0, 0.46, 0.02, 0.0, 0.02, 0.73, 0.0, 0.41],
    #     [0.82, 0.0, 0.45, 0.0, 0.0, 0.0, 0.82, 0.0, 0.45],
    # ]
    lines = file.readlines()
    data_diffs = []
    data_diffs_dis = []
    data_diffs_angle = []
    for tmp in lines:
        tmp = str(tmp).strip()
        tmp = tmp.replace('[', '')
        tmp = tmp.replace(']', '')
        tmp = tmp.replace('"', '')
        tmp_new = tmp.split(", ")
        data_diff = [0 for i in range(9)]
        data = []
        for tmp_n in tmp_new:
            data.append(float(tmp_n))

        for i in range(3):
            for j in range(1,4):
                data_diff[i * 3 + j - 1] = round(data[i * 4 + j] - data[i * 4], 2)
        file_diff.write(str(data_diff))
        file_diff.write("\n")
        data_diffs.append(data_diff)
        '''
        diff distance
        '''
        corrcoeff_arrays = []
        for array in arrays:
            corrcoeff_arrays.append(round(np.corrcoef(data_diff, array)[0][1], 2))
        data_diffs_dis.append(corrcoeff_arrays)
        print "corrcoeff:", corrcoeff_arrays
        file_corr_diff.write(str(round(np.average(corrcoeff_arrays), 2)))
        file_corr_diff.write("\n")

        '''
        diff angle
        '''
        corrcoeff_arrays = []
        for array in arrays:
            corrcoeff_arrays.append(round(np.corrcoef(data_diff, array)[0][1], 2))
        data_diffs_angle.append(corrcoeff_arrays)


    '''
    distances write:
    '''
    len1 = len(data_diffs_dis)
    for j in range(9):
        for i in range(len1):
            file_diff_dis_corrcoeff.write(str(data_diffs_dis[i][j]) + " ")
        file_diff_dis_corrcoeff.write("\n")

    '''
    angle write:
    '''
    # len2 = len(data_diffs_angle)
    # len3 = len(data_diffs_angle[0])
    # for j in range(len3):
    #     for i in range(len2):
    #         file_diff_angle_corrcoeff.write(str(data_diffs_angle[i][j]) + " ")
    #     file_diff_angle_corrcoeff.write("\n")



    file.close()
    file_diff.close()
    file_corr.close()
    file_corr_diff.close()
    file_diff_dis_corrcoeff.close()
    file_diff_angle_corrcoeff.close()
    return data_diffs

def get_theory_value(angle, dis):
    '''
    get tdoa diff theory
    :param angle:
    :param dis:
    :return:
    '''
    dis_phoneme = [0, 50, 0, 25]
    res_values = []
    for dis_p in dis_phoneme:
        res_value = cav.cal_values(dis + dis_p, angle)
        res_values.append(res_value)
    res_values_diff = [0 for i in range(9)]
    for i in range(3):
        for j in range(3):
            #print res_values[i + 1][j], res_values[0][j]
            res_values_diff[i + j * 3] = round(res_values[i + 1][j] - res_values[0][j], 2)
    return res_values_diff

def corrcoeff_theory_actual(angle, dis):
    dis_phoneme = [0, 50, 0, 25]
    res_values = []
    for dis_p in dis_phoneme:
        res_value = cav.cal_values(dis * 10 + dis_p, angle)
        for res_v in res_value:
            res_values.append(res_v)

    test_file_name = "all_angle_" + str(dis) + "/log_1_" + str(dis) + "_" + str(angle) + "_merge"

    file = open(test_file_name)
    lines = file.readlines()

    datas = []
    for tmp in lines:
        tmp = str(tmp).strip()
        tmp = tmp.replace('[', '')
        tmp = tmp.replace(']', '')
        tmp = tmp.replace('"', '')
        tmp_new = tmp.split(", ")
        data = []
        for tmp_n in tmp_new:
            data.append(float(tmp_n))
        data_changed = change_format(data)
        datas.append(data_changed)
    corrcoeffs = []
    for data in datas:
        corrcoeffs.append(np.corrcoef(data, res_values)[0][1])
        print data
        print res_values
    for corrcoeff in corrcoeffs:
        print corrcoeff

def change_format(datas):
    res = [0 for i in range(12)]
    count = 0
    for i in range(3):
        for j in range(4):
            res[count] = datas[j * 3 + i]
            count += 1
    return res

def main():

    #file_list = [0, 15, 30, 45, 60] # 10
    file_list = [0, 15, 30, 45, 60, 75, 90] # 20
    dis = 20

    for file in file_list:
        file_name = "corrcoef/corrcoef_file_" + str(dis) + "_" + str(file)
        file_name_formated = file_name + "_formated"
        f = open(file_name, "w")
        f_f = open(file_name_formated, "w")
        values = read_and_cal_avg(file, dis)
        theory_value = get_theory_value(file, dis * 10)
        correct_num = 0
        wrong_num = 0
        for value in values:
            #print "theory:", theory_value
            #print "value:", value
            f.write(str(round(np.corrcoef(theory_value, value)[0][1], 2)))
            f.write("\n")
            f_theory, f_value = formated(theory_value, value)

            for i in range(9):
                if f_theory[i] * f_value[i] <= 0:
                    wrong_num += 1
                else:
                    correct_num += 1

            f_f.write(str(round(np.corrcoef(f_theory, f_value)[0][1], 2)))
            f_f.write("\n")

            #print "theory values:", theory_value
        f_f.write("correct num:" + str(correct_num) + "\n")
        f_f.write("wrong num:" + str(wrong_num) + "\n")
        f_f.write("rate:" + str((float(correct_num) / (correct_num + wrong_num))))

        f.close()

def formated(theory_value, value):
    value_formated = []
    theory_value_formated = []
    for v in value:
        if v > 0:
            value_formated.append(1)
        elif v == 0:
            value_formated.append(0)
        else:
            value_formated.append(-1)
    for t_v in theory_value:
        if t_v > 0:
            theory_value_formated.append(1)
        elif t_v == 0:
            theory_value_formated.append(0)
        else:
            theory_value_formated.append(-1)
    return value_formated, theory_value_formated
    # corrcoeff = np.corrcoef(value_formated, theory_value_formated)
    # print "vf:", value_formated
    # print "tvf:", theory_value_formated
    # return round(corrcoeff[0][1], 2)

def main1():
    corrcoeff_theory_actual(45, 20)

if __name__ == "__main__":
    # main()
    # main1()
    read_and_cal_avg()
