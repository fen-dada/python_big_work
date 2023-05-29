import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib
import space
import mili2
matplotlib.use('TkAgg')
matplotlib.rcParams['font.family'] = 'SimHei'
import matplotlib.pyplot as plt

# 加载数据
#df = pd.read_csv('data.csv')

# 创建主窗口
root = tk.Tk()
root.title('数据可视化')
root.geometry('600x400')
root.configure(bg='#f0f0f0')

# 创建按钮样式
style = ttk.Style()
style.configure('TFrame', 
                background='#f0f0f0', 
                borderwidth=0)

style.configure('TLabel', 
                background='#f0f0f0', 
                foreground='#333333', 
                font=('Arial', 12))

style.configure('TButton', 
                background='#4caf50', 
                foreground='white', 
                font=('Arial', 12), 
                borderwidth=0, 
                relief='flat', 
                padding=10, 
                width=10, 
                height=2, 
                bordercolor='#dcdcdc', 
                focusthickness=0, 
                focuscolor='#dcdcdc', 
                anchor='center', 
                borderradius=20, 
                lightcolor='#f0f0f0', 
                darkcolor='#a0a0a0')

# 创建圆角窗口
frame = ttk.Frame(root, style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor='center')
#frame.tk.call('wm', 'overrideredirect', True)  # 去掉标题栏
frame.tk.call('tk::PlaceWindow', '.', 'center')  # 窗口居中
frame.configure(width=600, height=400)

# 创建标签
label = ttk.Label(frame, text='请选择数据类别', style='TLabel')
label.pack(side=tk.TOP, pady=20)

# 创建按钮
btn_economy = ttk.Button(root, text='经济', command=lambda: plot_data('经济'))
btn_military = ttk.Button(root, text='军事', command=mili2.MiliPlot)
btn_space = ttk.Button(root, text='航天', command=space.SpacePlot)


# 显示按钮
btn_economy.pack(side=tk.TOP, pady=20)
btn_military.pack(side=tk.TOP, pady=20)
btn_space.pack(side=tk.TOP, pady=20)

# # 绘制数据
# def plot_data(category):
#     data = df[df['类别'] == category]
#     plt.bar(data['年份'], data['数值'])
#     plt.title(category)
#     plt.xlabel('年份')
#     plt.ylabel('数值')
#     plt.show()

# 运行主循环
root.mainloop()