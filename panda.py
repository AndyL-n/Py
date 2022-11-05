import pandas as pd

"""
data = pd.read_csv('titanic.csv')

# print(data)

# print(data.head(10))

# print(data.columns)

# print(data)
# mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。
avg = data['Fare'].mean()
print(avg)
data['Fare'].fillna(avg, inplace = True)

mode = data['Embarked'].mode()
# print(type(mode))
mode = mode[0]
# print(type(mode))
data['Embarked'].fillna(mode[0], inplace=True)

data.loc[data['Fare'] > 10,'Fare'] /= 10

data.dropna(axis=0, how='any', subset=['Embarked'], inplace=True)
# data.dropna(axis=0, how='any', inplace=True)

data.drop_duplicates(inplace=True)

print(data.head(10))
"""


user = pd.read_csv("ml-100k/user", header=None, sep="|" )
user.columns = ["id","age","sex","occupation","ip"]
# print(user.keys())

occupation = pd.read_csv("ml-100k/occupation_map", header=None)
occupation.columns = ["occupation"]
occupation["index"] = occupation.index
# print(occupation)

#
user = pd.merge(left=user, right=occupation, left_on='occupation',right_on='occupation', how="left")

# data = [
#     ['河北', 630],
#     ['河南', 120],
# ]
counts = user["index"].value_counts()
print(type(counts))
data = []
for key,val in counts.items():
    # print(key ,val)
    data.append([key, val])
print(data)


