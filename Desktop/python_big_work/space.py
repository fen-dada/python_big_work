import matplotlib.pyplot as plt
import csv

import matplotlib as mpl
font_name = "Songti SC"
mpl.rcParams['font.family']=font_name
mpl.rcParams['axes.unicode_minus']=False # in case minus sign is shown as box


with open("航天.csv") as f:
    countries=[]
    nums=[]
    reader=csv.reader(f)
    for row in reader:
        countries.append(row[0]) 
        nums.append(row[1])
countries.remove("世界卫星排名")
nums.remove("数量")
amounts=[]
for i in nums:
    amounts.append(int(i))

plt.figure(figsize=(12,8))
plt.bar(countries,amounts)
for a,b in zip(countries,amounts):
    plt.text(a,b+2,b,ha='center',va="bottom")
plt.title("卫星数量")
plt.xlabel("国家")
plt.ylabel("数量")
plt.show()