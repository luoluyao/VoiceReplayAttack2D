import cal_actual_vals as cav
import numpy as np

def read_and_cal_avg(count, dis):
    test_file_name = "all_angle_" + str(dis) + "/log_1_" + str(dis) + "_" + str(count) + "_merge"
    test_file_name_diff = test_file_name + "_diff"
    file = open(test_file_name)
    file_diff = open(test_file_name_diff, "w")
    lines = file.readlines()
    data_diffs = []
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

    file.close()
    file_diff.close()
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
    main()
    # main1()
