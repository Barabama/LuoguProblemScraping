import requests
import kuser_agent
from bs4 import BeautifulSoup
from html2text import HTML2Text


def _get_url(url: str):
    """发送GET请求获取网页内容"""
    headers = {"User-Agent": kuser_agent.get()}  # 设置请求头信息
    response = requests.get(url, headers=headers)
    html_content = response.text
    return html_content


def _scrape(url: str, element="", All=True):
    """获取网页元素"""
    soup = BeautifulSoup(_get_url(url), "html.parser")
    if element == "":
        return soup
    else:
        return soup.find_all(element) if All else soup.find(element)


def scrape():
    main_url = "https://www.luogu.com.cn/problem/"
    list_url = main_url + "list"

    problems = _scrape(list_url, "li")  # 获取所有题库列表
    sets = []
    for problem in problems:
        # 题目的编号、标题
        Id, title, = problem.get_text().split(maxsplit=1)

        # 题目内容并转为字符串
        article = _scrape(main_url + Id, "article", False)
        converter = HTML2Text()
        text = converter.handle(article.prettify())

        sets.append({
            "Id": Id,
            "title": title,
            "difficulty": "",
            "content": text,
            "solution": "",
        })
    return sets


if __name__ == "__main__":
    scrape()
