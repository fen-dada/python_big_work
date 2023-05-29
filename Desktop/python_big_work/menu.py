#导入tkinter库
import tkinter as tk

import space

def showMenu():
    #创建主窗口
    root = tk.Tk()
    #设置窗口标题
    root.title("分析祖国发展成就")
    #设置窗口大小和位置
    root.geometry("800x600+100+100")

    #创建菜单栏
    menubar = tk.Menu(root)
    #创建文件菜单
    filemenu = tk.Menu(menubar, tearoff=0)
    #添加文件菜单项
    filemenu.add_command(label="打开", command=lambda: print("打开文件"))
    filemenu.add_command(label="保存", command=lambda: print("保存文件"))
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=root.quit)
    #将文件菜单添加到菜单栏
    menubar.add_cascade(label="文件", menu=filemenu)

    #创建帮助菜单
    helpmenu = tk.Menu(menubar, tearoff=0)
    #添加帮助菜单项
    helpmenu.add_command(label="关于", command=lambda: print("关于本程序"))
    helpmenu.add_command(label="使用说明", command=lambda: print("使用说明"))
    #将帮助菜单添加到菜单栏
    menubar.add_cascade(label="帮助", menu=helpmenu)

    #将菜单栏添加到主窗口
    root.config(menu=menubar)

    #创建标签，显示欢迎信息
    label = tk.Label(root, text="欢迎使用本程序，分析祖国发展成就！", font=("宋体", 20))
    #将标签放置在主窗口中央
    label.pack()

    #创建一个框架，用于放置分析按钮
    frame = tk.Frame(root)
    #将框架放置在主窗口下方
    frame.pack()

    #创建经济分析按钮，并设置按钮大小为20x10
    economy_button = tk.Button(frame, text="经济", command=lambda: print("分析经济"), width=20, height=1)
    #将按钮放置在框架中，并设置边距为20像素
    economy_button.pack(side=tk.TOP, pady=20)

    #创建科技分析按钮，并设置按钮大小为20x10
    technology_button = tk.Button(frame, text="科技", command=lambda: print("分析科技"), width=20, height=1)
    #将按钮放置在框架中，并设置边距为20像素
    technology_button.pack(side=tk.TOP, pady=20)

    #创建文化分析按钮，并设置按钮大小为20x10
    culture_button = tk.Button(frame, text="文化", command=lambda: print("分析文化"), width=20, height=1)
    #将按钮放置在框架中，并设置边距为20像素
    culture_button.pack(side=tk.TOP, pady=20)

    #创建社会分析按钮，并设置按钮大小为20x10
    society_button = tk.Button(frame, text="社会", command=lambda: print("分析社会"), width=20, height=1)
    #将按钮放置在框架中，并设置边距为20像素
    society_button.pack(side=tk.TOP, pady=20)

    #创建环境分析按钮，并设置按钮大小为20x10
    environment_button = tk.Button(frame, text="航天", command=space.SpacePlot, width=20, height=1)
    #将按钮放置在框架中，并设置边距为20像素
    environment_button.pack(side=tk.TOP, pady=20)

    #启动主循环
    root.mainloop()

