---
title: 城市列表页面
---

## 城市列表接口

#### URL

**`/api/city.list`**

#### Method

GET

#### Parameters

| 字段名 | 类型 | 描述 | 必填 |
| ----- | ----- | ----- | ----- |



#### Response

##### 字段说明

* payload

| 字段名 | 类型 | 描述 |
| ----- | ----- | ----- |
| id | Integer | id |
| city_name | String | 城市名 |

```json
{
  "err_code": 0,
  "err_msg": "",
  "payload": [
    {
      "id": 1,
      "city_name": "城市名",
    }
  ]
}
```
