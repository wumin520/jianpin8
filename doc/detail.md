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
| tag | String | 标签 |
| jianpin_type | Integer | 招聘方式：1：长期招聘，2：指定时间 |
| jianpin_starttime | String | 招聘开始时间 |
| jianpin_endtime | String | 招聘结束时间 |
| currency | String | 薪资 |
| currency_unit | String | 薪资结算的单位 |
| jiexi_type | Integer | 结息方式 |
| jianpin_person | String | 招聘人数 |
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
      "tag": "标签",
      "jianpin_type": "招聘方式：1：长期招聘，2：指定时间",
      "jianpin_starttime": "招聘开始时间",
      "jianpin_endtime": "招聘结束时间",
      "currency": "薪资",
      "currency_unit": "薪资结算的单位",
      "jiexi_type": "结息方式",
      "jianpin_person": "招聘人数",
      "jianpin_detail": "职位描述",
      "welfare": "待遇福利",
      "work_time": "工作时间",
      "work_adress": "工作地点",
      "company": "公司名称",
      "jump_url": "跳转的url",
      "jump_type": "跳转方式：1：URL，2：wechat",
      ""
  }
}
```