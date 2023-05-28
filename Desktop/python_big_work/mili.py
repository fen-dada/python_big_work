# 导入需要的库
import pandas as pd
import matplotlib.pyplot as plt

# 读取csv文件，假设文件名是data.csv，第一列是国家名，第二列是战斗机数量，第三列是坦克数量，第四列是导弹数量
df = pd.read_csv("data.csv")
print(df)

# 设置图形大小和子图间距
plt.figure(figsize=(10, 6))
plt.subplots_adjust(wspace=0.3)

# 画折线图，显示各国战斗机，坦克，导弹的数量随国家名的变化
plt.subplot(1, 2, 1)
plt.plot(df["国家名"], df["战斗机数量"], label="战斗机数量")
plt.plot(df["国家名"], df["坦克数量"], label="坦克数量")
plt.plot(df["国家名"], df["导弹数量"], label="导弹数量")
plt.xlabel("国家名")
plt.ylabel("数量")
plt.title("各国军事实力折线图")
plt.legend()

# 画柱状图，显示各国战斗机，坦克，导弹的数量
plt.subplot(1, 2, 2)
width = 0.25 # 设置柱子的宽度
x = df["国家名"] # 设置x轴的刻度
plt.bar(x - width, df["战斗机数量"], width=width, label="战斗机数量")
plt.bar(x, df["坦克数量"], width=width, label="坦克数量")
plt.bar(x + width, df["导弹数量"], width=width, label="导弹数量")
plt.xlabel("国家名")
plt.ylabel("数量")
plt.title("各国军事实力柱状图")
plt.legend()

# 显示图形
plt.show()