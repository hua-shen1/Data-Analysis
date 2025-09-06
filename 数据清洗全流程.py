#导入pandas库，解析csv。
import pandas as pd
from pathlib import Path

#设置pandas库显示dataframe
pd.set_option('display.max_columns', None) #显示最大列数
pd.set_option('display.max_rows', None) #显示最大行数
pd.set_option('display.float_format','{:.0f}'.format) #关闭科学计数法
data_path = Path(__file__).with_name("ds_salaries.csv")
original_data = pd.read_csv(data_path)
original_data.head()

#评估数据
original_data.sample(10) #从抽样的数据来看，符合每列代表一个变量，每行代表一个观察值，每个单元格是一个值
original_data.info() #评估数据干净度 #从输出结果看，一共有3755条数据，没有缺失值
original_data["work_year"].isnull() #work_year列是否有缺失值
original_data[original_data["work_year"].isnull()] #找出original_data为缺失值的观察值
original_data["employee_residence"].value_counts() #评估某一列数据出现次数
original_data.describe() #求某一列的计算

#清洗数据
cleaned_data = original_data.copy() #创建一个与原始dataframe相同的dataframe
cleaned_data["work_year"] = pd.to_datetime(
    cleaned_data["work_year"].astype(str), format="%Y", errors="coerce"
) #将入职年份改为正确的年份日期类型（按年解析）
cleaned_data["salary_in_usd"] = cleaned_data["salary_in_usd"].astype(str) #将数据类型改为字符串
cleaned_data.info()
cleaned_data = cleaned_data.dropna(subset = ["salary"]) #删除salary列的缺失值
cleaned_data["salary"].isnull().sum() #求空值的个数
cleaned_data["employee_residence"] = cleaned_data["employee_residence"].replace({"US":"USA"}) #将employee_residence列中的US改为USA

#保存清洗后数据
cleaned_data.to_csv("ds_salaries_cleaned.csv",index = False)
