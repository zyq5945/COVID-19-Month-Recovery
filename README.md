
## 1.介绍说明

首先声明下，重新整理分析的是[CSSEGISandData](https://github.com/CSSEGISandData)的[COVID-19](https://github.com/CSSEGISandData/COVID-19)数据，针对的是该数据各地区不同阶段的康复情况的好坏,。若是你认为数据有误，请向CSSEGISandData联系反馈修改。


## 2.文件目录
* Stage-0：以月份为阶段进行划分的COVID-19的康复情况
* Stage-N：以N天间隔为阶段进行划分的COVID-19的康复情况


注：本仓库的数据不定期更新，需要最新数据或者其他阶段划分的请自行运行脚本

## 3.运行脚本Python


### 3.1 安装Python3.8和依赖库

```
pip install pandas 
```


### 3.2 运行命令

```
python COVID-19.py /xxx/xxx/COVID-19 /yyy/yyy/COVID-19-Stage-Recovery Step
```
*  /xxx/xxx/COVID-19: 下载的[COVID-19](https://github.com/CSSEGISandData/COVID-19)仓库数据根目录，默认是当前目录
* /yyy/yyy/COVID-19-Stage-Recovery: 输出数据目录，默认是当前目录
* Step：当前阶段的间隔天数，当等于0时按月份来进行分阶段，默认是按月份



## 4.字段说明



| 字段名 |  说明 |  数值的计算 | 计算的说明 |
|---|---|---|---|
|  Index | 当前阶段计算对应的序号 |||
|  Region | 地区 |||
|  Subregion | 子地区 |||
|  Stage | 当前阶段结算的日期 |||
|  Confirmed | 当前阶段结算的确诊数 |||
|  Deaths | 当前阶段结算的死亡数 |||
|  Recovered | 当前阶段结算的康复数 |||
|  Stage_Confirmed | 当前阶段计算的确诊数 | Current#Confiremed - Last#Recovered - Last#Deaths  | 当前阶段结算的确诊数减去上阶段结算的康复数与死亡数之和|
|  Stage_Deaths | 当前阶段计算的死亡数 | Current#Deaths - Last#Deaths | 当前阶段结算的死亡数减去上阶段结算的死亡数  |
|  Stage_Recovered | 当前阶段计算的康复数 | Current#Confirmed - Last#Confirmed  | 当前阶段结算的康复数减去上阶段结算的康复数|
|  Stage_Treated% | 当前阶段计算的病例已经获得处理率 | Stage_Treated/Stage_Confirmed  | 当前阶段计算的病例已经获得处理数量除以当前阶段计算的确诊数|
|  Stage_Deaths% | 当前阶段计算的死亡率 | Stage_Deaths/Stage_Treated  | 当前阶段计算的死亡数除以当前阶段计算的病例已经获得处理数量|
|  Stage_Recovered% | 当前阶段计算的康复率 | Stage_Recovered/Stage_Treated  | 当前阶段计算的康复数除以当前阶段计算的病例已经获得处理数量|
|  Stage_Treated | 当前阶段计算的病例已经获得处理数量 | (Current#Recovered + Current#Deaths) - (Last#Recovered + Last#Deaths) | 当前阶段计算的康复数与死亡数之和减去上阶段计算的康复数与死亡数之和 |
|  Recovered_Change | 当前阶段计算的康复率变化情况 | Current#Stage_Recovered% - Last#Stage_Recovered%  | 当前阶段计算的康复率减去上阶段计算的康复率|



* Current#XXX：表示的是当前阶段的XXX数值

* Last#XXX：表示的是相对于当前阶段的上阶段的XXX数值



## 5.数据分析的一些心得体会

在阶段病例已经获得处理数量（即Stage_Treated）较大，且认为其数据是有效的情况下：

* 阶段的康复率变化波动大的地区与环境温度相关性越能对应上

* 康复情况越差的地区越可能是处于寒冷的地区，反之则不一定成立

* 康复情况好的地区很多都是处于环境温度较高地区

* 当以间隔天数较小进行阶段划分时，同一地区出现较多较大的阶段的康复率的概率是在天气温度较好的时间（在Excel中可过滤可能是异常数值的数据，如阶段康复率是在0.5到1的区间，阶段康复数大于或等于10和阶段死亡数大于或等于0，将过滤后的数据拷贝到新的工作表中，针对该新建工作表数据创建一个以地区和子地区为行，阶段日期组合成月为列，阶段康复率平均值为值的数据透视表）

* 环境温度对阶段康复率的影响有滞后性，根据供冷供暖情况不同，天气温度会对环境温度有不同的影响，所以不太会出现极端天气温度造成极端差的康复情况，有些地区会出现在寒冷的天气温度下供暖后的康复情况比不供暖时的要好，但大多都会比不过天气温度较高时的状况。

* 印度的疫情大数据告诉我们，并不是温度越高越好，在2021年2月温度较适宜，2021年1月和2021年3月稍差，到了现在2021年5月更差了，预测印度接下来的更炎热的夏天会疫情康复情况数据会更差。

  
## 6.License
* This data set is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) by zyq5945 
* This code set is  licensed under MIT by zyq5945
