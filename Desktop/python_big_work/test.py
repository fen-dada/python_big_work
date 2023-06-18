import tkinter as tk
from tkinter import ttk
import space 
import mili2
import transport
import src
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
matplotlib.rcParams['font.family'] = 'SimHei'
import matplotlib.pyplot as plt
#hehe

# 新增数据
def add_data():
    add_window = tk.Toplevel(root)
    add_window.title('新增数据')
    add_window.geometry('300x300')
    add_window.configure(bg='#f0f0f0')
    tk.Label(add_window, text='请输入数据类别：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    category_entry = tk.Entry(add_window, font=('Arial', 12))
    category_entry.pack(pady=10)
    tk.Label(add_window, text='请输入数据年份：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    year_entry = tk.Entry(add_window, font=('Arial', 12))
    year_entry.pack(pady=10)
    tk.Label(add_window, text='请输入数据数值：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    value_entry = tk.Entry(add_window, font=('Arial', 12))
    value_entry.pack(pady=10)
    tk.Button(add_window, text='确定', bg='#4caf50', fg='white', font=('Arial', 12), command=lambda: save_data(category_entry.get(), year_entry.get(), value_entry.get())).pack(pady=10)

# 保存数据
def save_data(category, year, value):
    global df
    new_data = {'类别': category, '年份': year, '数值': value}
    df = df.append(new_data, ignore_index=True)
    tk.messagebox.showinfo('提示', '数据已保存')
    root.update()

# 删除数据
def delete_data():
    delete_window = tk.Toplevel(root)
    delete_window.title('删除数据')
    delete_window.geometry('300x300')
    delete_window.configure(bg='#f0f0f0')
    tk.Label(delete_window, text='请输入要删除的数据类别：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    category_entry = tk.Entry(delete_window, font=('Arial', 12))
    category_entry.pack(pady=10)
    tk.Label(delete_window, text='请输入要删除的数据年份：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    year_entry = tk.Entry(delete_window, font=('Arial', 12))
    year_entry.pack(pady=10)
    tk.Button(delete_window, text='确定', bg='#f44336', fg='white', font=('Arial', 12), command=lambda: remove_data(category_entry.get(), year_entry.get())).pack(pady=10)

# 删除数据
def remove_data(category, year):
    #global df
    # df = df.drop(df[(df['类别'] == category) & (df['年份'] == year)].index)
    if(category=="经济"):
        src.del_year.append(year)
    elif(category=="铁路"):
        transport.del_rail.append(year)
    elif(category=="公路"):
        transport.del_road.append(year)
    else:
        tk.messagebox.showinfo('提示', '输入有误！')
        return
    tk.messagebox.showinfo('提示', '数据已删除')
    root.update()

# 修改数据
def update_data():
    update_window = tk.Toplevel(root)
    update_window.title('修改数据')
    update_window.geometry('300x300')
    update_window.configure(bg='#f0f0f0')
    tk.Label(update_window, text='请输入要修改的数据类别：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    category_entry = tk.Entry(update_window, font=('Arial', 12))
    category_entry.pack(pady=10)
    tk.Label(update_window, text='请输入要修改的数据年份：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    year_entry = tk.Entry(update_window, font=('Arial', 12))
    year_entry.pack(pady=10)
    tk.Label(update_window, text='请输入新的数据数值：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    value_entry = tk.Entry(update_window, font=('Arial', 12))
    value_entry.pack(pady=10)
    tk.Button(update_window, text='确定', bg='#2196f3', fg='white', font=('Arial', 12), command=lambda: change_data(category_entry.get(), year_entry.get(), value_entry.get())).pack(pady=10)

# 修改数据
def change_data(category, year, value):
    # global df
    # df.loc[(df['类别'] == category) & (df['年份'] == year), '数值'] = value
    if(category=="中国经济"):
        src.modify_china[year]=value
    elif(category=="美国经济"):
        src.modify_usa[year]=value
    elif(category=="英国经济"):
        src.modify_uk[year]=value
    elif(category=="俄罗斯经济"):
        src.modify_russia[year]=value
    elif(category=="铁路"):
        transport.modify_rail[year]=value
    elif(category=="公路"):
        transport.modify_road[year]=value
    else:
        tk.messagebox.showinfo('提示', '输入有误！')
        return
    tk.messagebox.showinfo('提示', '数据已修改')
    root.update()

# 查询数据
def search_data():
    search_window = tk.Toplevel(root)
    search_window.title('查询数据')
    search_window.geometry('300x300')
    search_window.configure(bg='#f0f0f0')
    tk.Label(search_window, text='请输入要查询的数据类别：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    category_entry = tk.Entry(search_window, font=('Arial', 12))
    category_entry.pack(pady=10)
    tk.Label(search_window, text='请输入要查询的数据年份：', bg='#f0f0f0', font=('Arial', 12)).pack(pady=10)
    year_entry = tk.Entry(search_window, font=('Arial', 12))
    year_entry.pack(pady=10)
    tk.Button(search_window, text='确定', bg='#9c27b0', fg='white', font=('Arial', 12), command=lambda: find_data(category_entry.get(), year_entry.get())).pack(pady=10)

# 查询数据
def find_data(category, year):
    # global df
    # data = df[(df['类别'] == category) & (df['年份'] == year)]
    # if len(data) > 0:
    #     tk.messagebox.showinfo('查询结果', f'类别：{data.iloc[0]["类别"]}，年份：{data.iloc[0]["年份"]}，数值：{data.iloc[0]["数值"]}')
    # else:
    #     tk.messagebox.showerror('查询结果', '未找到符合条件的数据')
    if(category=="经济"):
        data=src.search_eco(year)
    elif(category=="公路"):
        data=transport.search_road(year)
    elif(category=="铁路"):
        data=transport.search_rail(year)
    elif(category=="卫星"):
        data=space.search(year)
    else:
        tk.messagebox.showinfo('提示', '输入有误！')
        return
    tk.messagebox.showinfo('查询结果', f'类别：{category}，年份：{year}，数值：{data}')
    root.update()



# 创建主窗口
root = tk.Tk()
root.title('祖国发展成就数据系统')
root.geometry('800x600')
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

def show_main_menu():
    road_button.pack_forget()
    railway_button.pack_forget()
    return_button.pack_forget()

    btn_economy.pack(side=tk.TOP, pady=20)
    btn_military.pack(side=tk.TOP, pady=20)
    btn_space.pack(side=tk.TOP, pady=20)
    btn_transport.pack(side=tk.TOP, pady=20)
    
    btn_add.place(relx=0.15, rely=0.8, anchor='w')
    btn_delete.place(relx=0.35, rely=0.8, anchor='w')
    btn_update.place(relx=0.55, rely=0.8, anchor='w')
    btn_search.place(relx=0.75, rely=0.8, anchor='w')


def show_transport_buttons(root):
    # 隐藏交通按钮
    btn_transport.pack_forget()
    btn_space.pack_forget()
    btn_economy.pack_forget()
    btn_military.pack_forget()
    btn_add.pack_forget()
    btn_delete.pack_forget()
    btn_update.pack_forget()
    btn_search.pack_forget()

    # 创建交通方式按钮
    road_button.pack(side=tk.TOP, pady=20)
    railway_button.pack(side=tk.TOP, pady=20)
    return_button.pack(side=tk.TOP, pady=20)

# 创建圆角窗口
frame = ttk.Frame(root, style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor='center')
#frame.tk.call('wm', 'overrideredirect', True)  # 去掉标题栏
frame.tk.call('tk::PlaceWindow', '.', 'center')  # 窗口居中
frame.configure(width=600, height=400)

# 创建按钮
btn_economy = ttk.Button(root, text='经济', command=src.EcoPlot)
btn_military = ttk.Button(root, text='军事', command=mili2.MiliPlot)
btn_space = ttk.Button(root, text='航天', command=space.SpacePlot)
btn_transport = ttk.Button(root, text='交通', command=lambda: show_transport_buttons(root))

road_button = ttk.Button(root, text="公路",command=transport.TransPlot)
road_button.pack(pady=20)

railway_button = ttk.Button(root, text="铁路",command=transport.TransPlot_rail)
railway_button.pack(pady=20)

return_button = ttk.Button(root, text="返回", command=show_main_menu)
return_button.pack(pady=20)


# 显示按钮
btn_economy.pack(side=tk.TOP, pady=20)
btn_military.pack(side=tk.TOP, pady=20)
btn_space.pack(side=tk.TOP, pady=20)
btn_transport.pack(side=tk.TOP, pady=20)

# 创建增删改查按钮
btn_add = tk.Button(text='新增', bg='#4caf50', fg='white', font=('Arial', 14), bd=0, width=6, height=2, command=add_data)
btn_delete = tk.Button(text='删除', bg='#f44336', fg='white', font=('Arial', 14), bd=0, width=6, height=2, command=delete_data)
btn_update = tk.Button(text='修改', bg='#2196f3', fg='white', font=('Arial', 14), bd=0, width=6, height=2, command=update_data)
btn_search = tk.Button(text='查询', bg='#9c27b0', fg='white', font=('Arial', 14), bd=0, width=6, height=2, command=search_data)



# 绘制数据
def plot_data(category):
    data = df[df['类别'] == category]
    plt.bar(data['年份'], data['数值'])
    plt.title(category)
    plt.xlabel('年份')
    plt.ylabel('数值')
    plt.show()

show_main_menu()

# 运行主循环
root.mainloop()

