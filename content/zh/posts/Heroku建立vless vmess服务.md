---
title: "Heroku建立vless vmess服务"
summary: Heroku建立vless vmess服务
date: 2021-10-27
tags: ["Heroku","vless","vmess"]
author: "YSL"
draft: false
weight: 2
---
#### Heroku建立vless服务步骤

1. 将[HerokuXray](https://github.com/Lbingyi/HerokuXray)Fork 本专案到自己的 GitHub 账户（用户名以 `example` 为例）
2. 选取vless分支
3. 修改专案名称，注意不要包含 `v2ray` 和 `heroku` 两个关键字（修改后的专案名以 `demo` 为例）
4. 修改 `README.md`，将 `Lbingyi/HerokuXray` 替换为自己的内容（如 `example/demo`）
![](https://gitee.com/yslinxx/image-bed/raw/master/images/126950598-7930a0ac-739a-46ac-aef2-afa2d213a06c.png)
```
https://dashboard.heroku.com/new?template=https://github.com/bclswl0827/v2ray-heroku
```



5. 回到专案首页，点击上面的链接以部署 V2Ray

5. 利用[长风网站的UUID生成工具](https://v2rayse.com/v2ray-tools)，更新后复制（**UUID 填写节点时候要用，记得保存**）
![image-20211027211543908](https://gitee.com/yslinxx/image-bed/raw/master/images/image-20211027211543908.png)
6. 如下图填写，然后deploy app（**App name 在cloudflare 反向代理中要用，记得保存**）

![](https://gitee.com/yslinxx/image-bed/raw/master/images/20211205144319.png)


#### 利用cloudflare 反向代理

[cloudflare地址 ](https://dash.cloudflare.com/7bc91c59cf0aabd0ad1accfb31638dd0/workers/overview)

注册登录使用免费版本（每天有100k次requests）



首页->Workers->Create a Worker

编辑Workers

在左边Script窗口填入

其中**应用名称**是在Heroku中的App name

右边是host **（host 填写节点时候要用，记得保存）**

> 打开host+/web 出现 **Bad Request**表示成功
>

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

1.  关于CF筛选IP
* 请参考 [CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest) `推荐`
* 请参考 [better-cloudflare-ip](https://github.com/badafans/better-cloudflare-ip)

2. 下载对应版本，打开文件夹中的**CF优选IP.bat** 输入希望最大带宽 建议设置 50

3. 复制ip

4. 填写

   地址填写ip

   用户id 复制之前用长风网站工具生成的UUID

   伪装域名用 cloudflare中的混淆host不要**https://** ，以dev结尾的。

   ![](https://gitee.com/yslinxx/image-bed/raw/master/images/20211205144747.png)
```
* 客户端下载：https://github.com/2dust/v2rayN/releases
* 代理协议：vless 或 vmess
* 地址：xxx.herokuapp.com
* 端口：443
* 默认UUID：24b4b1e1-7a89-45f6-858c-242cf53b5bdb
* vmess额外id：0
* 加密：none
* 传输协议：ws
* 伪装类型：none
* 伪装域名：xxx.workers.dev(CF Workers反代地址)
* 路径：/24b4b1e1-7a89-45f6-858c-242cf53b5bdb-vless // 默认vless使用(/自定义UUID码-vless)，vmess使用(/自定义UUID码-vmess)
* 底层传输安全：tls
* 跳过证书验证：false
```