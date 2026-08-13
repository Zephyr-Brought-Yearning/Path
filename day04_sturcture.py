def calculate_usage(previous_reading,current_reading):
    return current_reading - previous_reading

def calculate_amount(usage,unit_price):
    return round(usage*unit_price,2)

def get_level(usage):
    if usage<100:
        return "用量等级：较低"
    elif usage<500:
        return "用量等级：一般"
    else:
        return "用量等级：较高"
customers=[
    {'customer_id':'C001',
     'customer_name':'模拟客户一',
     'previous_reading':1000,
     'current_reading':1128.5,
     'unit_price':0.62
     },
    {'customer_id':'C002',
     'customer_name':'模拟客户二',
     'previous_reading':800,
     'current_reading':975,
     'unit_price':0.61
     },
    {'customer_id':'C003',
     'customer_name':'模拟客户三',
     'previous_reading':1352.8,
     'current_reading':1888.6,
     'unit_price':0.60
     }
]

for customer in customers:
    usage = calculate_usage(customer['previous_reading'],customer['current_reading'])
    amount = calculate_amount(usage,customer['unit_price'])
    print(
        customer["customer_id"],
        customer["customer_name"],
        f"用量 {usage:.2f}",
        get_level(usage),
        f"金额 {amount:.2f}",
    )
