import sys
import numpy

# data number for one set
one_set_sample = 12

# data number for phoneme
phoneme_num = 4

# calcAvg, return 12 avg
def calc_avg(datas):
    avgs = [0 for i in range(one_set_sample)]
    for i in range(one_set_sample):
        one_sum = 0
        valid_count = 0
        for j in range(len(datas)):
            if datas[j][i] < 5: # valid data
                continue
            one_sum += datas[j][i]
            valid_count += 1
        if valid_count == 0:
            continue
        avgs[i] = round(one_sum / valid_count, 2)
    return avgs

#calc every set variance, return 60
def every_set_variance(datas, avgs):
    variances = []
    for data in datas:
        one_set_sum = 0
        for i in range(one_set_sample):
            if data[i] < 5: # valid data
                continue
            one_set_sum += pow(data[i] - avgs[i], 2)
        variances.append(round(pow(one_set_sum, 0.5), 2))
    return variances

# calc trainData
def train_data(datas, avgs):
    train_data_values = []
    for data in datas:
        train_data_values.append([ round(data[i] - avgs[i], 2) for i in range(len(avgs))])
    return train_data_values

# compare .wav name
def cmd_func(a, b):
    return cmp(a, b)

# read file datas
def read_file(file_name):
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
                # print "tmp_new", tmp_new[i]
                merge_tmp.append(float(tmp_new[i]))
            tmp = []
            datas.append(merge_tmp)
            merge_tmp = []
        line_count += 1
    file.close()
    return datas




def get_right_data():
    test_file_name = "different_samplerate/log_sample48k"
    datas = read_file(test_file_name)
    test_file_name_write = test_file_name + "_merge"
    f_wite = open(test_file_name_write, "w")
    for data in datas:
        f_wite.write(str(data))
        f_wite.write("\n")
    f_wite.close()


def read_and_cal_avg(count):
    test_file_name = "log2/log_machine_" + str(count) + "_merge"
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
        datas.append(data)
    avg_datas = []
    for i in range(12):
        sum_value = 0
        count = 0
        for data in datas:
            sum_value += data[i]
            count += 1
        avg_datas.append(round(sum_value / count, 2))
    print "count", avg_datas


# def write(count):
#     test_file_name = "log2/log_human_" + str(count)
#     test_file_name_write = test_file_name + "_write"
#     f_wite = open(test_file_name_write, "w")
#     distance = count * 10
#     datas = read_file(test_file_name)
#
#     results = []
#     for data in datas:
#         print_result = calc_actual(data, distance)
#         f_wite.write(str(print_result))
#         f_wite.write("\n")
#         results.append(print_result)
#     f_wite.write("max:" + str(numpy.max(results)))
#     f_wite.write("\n")
#     f_wite.write("min:" + str(numpy.min(results)))
#     f_wite.write("\n")
#     f_wite.write("median:" + str(numpy.median(results)))
#     f_wite.write("\n")
#     f_wite.write("mean:" + str(numpy.mean(results)))
#     f_wite.write("\n")

def origin_data():
    test_file_name = "log2/log_human_10"
    datas = read_file(test_file_name)
    new_data = []
    for i in range(12):
        sum_value = 0
        count = 0
        for data in datas:
            sum_value += data[i]
            count += 1
        new_data.append(round(sum_value / count, 2))
    print new_data

def main():
    get_right_data()
    # distances = [10,20,30,35,40,45,50,60,80]
    # origin_data()
    # for distance in distances:
    #     read_and_cal_avg(distance)
        #get_right_data(distance)

    #     write(distance)
    # for i in range(1,6):
    #     if i == 4:
    #         continue
    #     get_right_data(i*10)
    #     #read_and_cal_avg(i * 10)
    # origin_data()
    # test data file
    # for i in range(1,6):
    #     if i == 4:
    #         continue
    #     write(i * 10)
    # write(39)


if __name__ == '__main__':
    main()