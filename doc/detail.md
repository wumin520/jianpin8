---
title: 详情页面
---

## 详情接口

#### URL

**`/api/job.detail`**

#### Method

GET

#### Parameters

| 字段名 | 类型 | 描述 | 必填 |
| ----- | ----- | ----- | ----- |
| id | Integer | id |  是 |


#### Response

##### 字段说明

* payload

| 字段名 | 类型 | 描述 |
| ----- | ----- | ----- |
| id | Integer | id |
| title | String | 标题 |
| city_name | String | 城市名 |
| hot_tag | Integer | 是否启用热门标签：1：启用，2：不启用 |
| currency | String | 薪资 |
| currency_unit | String | 薪资结算的单位 |
| jiexi_type | String | 结息方式 |
| jianpin_person | Integer | 招聘人数 |
| jianpin_detail | String | 职位描述 |
| work_time | String | 工作时间 |
| work_adress | String | 工作地点 |
| company | String | 公司名称 |
| jump_url | String | 跳转的url |
| jump_type | Integer | 跳转方式：1：URL，2：wechat |


```json
{
  "err_code": 0,
  "err_msg": "",
  "payload": {
      "id": 1,
      "title": "标题",
      "city_name": "城市名",
      "hot_tag": 1,
      "currency": "2000",
      "currency_unit": "日",
      "jiexi_type": "月结",
      "jianpin_person": "1000",
      "jianpin_detail": "这里展示职位描述",
      "welfare": "这里显示待遇福利",
      "work_time": "每天工作8小时",
      "work_adress": "上海",
      "company": "公司名称",
      "jump_url": "跳转的url",
      "jump_type": 1,
  }
}
```