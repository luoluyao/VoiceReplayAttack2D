# VoiceReplayAttack2D

## 文件说明

### readwav.py

 * 输入：两个音频文件(.wav)和对应的TextGrid文件
 * 输出：三个麦克风与某一个麦克风各个音素的tdoa
 
 
### generateResult_script.py

* 功能：多线程批量执行**readwav.py**脚本。
* 输入：path（给的是一个目录，会将该目录下的所有文件都进行分析）
* 输出：到**path+“_log”** 文件下
* 路径用的是**硬编码**，直接在文件的path改即可。
* 输出日志示例部分如下：
```
['different_samplerate/sample16khz/log_19/test0.wav', 'different_samplerate/sample16khz/log_19/test2.wav', -79.69, -75.7, -78.36, -78.36]
['different_samplerate/sample16khz/log_19/test0.wav', 'different_samplerate/sample16khz/log_19/test3.wav', -42.5, -42.5, -43.83, -42.5]
['different_samplerate/sample16khz/log_19/test0.wav', 'different_samplerate/sample16khz/log_19/test1.wav', -43.83, -42.5, -42.5, -43.83]
```
* 注意：由于未做多线程安全处理，所以输出到文件时，存在两条日志杂在一起的情况，需要手动规范了。但是只是"["，"]"符号出乱，可以不管。

### formated_multithread.py

* 功能：将**generateResult_script.py**生成的日志，格式化输出。
* 输入：前者的日志
* 输出：到**日志名+“_merge”**中
* 输出的一条日志示例如下：
```
[-43.83, -42.5, -42.5, -43.83, -79.69, -75.7, -78.36, -78.36, -42.5, -42.5, -43.83, -42.5]
```


### cal_actual_vals.py
 
 * 功能：2D中，理论值的计算；
 * def cal_values(D, angle):
 
    **输入**：2D模型中距离（D）和角度（angle）
    
    **输出**：三对麦克风tdoa的差值。
  
  * def theory_value_distance(dis):
  
     **输入**：距离
     
     **输出**：三对麦克风，4个音素间的差值。
     
     **示例**输出9个值。
     
     第1个值表示：第一对麦克风第二个音素tdoa-第一个音素tdoa
     
     第2个值表示：第一对麦克风第三个音素tdoa-第一个音素tdoa
     
     第3个值表示：第一对麦克风第四个音素tdoa-第一个音素tdoa
     
     第4个值表示：第二对麦克风第二个音素tdoa-第一个音素tdoa
     
### theory_value_angle(angle):

 * 同上，但输入的是**角度**
 
 
### mathanalysis_multithread_diff.py
* 归一化方法获得相关系数

### mathanalysis_multithread_diff_3.py

* 不同角度，不同距离获得相关系数
  
 
    
 
