from pathlib import Path
import pandas as pd


file_path=Path('学习数据/customer_usage.csv')
data=pd.read_csv(file_path,encoding='utf-8-sig')

print("前三行：")
print(data.head(3))
print("后两行：")
print(data.tail(2))
print("行数和列数：",data.shape)
print("字段名：",data.columns.tolist())

print("各字段缺失数量：")
print(data.isna().sum())
print("区域记录数：")
print(data['region'].value_counts())