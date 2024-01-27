# 使用dict
dic = dict()
# 获取元素
dic.get("dic")
# 元素累加
# 如果存在
if dic.get("dic") > 1:
    dic["dic"] += 1
# 不存在
else:
    dic["dic"] = 1
# 遍历 key, value
for key, value in dic.items():
    print(key, value)
