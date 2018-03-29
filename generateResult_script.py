import os
import threading

path = "different_samplerate/sample16khz"

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()


def os_cmd(filename):
    cmds = []
    for i in range(0,4,):
        if i == 0 :
            continue
        cmd = "python readwav.py " + filename + "0.wav " + filename + str(i) + ".wav " + filename + "0.TextGrid " +  filename + str( i) + ".TextGrid >> " + path + "_log"
        cmds.append(cmd)
        print cmd
    # threads pool
    threads = []

    # create four threads
    try:
        for cmd in cmds:
            th = threading.Thread(target=exec_cmd, args=(cmd,))
            th.start()
            threads.append(th)
    except:
       print "Error: unable to start thread"

    for th in threads:
        th.join()

def dirlist(path, allfile):
    '''
    get all files under path
    :param path:
    :param allfile:
    :return:
    '''
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile

def get_same_file_name(allfiles):
    '''
    remove same files
    :param allfiles:
    :return:
    '''
    for filename in allfiles:
        print filename
        if filename.endswith('test.wav'):
            os_cmd(filename[:-4])

def main():
    allfile = []
    dirlist(path, allfile)
    get_same_file_name(allfile)

if __name__ == "__main__":
    main()



