import tkinter as tk
from tkinter import ttk
import threading  # 用于在后台运行爬虫

from scrape import scrape
from save import save


# 定义主要的爬虫函数
def main():
    # 在这里编写爬取操作的代码
    status_label.config(text="正在爬取")
    sets = scrape()
    save(sets)
    status_label.config(text="爬取成功")


# 创建一个tkinter窗口
root = tk.Tk()
root.title("爬虫工具")

# 设置窗口宽度和高度（以像素为单位）
window_width = 300
window_height = 200

# 使用geometry方法设置窗口大小
root.geometry(f"{window_width}x{window_height}")

# 创建一个下拉选单
label = ttk.Label(root, text="选择难度:")
label.pack(pady=10)

difficulty_var = tk.StringVar()
difficulty_dropdown = ttk.Combobox(root, textvariable=difficulty_var, values=[
    "暂无评定", "入门", "普及-", "普及/提高-", "普及+/提高", "提高+/省选-", "省选/NOI-", "NOI/NOI+/CTSC"])
difficulty_dropdown.pack()


# 创建一个按钮，并将其与main函数关联
def start_crawling():
    selected_difficulty = difficulty_var.get()
    print(f"选择的难度: {selected_difficulty}")

    # 在单独的线程中运行爬虫以避免界面冻结
    crawler_thread = threading.Thread(target=main)
    crawler_thread.start()


# 创建一个标签用于显示爬取状态
status_label = tk.Label(root, text="等待开始爬取", padx=10, pady=10)
status_label.pack()

start_button = ttk.Button(root, text="开始爬取", command=start_crawling)
start_button.pack(pady=20)

root.mainloop()
