
# 导入csv模块
import csv


def MiliPlot():
    # 定义数据列表
    data = [
        ["国家", "坦克", "战斗机", "导弹"],
        ["中国", 3500, 3200, 2800],
        ["美国", 6000, 4500, 4000],
        ["俄罗斯", 13000, 4000, 6500],
        ["印度", 4500, 2700, 1500],
        ["法国", 400, 1200, 300]
    ]

    # 打开一个csv文件，写入模式
    with open("data2.csv", "w", newline="") as f:
        # 创建一个csv写入对象
        writer = csv.writer(f)
        # 循环写入每一行数据
        for row in data:
            writer.writerow(row)



    # 导入matplotlib模块
    import matplotlib.pyplot as plt

    # 定义国家列表和颜色列表
    countries = ["China", "USA", "Russia", "India", "France"]
    colors = ["red", "blue", "green", "orange", "purple"]

    # 定义坦克列表，战斗机列表和导弹列表
    tanks = [3500, 6000, 13000, 4500, 400]
    jets = [3200, 4500, 4000, 2700, 1200]
    missiles = [2800, 4000, 6500, 1500, 300]

    # 创建一个新的图形窗口
    plt.figure(figsize=(12,8))

    # 创建一个2x1的子图网格，激活第一个子图
    plt.subplot(2,1,1)

    # 绘制柱形图，设置标题和标签
    plt.bar(countries, tanks, color=colors)
    for a,b in zip(countries,tanks):
        plt.text(a,b+2,b,ha='center',va="bottom")
    plt.title("Tanks")
    plt.xlabel("Country")
    plt.ylabel("Amount")

    # 激活第二个子图
    plt.subplot(2,1,2)

    # 绘制折线图，设置标题和标签
    plt.plot(countries,jets,'ro-',color="red",label="Fighters")
    plt.plot(countries,missiles,'ro-',color="blue",label="Missiles")
    for a,b in zip(countries,jets):
        plt.text(a,b+3,b,ha='center',va="bottom")
    for a,b in zip(countries,missiles):
        plt.text(a,b+3,b,ha='center',va="bottom")
    plt.title("Fighters and Missiles")
    plt.xlabel("Country")
    plt.ylabel("Amount")
    plt.legend()


    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False

    # 调整子图间距
    plt.tight_layout()

    # 显示图形窗口
    plt.show()

