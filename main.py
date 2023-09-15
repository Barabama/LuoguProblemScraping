import tkinter as tk

# 创建GUI窗口
window = tk.Tk()

# 添加输入框和按钮等控件
difficulty_label = tk.Label(window, text="题目难度：")
difficulty_label.pack()

difficulty_entry = tk.Entry(window)
difficulty_entry.pack()

search_button = tk.Button(window, text="搜索")
search_button.pack()

# 添加列表框，用于展示题目列表
problem_listbox = tk.Listbox(window)
problem_listbox.pack()

# 运行GUI窗口
window.mainloop()
