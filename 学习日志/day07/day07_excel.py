from pathlib import Path
import pandas as pd
output_dir=Path('输出结果')
output_dir.mkdir(exist_ok=True)

customer_data=pd.read_excel("学习数据/training_data.xlsx",sheet_name="客户用量",)
monthly_data=pd.read_excel("学习数据/training_data.xlsx",sheet_name="月度趋势",)
character_data=pd.read_excel("学习数据/training_data.xlsx",sheet_name='字段说明')
print("客户用量表：", customer_data.shape)
print(customer_data.head(3))
print("月度趋势表：", monthly_data.shape)
print(monthly_data)

output_file=output_dir/"day07_excel_result.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    customer_data.to_excel(writer, sheet_name="客户用量副本",index=False,)
    monthly_data.to_excel(writer,sheet_name="月度用量趋势",index=False,)
    character_data.to_excel(writer,sheet_name='字段说明',index=False,)
print("已生成：", output_file)
