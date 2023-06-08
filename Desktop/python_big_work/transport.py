import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'

modify_road={}
modify_rail={}
del_road=[]
del_rail=[]
def TransPlot():
    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\交通.csv",encoding='utf-8') as f:
        years=[] 
        nums=[]
        reader=csv.reader(f)
        for row in reader:
            if row[0] in del_road:
                continue
            years.append(row[0]) 
            
            if row[0] in modify_road:
                nums.append(modify_road[row[0]])
                continue
            #years.append(row[0]) 
            nums.append(row[1])
            if(row[0]=='1980'):
                break
        years.remove("\ufeff时间")
        nums.remove("万公里")
        amounts=[]
        years.reverse()
        for i in nums:
            amounts.append(float(i))
        amounts.reverse()
        plt.figure(figsize=(20,12))
        plt.bar(years,amounts)
        for a,b in zip(years,amounts):
            plt.text(a,b+2,b,ha='center',va="bottom")
        plt.title("公路交通里程数")
        plt.xlabel("年份")
        plt.ylabel("万公里")
        plt.show()


def TransPlot_rail():
    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\交通.csv",encoding='utf-8') as f:
        years=[] 
        nums=[]
        reader=csv.reader(f)
        for row in reader:
            if row[2].replace('年','') in del_rail:
                continue
            years.append(row[2].replace('年','')) 
            if row[2].replace('年','') in modify_rail:
                nums.append(modify_rail[row[2].replace('年','')])
                continue

            #years.append(row[2].replace('年','')) 
            nums.append(row[3])
            if(row[0]=='1980'):
                break
        #print(years)
        years.remove("时间")
        nums.remove("万公里")
        amounts=[]
        
        years.reverse()
        for i in nums:
            amounts.append(float(i))
        amounts.reverse()
        plt.figure(figsize=(20,12))
        plt.bar(years,amounts)
        for a,b in zip(years,amounts):
            plt.text(a,b,b,ha='center',va="bottom")
        plt.title("铁路交通里程数")
        plt.xlabel("年份")
        plt.ylabel("万公里")
        plt.show()

def search_road(year):
    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\交通.csv",encoding='utf-8') as f:
        years=[] 
        nums=[]
        reader=csv.reader(f)
        for row in reader:
            if(year==row[0]):
                data=float(row[1])
        return data
    
def search_rail(year):
    with open("C:\\Users\\admin\\Desktop\\python_big_work\\Desktop\\python_big_work\\交通.csv",encoding='utf-8') as f:
        years=[] 
        nums=[]
        reader=csv.reader(f)
        for row in reader:
            if(year==row[2]):
                data=float(row[3])
        return data