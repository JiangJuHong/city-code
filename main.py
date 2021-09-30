# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import bs4
import json
import pinyin


# 请求政府网，获得数据结构，返回行政区划代码、名称、级别
# 统一规范，仅返回 code、name、level数据。直辖市需要在 level 0 和 level 1 中均出现
def parse():
    # 读取网页
    res = requests.get("http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html")
    if res.status_code != 200:
        raise Exception("网页请求失败!")

    # 解析数据
    return _parse_20201201(bs4.BeautifulSoup(str(res.content, 'utf-8')))


# 解析 民政部 20201201 数据
# 统一规范，仅返回 code、name、level数据。直辖市需要在 level 0 和 level 1 中均出现
def _parse_20201201(soup):
    valid_data = []
    # 获得表格，并过滤前三行的标题行以及后面的港澳台信息
    trs = soup.table.findAll('tr')[3:-12]
    for tr in trs:
        tds = tr.findAll('td')
        tds = list(filter(lambda item: item.text != '', tds))
        if len(tds) < 2:
            continue

        # 获得城市编码，名称，级别
        code = tds[0].text
        name = tds[1].text
        level = name.count(' ')
        if level > 2:
            level = 2

        # 追加数据
        valid_data.append({
            "code": code,
            "name": name.strip(),
            "level": level,
        })

        # 如果是直辖市，则添加市数据
        if ["110000", "120000", "310000", "500000"].count(code):
            valid_data.append({
                "code": code,
                "name": name.strip(),
                "level": 1,
            })

    return valid_data


if __name__ == '__main__':
    result = []
    data = parse()

    parentCode = {}
    lastLevel = None
    lastCode = None
    for item in data:
        # 层级、代码、名称
        level = item["level"]
        code = item["code"]
        name = item["name"]
        py = ""

        # 层级发生改变时更新层级关系
        if lastLevel != level:
            lastLevel = level
            lastCode = code
            parentCode[level] = code

        # 赋值拼音
        for key in list(name):
            py += pinyin.get(key)[0]

        parent = None
        if level != 0:
            parent = parentCode[level - 1]

        result.append({
            "level": level,
            "code": code,
            "name": name,
            "initials": py,
            "pinyin": pinyin.get(name),
            "parent": parent,
        })

    print(json.dumps(result, ensure_ascii=False))
