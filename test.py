import tkinter as tk

def show_transport_ui():
    # 创建主窗口
    root = tk.Tk()
    root.title("交通")

    # 创建交通按钮
    traffic_button = tk.Button(root, text="交通", command=lambda: show_transport_buttons(root, traffic_button))
    traffic_button.pack(pady=20)

    root.mainloop()

def show_transport_buttons(root, traffic_button):
    # 隐藏交通按钮
    traffic_button.pack_forget()

    # 创建交通方式按钮
    transport_frame = tk.Frame(root)

    road_button = tk.Button(transport_frame, text="公路", command=lambda: show_transport_options(root, transport_frame))
    road_button.pack(pady=10)

    railway_button = tk.Button(transport_frame, text="铁路", command=lambda: show_transport_options(root, transport_frame))
    railway_button.pack(pady=10)

    transport_frame.pack(fill=tk.BOTH, expand=True)

def show_transport_options(root, transport_frame):
    # 隐藏交通方式按钮
    transport_frame.pack_forget()

    # 创建交通方式选项按钮和返回按钮
    options_frame = tk.Frame(root)

    return_button = tk.Button(options_frame, text="返回", command=lambda: show_transport_buttons(root, return_button))
    return_button.pack(pady=20)

    options_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    show_transport_ui()