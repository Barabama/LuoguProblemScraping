import os


def save(sets: [dict]):
    for s in sets:
        Id = s["Id"]
        title = s["title"]
        difficulty = s["difficulty"]
        content = s["content"]
        solution = s["solution"]

        # 创建题目文件夹
        folder_path = os.path.join("Problems", f"{Id}-{title}")
        file_name = f"{Id}-{title}.md"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 保存md文件
        with open(os.path.join(folder_path, file_name), "w", encoding="utf-8") as f:
            f.write(content)
