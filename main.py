# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import bs4
import json
import pinyin


# 请求政府网，获得数据结构
def getText():
    res = requests.get("http://www.gov.cn/test/2011-08/22/content_1930111.htm")
    if res.status_code != 200:
        raise Exception("网页请求失败!")

    # 网页源码
    data = str(res.content, 'utf-8')

    # 解析节点，获得文本形式的数据
    soup = bs4.BeautifulSoup(data)
    return soup.span.text


if __name__ == '__main__':
    text = getText()
    result = []
    for item in text.split("\n"):
        if item == '':
            continue

        # 分隔字符串行政区划代码和区县
        its = item.split("  ")

        # 层级、代码、名称
        level = item.count("\xa0\xa0")
        code = its[0].strip()
        name = its[1]
        py = ""

        for key in list(name):
            py += pinyin.get(key)[0]

        result.append({
            "level": level,
            "code": code,
            "name": name,
            "initials": py,
            "pinyin": pinyin.get(name)
        })

    print(json.dumps(result, ensure_ascii=False))
