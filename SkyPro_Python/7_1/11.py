order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []
temp_dict = {}
# Не удаляйте текст ниже, он нужен для проверки
for item in order:
    temp_dict["count"] = int(item["skolko"])
    temp_dict["specie"] = item["poroda"].capitalize()
    temp_dict["avg_size"] = int(item["sred_razmer"]/10)
    order_converted.append(temp_dict.copy())

for item in order_converted:
    for key, value in item.items():
        print(key, value)
