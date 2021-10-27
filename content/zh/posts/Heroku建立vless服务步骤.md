---
title: "Heroku建立vless服务"
summary: Heroku建立vless服务
date: 2021-10-27
tags: ["Heroku、vless"]
author: "YSL"
draft: false
weight: 2
---
#### Heroku建立vless服务步骤

1. Fork 本专案到自己的 GitHub 账户（用户名以 `example` 为例）
2. 选取vless分支
3. 修改专案名称，注意不要包含 `v2ray` 和 `heroku` 两个关键字（修改后的专案名以 `demo` 为例）
4. 修改 `README.md`，将 `bclswl0827/v2ray-heroku` 替换为自己的内容（如 `example/demo`）

https://dashboard.heroku.com/new?template=https://github.com/**bclswl0827/v2ray-heroku**

4. 回到专案首页，点击上面的链接以部署 V2Ray
5. 利用[长风网站的UUID生成工具](https://v2rayse.com/v2ray-tools)，更新后复制（**UUID 填写节点时候要用，记得保存**）
![image-20211027153154846](C:\Users\25775\AppData\Roaming\Typora\typora-user-images\image-20211027153154846.png)
6. 如下图填写，然后deploy app（**App name 在cloudflare 反向代理中要用，记得保存**）

<img src="https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211027153322461.png" alt="image-20211027153322461"  />



#### 利用cloudflare 反向代理

[cloudflare地址 ](https://dash.cloudflare.com/7bc91c59cf0aabd0ad1accfb31638dd0/workers/overview)

注册登录使用免费版本（每天有100k次requests）



首页->Workers->Create a Worker

编辑Workers

在左边Script窗口填入

其中**应用名称**是在Heroku中的App name

，右边是host **（host 填写节点时候要用，记得保存）**

打开host+/web 出现 **Bad Request**表示成功

```javascript
addEventListener(
  "fetch",event => {
     let url=new URL(event.request.url);
     url.hostname="应用名称.herokuapp.com";
     let request=new Request(url,event.request);
     event. respondWith(
       fetch(request)
     )
  }
)
```

![image-20211027154253078](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211027154253078.png)



#### 填写vless节点

步骤：

1. 使用[better-cloudflare-ip](https://github.com/badafans/better-cloudflare-ip)工具获取在本网络内最快ip

2. 下载对应版本，打开文件夹中的**CF优选IP.bat** 输入希望最大带宽 建议设置 50

3. 复制ip

4. 填写

   地址填写ip

   用户id 复制之前用长风网站工具生成的UUID

   伪装域名用 cloudflare中的混淆host不要**https://** ，以dev结尾的。

   ![image-20211027155424187](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211027155424187.png)
