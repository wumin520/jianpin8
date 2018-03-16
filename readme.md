
## 兼聘网 

### 目标

招聘网站上线，可以后台自由编辑内容和排序

### 目的 

因为钱咖的特殊性，很多流量渠道钱咖都无法开户，所以我们做了一个兼职网站，以兼职招聘网站的名义去开户，用户进入网站后看到一个个APP
试玩赚钱的兼职信息，再将他们引导入钱咖。

### 开发


#### 初始化开发环境

```powershell
make install
```

#### 开发运行

```powershell
make run
```

### 生产部署

机器部署在n1375

上线：

```powershell
ssh n1375

cd /home/www/jianpin8

bash release.sh
```

+ Nginx把/api/xxx的请求转发到jianpin后端代码
+ Nginx把其它请求指到前端代码库目录 [https://git.corp.qianka.com/market/sugar](https://git.corp.qianka.com/market/sugar)