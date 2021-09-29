# city-code

中国大陆城市行政区划数据，包含**城市名称**、**行政区划代码**、**层级数据**，数据来源: [中华人民共和国中央人民政府《县及县以上行政区划代码（截止2010年12月31日）》](http://www.gov.cn/test/2011-08/22/content_1930111.htm)

> 不包含港澳台数据

## 数据示例

````json
[
	{
        "level":0,
        "code":"110000",
        "name":"北京市"
  },
  {
        "level":1,
        "code":"110100",
        "name":"市辖区"
    }
]
````

更多数据请查看:[city-code-20101231.json](./city-code-20101231.json)



## 数据结构

| 名称  | 描述         | 示例          |
| ----- | ------------ | ------------- |
| level | 等级         | 省0市1区2.... |
| name  | 名称         | 北京市        |
| code  | 行政区划代码 | 110000        |



## 采集工具

数据使用: [./main.py ](./main.py)进行采集



## 注意事项

* 禁止将此数据或[数据采集工具](#采集工具)用作任何违法犯罪活动
* 本数据与[中华人民共和国中央人民政府](http://www.gov.cn/)网保持同步，所有内容均为``公开、合法``内容，禁止将[数据采集工具](#采集工具)用在非法场景