
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



| 字段名 |  说明 |  数值的计算 |
|---|---|---|
|  Index | 当前阶段计算对应的序号 ||
|  Region | 地区 ||
|  Subregion | 子地区 ||
|  Stage | 当前阶段结算的日期 ||
|  Confirmed | 当前阶段结算的确诊数 ||
|  Deaths | 当前阶段结算的死亡数 ||
|  Recovered | 当前阶段结算的康复数 ||
|  Stage_Confirmed | 当前阶段计算的确诊数 | Current#Confiremed - Last#Recovered - Last#Deaths  |
|  Stage_Deaths | 当前阶段计算的死亡数 | Current#Deaths - Last#Deaths |
|  Stage_Recovered | 当前阶段计算的康复数 | Current#Confirmed - Last#Confirmed  |
|  Stage_Treated% | 当前阶段计算的病例已经获得处理率 | Stage_Treated / Stage_Confirmed |
|  Stage_Deaths% | 当前阶段计算的死亡率 | Stage_Deaths / Stage_Treated |
|  Stage_Recovered% | 当前阶段计算的康复率 | Stage_Recovered / Stage_Treated |
|  Stage_Treated | 当前阶段计算的病例已经获得处理数量 | (Current#Recovered + Current#Deaths) - (Last#Recovered + Last#Deaths) |
|  Recovered_Change | 当前阶段计算的康复率变化情况 | Current#Stage_Recovered% - Last#Stage_Recovered%  |



* Current#XXX：表示的是当前阶段的XXX数值

* Last#XXX：表示的是相对于当前阶段的上阶段的XXX数值



## 5.数据分析的一些心得体会

在阶段病例已经获得处理数量（即Stage_Treated）较大，且认为其数据是有效的情况下：

* 阶段的康复率变化波动大的地区与环境温度相关性越能对应上

* 康复情况越差的地区越可能是处于寒冷的地区，反之则不一定成立

* 康复情况好的地区很多都是处于环境温度较高地区

* 当以间隔天数较小进行阶段划分时，同一地区出现较多较大的阶段的康复率的概率是在天气温度较好的时间（在Excel中可过滤可能是异常数值的数据，如阶段康复率是在0.5到1的区间，阶段康复数大于或等于10和阶段死亡数大于或等于0，将过滤后的数据拷贝到新的工作表中，针对该新建工作表数据创建一个以地区和子地区为行，阶段日期组合成月为列，阶段康复率平均值为值的数据透视表）

* 环境温度对阶段康复率的影响有滞后性，根据供冷供暖情况不同，天气温度会对环境温度有不同的影响，所以不太会出现极端天气温度造成极端差的康复情况，有些地区会出现在寒冷的天气温度下供暖后的康复情况比不供暖时的要好，但大多都会比不过天气温度较高时的状况

* 印度的疫情大数据告诉我们，并不是温度越高越好，在2021年2月温度较适宜，2021年1月和2021年3月稍差，到了现在2021年5月更差了，预测印度接下来的更炎热的夏天会疫情康复情况数据会更差

* 处于北半球中高纬度的国家，如意大利，美国，德国，加拿大，丹麦等大多都是2020年10月左右进入疫情恶化的情况（还包括确诊数激增，重症患者占比增大等）。在排除掉初始阶段不稳定数据情况下，这些国家2020年11月和12月，2021年1月和2月的阶段计算的康复率求平均值，比自己刚刚过去的2021年6月的数据要差（美国2021年6月的数据缺失，无法做数据对比），康复情况较好的冰岛自己最差数据也是在2020年11月

* 2021年5月和6月疫情急剧进入恶化状况的都是处于南半球的高纬度国家，如智利，乌拉圭，阿根廷和澳大利亚等（新西兰数据量较少看不出来变化，但也有较好康复情况，南非数据变化有些奇怪，原因暂时未知），这些国家现在重现了北半球那些2020年10月左右疫情急剧恶化的状况。在排除掉初始阶段不稳定数据情况下，他们自己最差的阶段计算的康复率容易出现在是在2020年6月左右，刚刚过去的2021年6月有些国家已经重现了自己较差的康复情况数据（澳大利亚整体数据和新南威尔士州的数据有误，分析时请注意）

* 南北半球的冬天和夏天时间是颠倒过来的，颠倒的环境温度也造成了在各个半球很多中高纬度地区的康复情况好坏的数据是颠倒过来的。若是数据不符合该该规律，可查询该地区的历史天气温度情况（2021年天气异常情况很大），结合当地的实际供冷供暖情况，粗略地推算出其环境温度，再以最佳人体舒适温度做为基准，就可能得出该基准，环境温度与该地区的康复情况之间的关联关系了（因不同地区的受温度影响程度还不一样，或许其他因素影响覆盖掉了温度的影响，但个人认为数值波动大的地区是受温度影响较大的地区，也是人均寿命不高的地区，康复情况的好坏也在某种程度上反应出了地区的人均寿命）

  
## 6.License
* This data set is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) by zyq5945 
* This code set is  licensed under MIT by zyq5945
