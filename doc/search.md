---
title: 搜索页面
---

## 搜索接口

#### URL

**`/api/job.search`**

#### Method

GET

#### Parameters

| 字段名 | 类型 | 描述 | 必填 |
| ----- | ----- | ----- | ----- |
| keywords | String | 搜索词 | 是 |
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
| hot_tag | Integer | 是否启用热门标签：1：启用，2：不启用 |
| jianpin_startdate | String | 招聘开始日期 |
| jianpin_enddate | String | 招聘结束日期 |
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
      "hot_tag": 1,
      "jianpin_startdate": "03.15",
      "jianpin_enddate": "08.15",
      "currency": "2000",
      "currency_unit": "日",
      "jiexi_type": "月结",
    }
  ]
}
```