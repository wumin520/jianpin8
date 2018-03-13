---
title: 列表页面
---

## 列表接口

#### URL

**`/api/job.list`**

#### Method

GET

#### Parameters

| 字段名 | 类型 | 描述 | 必填 |
| ----- | ----- | ----- | ----- |
| city_id | Integer | 城市id（0全国） | 否 |
| offset | Integer | 偏移量(default=0) | 否 |
| pagesize | Integer | 每页条数(default=50) | 否 |


#### Response

##### 字段说明

* payload

| 字段名 | 类型 | 描述 |
| ----- | ----- | ----- |
| id | Integer | id |
| title | String | 标题 |
| city_name | String | 城市名 |
| new_tag | String | 标签 |
| recruit_starttime | String | 招聘开始时间 |
| recruit_endtime | String | 招聘结束时间 |
| currency | String | 薪资 |
| currency_unit | String | 薪资结算的单位 |
| jiexi_type | String | 结息方式 |

```json
{
  "err_code": 0,
  "err_msg": "",
  "payload": [
    {
      "id": 1,
      "title": "标题",
      "city_name": "城市名",
      "tag": "标签",
      "recruit_starttime": "招聘开始时间",
      "recruit_endtime": "招聘结束时间",
      "currency": "薪资",
      "currency_unit": "薪资结算的单位",
      "jiexi_type": "结息方式",
    }
  ]
}
```
