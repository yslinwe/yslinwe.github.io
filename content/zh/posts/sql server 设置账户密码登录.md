---
title: " sql server 设置账户密码登录"
summary:  sql server 设置账户密码登录
date: 2021-10-25
tags: ["sql server"]
author: "YSL"
draft: false
weight: 2
---
#### sql server 设置账户密码登录

```shell
打开Microsoft SQL Server Management Studio -> 视图 -> 已注册的服务器
```

```shell
打开数据库引擎->本地服务器组- >右键属性 
```

- 身份验证 设置 **SQL Server 身份验证** 
- 设置 登录名和密码

![image-20211025120849634](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211025120849634.png)

#### 对象资源管理器 设置

```shell
右键属性->安全性->设置 SQL Server 和 Windows 身份验证模式 和 失败和成功的登录
```

![image-20211025121154573](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211025121154573.png)

#### 重启服务

右键属性->重新启动 

![image-20211025122430875](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211025122430875.png)

#### 选择账户密码登录

![image-20211025122814413](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211025122814413.png)

