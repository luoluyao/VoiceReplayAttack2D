import sys
import numpy

# data number for one set
one_set_sample = 12

# data number for phoneme
phoneme_num = 4

test_file_name = "different_samplerate/sample16khz_log"

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
    datas = read_file(test_file_name)
    test_file_name_write = test_file_name + "_merge"
    f_wite = open(test_file_name_write, "w")
    for data in datas:
        f_wite.write(str(data))
        f_wite.write("\n")
    f_wite.close()

def main():
    get_right_data()

if __name__ == '__main__':
    main()