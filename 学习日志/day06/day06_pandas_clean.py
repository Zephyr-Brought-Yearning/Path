from pathlib import Path
import pandas as pd
output_dir=Path('输出结果')
output_dir.mkdir(exist_ok=True)
data=pd.read_csv('学习数据/customer_usage.csv',encoding='utf-8-sig')
#去除首尾空格
data['customer_name']=data['customer_name'].str.strip()
data['region']=data['region'].str.strip()

data['previous_reading']=pd.to_numeric(data['previous_reading'],errors='coerce')
data['current_reading']=pd.to_numeric(data['current_reading'],errors='coerce')
data['unit_price']=pd.to_numeric(data['unit_price'],errors='coerce').fillna(0.62)
#清洗数据
data['usage']=data['current_reading']-data['previous_reading']
valid_mask=(data['previous_reading'].notna()&data['current_reading'].notna()&(data['usage']>=0))
clean_data=data.loc[valid_mask].copy()
error_data=data.loc[~valid_mask].copy()

clean_data['amount']=(clean_data['usage']*clean_data['unit_price']).round(2)
clean_file=output_dir/'clean_customer_usage.csv'
error_file=output_dir/'error_customer_usage.csv'
clean_data.to_csv(clean_file,index=False,encoding='utf-8-sig')
error_data.to_csv(error_file,index=False,encoding='utf-8-sig')
print("有效记录数：", len(clean_data))
print("异常记录数：", len(error_data))
print(clean_data[["customer_id", "customer_name", "region", "usage", "amount"]])
