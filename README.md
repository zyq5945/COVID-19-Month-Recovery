
## 1.介绍说明

首先声明下，重新整理分析的是[CSSEGISandData](https://github.com/CSSEGISandData)的[COVID-19](https://github.com/CSSEGISandData/COVID-19)数据，针对的是该数据各地区不同阶段的康复情况的好坏,。若是你认为数据有误，请向CSSEGISandData联系反馈修改。


## 2.文件目录
* Stage-0：以月份为一阶段进行划分的COVID19的康复情况
* Stage-10：以10天间隔为一阶段进行划分的COVID19的康复情况
* Stage-15：以15天间隔为一阶段进行划分的COVID19的康复情况
* Stage-20：以20天间隔为一阶段进行划分的COVID19的康复情况

注：本仓库的数据不定期更新，需要最新数据或者其他阶段划分的请自行运行脚本

## 3.运行脚本Python


### 3.1 安装Python3.8和依赖库

```
pip install pandas 
```


### 3.2 运行命令

```
python covid19.py /xxx/xxx/COVID-19 /yyy/yyy/COVID-19-Stage-Recovery Step
```
*  /xxx/xxx/COVID-19: 下载的[COVID-19](https://github.com/CSSEGISandData/COVID-19)仓库数据根目录，默认是当前目录
* /yyy/yyy/COVID-19-Stage-Recovery: 输出数据目录，默认是当前目录
* Step：当前阶段的间隔天数，当等于0时按月份来进行分阶段，默认是按月份



## 4.字段说明



| 字段名 |  说明 |  数值的计算 |
|---|---|---|
|  Index | 当前阶段对应的序号 ||
|  Region | 地区 ||
|  Subregion | 子地区 ||
|  Stage | 当前阶段的日期 ||
|  Confirmed | 当前阶段的确诊数 ||
|  Deaths | 当前阶段的死亡数 ||
|  Recovered | 当前阶段的康复数 ||
|  Stage_Confirmed | 当前阶段的确诊数 | 当前阶段的确诊数减去上阶段的康复数与死亡数之和 |
|  Stage_Deaths | 当前阶段的死亡数 | 当前阶段的死亡数减去上阶段的死亡数 |
|  Stage_Recovered | 当前阶段的康复数 | 当前阶段的康复数减去上阶段的康复数 |
|  Stage_Treated% | 当前阶段的病例已经获得处理率 | 当前阶段的病例已经获得处理数量除以当前阶段的确诊数 |
|  Stage_Deaths% | 当前阶段的死亡率 | 当前阶段的死亡数除以当前阶段病例已经获得处理数量 |
|  Stage_Recovered% | 当前阶段的康复率 | 当前阶段的康复数除以当前阶段病例已经获得处理数量 |
|  Stage_Treated | 当前阶段病例已经获得处理数量 | 当前阶段的确诊数与死亡数之和减去上阶段的确诊数与死亡数之和 |
|  Recovered_Change | 当前阶段康复率变化情况 | 当前阶段的康复率减去上阶段的康复率|


## 5.数据分析的一些心得体会

在阶段病例已经获得处理数量（即Stage_Treated）较大，且认为其数据是有效的情况下：

* 阶段的康复率变化波动大的地区与天气温度相关性越能对应上
* 康复情况越差的地区越可能是处于寒冷的地区，反之则不一定成立
* 康复情况好的地区很多都是处于天气温度较高地区

