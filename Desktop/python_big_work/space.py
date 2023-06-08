import matplotlib.pyplot as plt
import csv

import matplotlib as mpl

def SpacePlot():
    # font_name = "Songti SC"
    # mpl.rcParams['font.family']=font_name
    # mpl.rcParams['axes.unicode_minus']=False # in case minus sign is shown as box
    plt.rcParams['font.sans-serif']='SimHei'


    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\航天.csv",encoding='utf-8') as f:
        countries=[] 
        nums=[]
        sate=[]
        years=[]
        reader=csv.reader(f)
        for row in reader:
            countries.append(row[0]) 
            nums.append(row[1])
            years.append(row[3])
            sate.append((row[4]))
    countries.remove("\ufeff世界卫星排名")
    nums.remove("数量")
    sate.remove("数量")
    years.remove("时间")
    sate_amount=[]
    amounts=[]
    for i in nums:
        amounts.append(int(i))
    for i in sate:
        sate_amount.append(int(i))

    plt.figure(figsize=(12,8))

    plt.subplot(2,1,1)
    plt.bar(countries,amounts)
    for a,b in zip(countries,amounts):
        plt.text(a,b+2,b,ha='center',va="bottom")
    plt.title("卫星数量")
    plt.xlabel("国家")
    plt.ylabel("数量")

    plt.subplot(2,1,2)
    
    plt.plot(years,sate_amount,'ro-',color="blue",label="Satellite")
    for a,b in zip(years,sate_amount):
        plt.text(a,b+3,b,ha='center',va="bottom")
    plt.legend()

    plt.tight_layout()
    plt.show()


def search(year):
    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\航天.csv",encoding='utf-8') as f:
        
        reader=csv.reader(f)
        for row in reader:
            if year==row[3]:
                data=int(row[4])
    return data