previous_reading=float(input(("请输入上期读数：")))
current_reading=float(input("请输入本期读数："))
usage=current_reading-previous_reading

if usage<0:
    print("数据异常：本期读数小于上期读数")
elif usage==0:
    print("本期用量为0")
else:
    print(f"本期用量：{usage:.2f}")
    if usage<100:
        print("用量等级：较低")
    elif usage<500:
        print("用量等级：一般")
    else:
        print("用量等级：较高")

monthly_usage=[120.5,98.0,135.2,160.0,110.3,200.0]
total_usage=0
high_count=0
for item in monthly_usage:
    total_usage+=item
    print("月用量：",item)
    if item>130:
        high_count+=1

print(f"合计：{total_usage:.2f}")
print(f"高用量月份数：{high_count}")