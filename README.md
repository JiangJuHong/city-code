# city-code

中国大陆城市行政区划数据，包含**城市名称**、**行政区划代码**、**层级数据**、**拼音排序**、**父代码**等字段，数据来源: [中华人民共和国民政部](http://www.mca.gov.cn/article/sj/xzqh/1980/) .  
最新数据为 ``2020年12月01日 数据``

> 不包含港澳台数据

## 数据示例


| 名称  | 描述         | 示例          |
| ----- | ------------ | ------------- |
| level | 等级         | 省0市1区2.... |
| name  | 名称         | 北京市        |
| code  | 行政区划代码 | 110000        |
| initials  | 拼音首字母缩写 | bjs       |
| pinyin  | 完整拼音 | beijingshi       |
| parent  | 父级代码 | 110000       |

````json
[
	{
        "level":0,
        "code":"110000",
        "name":"北京市",
        "initials": "bjs",
        "pinyin": "beijingshi",
        "parent": null
  },
  {
        "level":1,
        "code":"110000",
        "name":"北京市",
        "initials": "bjs",
        "pinyin": "beijingshi",
        "parent": "110000"
    }
]
````

更多数据请查看:[city-code-20201231.json](./city-code-20201201.json)

## 采集工具

数据使用: [./main.py ](./main.py)进行采集



## 注意事项

* 禁止将此数据或 [数据采集工具](#采集工具) 用作任何违法犯罪活动
* 本数据与 [中华人民共和国民政部](http://www.mca.gov.cn/article/sj/xzqh/1980/) 网保持同步，所有内容均为``公开、合法``内容，禁止将 [数据采集工具](#采集工具) 用在非法场景