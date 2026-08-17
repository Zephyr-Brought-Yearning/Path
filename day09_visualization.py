from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=[
    'Microsoft YaHei',
    'SimHei',
    'Note Sans CJk SC',
]

plt.rcParams['axes.unicode_minus'] = False

output_dir=Path('输出结果')
output_dir.mkdir(exist_ok=True)


monthly_data=pd.read_excel(
    '学习数据/training_data.xlsx',
    sheet_name='月度趋势',
)
#折线图
plt.figure(figsize=(8, 5))
for region in ["南明区", "云岩区", "观山湖区"]:
    plt.plot(
        monthly_data["月份"],
        monthly_data[region],
        marker="o",
        label=region,
    )
plt.title("2026 年上半年虚拟区域用量趋势")
plt.xlabel("月份")
plt.ylabel("用量")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "monthly_trend.png", dpi=150)
plt.close()
#柱状图
summary=pd.read_excel(
    output_dir / 'day08_analysis.xlsx',
    sheet_name='区域汇总'
)
plt.figure(figsize=(7, 5))
plt.bar(summary['region'],summary['total_usage'])
plt.title("虚拟区域总用量对比")
plt.xlabel("区域")
plt.ylabel("总用量")
plt.tight_layout()
plt.savefig(output_dir / "monthly_usage.png", dpi=200)
plt.close()
print("已生成 monthly_trend.png 和 region_total_usage.png")