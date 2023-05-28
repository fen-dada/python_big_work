#import requests
import csv
import numpy as np
import matplotlib.pyplot as plt
import re
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

x=[]
js=open("军事.csv","r")
#jj=open("经济.csv","r")


def printEco():
    for line in jj:
        print(line[5:line.find("亿")])
        line=line.replace("\n","")
        ls=line.split(",")
        lns=""
        for s in ls:
            lns += "{}\t".format(s)
        #print(lns)
        
def test():
    for line in jj:
        list=line[5:line.find("亿")]
        if list.__contains__("万") and list.__contains__("."):
            list=list.replace(".","")
        list=list.replace("万","0000")
        print(list)
    

def printMili():
    for line in js:
        line=line.replace("\n","")
        ls=line.split(",")
        lns=""
        for s in ls:
            lns += "{}\t".format(s)
        print(lns)
    

        

        
def printBar(x,y):
    plt.bar(x, y)
    plt.show()

def printPlot():
    str=jj.read()
    plt.figure(num = 3, figsize = (12,9))
    #x=np.linspace(-1,1,50)
    plt.xlim(2000,2022)
    year=np.linspace(2000,2022,23)
    plt.xticks(year)
    eco=re.findall(r"\d+.?\d*+亿",str)
    y=[]
    for i in eco:
        i=i.replace("万","0000")
        i=i.replace("亿","")
        y.append(i)
    print(y)
    np.ndarray(y)
    plt.yticks(y)
    
    plt.plot()
    plt.show()



x = [2018,2019]
y = [60, 45, 49, 36, 42, 67, 40, 50]
printBar(x,y)




with open("经济.csv") as f:
    reader=csv.reader(f)
    header_row=next(reader)
    years_china=[]
    gdps_china=[]
    years_usa=[]
    years=[]
    gdps_usa=[]
    for row in reader:
        if row[0]=="1987":
            break
        year=int(row[0])
        for i in range(1,3):
            row[i]=row[i].replace("亿","")
            if row[i].__contains__("万") and row[i].__contains__("."):
                #row[i]=row[i].replace(".","")
                t=row[i].replace("万","")
                ans=float(t)*10000
                row[i]=str(ans)
            #row[i]=row[i].replace("万","0000")
        gdp_china=float(row[1])
        gdp_usa=float(row[2])
        years.append(year)
        gdps_china.append(gdp_china)
        gdps_usa.append(gdp_usa)



print(gdps_china)
plt.figure(num = 1, figsize = (14,8))
plt.plot(years,gdps_china,'ro-',alpha=0.8,c="red",label="China")
plt.plot(years,gdps_usa,'ro-',c="blue",label="USA")

plt.title("GDP of China and USA",fontsize="18")
plt.xlabel("Years",fontsize=14)
plt.ylabel("GDP(hundred million)",fontsize=14)
plt.tick_params(axis="both",labelsize=12)

plt.legend()
plt.show()

js.close()
#jj.close()
