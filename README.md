
## 1.介绍说明

首先声明下，重新整理分析的是[CSSEGISandData](https://github.com/CSSEGISandData)的[COVID-19](https://github.com/CSSEGISandData/COVID-19)数据，针对的是该数据各地区各月份的康复情况的好坏,。若是你认为数据有误，请向CSSEGISandData联系反馈修改。


## 2.运行脚本Python


### 2.1 安装Python3.8和依赖库

```
pip install pandas 
```


### 2.2 运行命令

```
python covid19.py /xxx/xxx/COVID-19 /yyy/yyy/COVID-19-Month-Recovery
```
/xxx/xxx/COVID-19是下载的[COVID-19](https://github.com/CSSEGISandData/COVID-19)仓库数据根目录，默认是当前目录

/yyy/yyy/COVID-19-Month-Recovery是输出数据目录，默认是当前目录

## 3.字段说明



| 字段名 |  说明 |  数值的计算 |
|---|---|---|
|  Index | 月份对应的序号 ||
|  Region | 地区 ||
|  Subregion | 子地区 ||
|  Month | 月份 ||
|  Confirmed | 当月最后一天的确诊数 ||
|  Deaths | 当月最后一天的死亡数 ||
|  Recovered | 当月最后一天的康复数 ||
|  Month_Confirmed | 当月的确诊数 | 当月最后一天的确诊数减去上月最后一天的康复数与死亡数之和 |
|  Month_Deaths | 当月的死亡数 | 当月最后一天的死亡数减去上月最后一天的死亡数 |
|  Month_Recovered | 当月的康复数 | 当月最后一天的康复数减去上月最后一天的康复数 |
|  Month_Treated% | 当月的病例已经获得处理率 | 当月病例已经获得处理数量除以当月的确诊数 |
|  Month_Deaths% | 当月的死亡率 | 当月的死亡数除以当月病例已经获得处理数量 |
|  Month_Recovered% | 当月的康复率 | 当月的康复数除以当月病例已经获得处理数量 |
|  Month_Treated | 当月病例已经获得处理数量 | 当月最后一天的确诊数与死亡数之和减去上月最后一天的确诊数与死亡数之和 |
|  Recovered_Change | 当月康复率变换情况 |当月的康复率减去上月的康复率|



