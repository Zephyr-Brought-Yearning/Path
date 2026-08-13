print("=== 虚构用量计算练习 ===")
previous_reading=float(input("请输入上期读数："))
current_reading=float(input("请输入当前读数："))
unit_price=float(input("请输入练习单价："))

usage=current_reading-previous_reading
amount=round(usage*unit_price,2)
department="数智科创部"

print(f"部门：{department}")
print(f"本期用量：{usage:.2f}")
print(f"练习金额：{amount:.2f}")