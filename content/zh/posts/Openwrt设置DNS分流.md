---
title: "Openwrt设置DNS分流"
summary: Openwrt设置DNS分流
date: 2022-11-20
tags: ["Openwrt,SmartDNS,Adguard "]
author: "YSL"
draft: false
weight: 2
---



### SmartDNS设置

```
https://8.8.8.8/dns-query
https://8.8.4.4/dns-query
https://doh.opendns.com/dns-query
https://doh.dns.sb/dns-query
https://dns9.quad9.net/dns-query
https://1.1.1.1/dns-query
```

自定义设置

```
bind :6453 -group GW -no-speed-check
bind :5335 -group GW -no-speed-check
```

### Adguard Home 设置

上游DNS服务器

```
https://dns.alidns.com/dns-query
https://doh.pub/dns-query
```

设置并行请求

Bootstrap DNS 服务器

```
0.0.0.0
```

DNS 拦截列表

```
https://cdn.jsdelivr.net/gh/o0HalfLife0o/list@master/ad-mo.txt
```

### DNS服务配置

勾选

- [x] 启用EDNS客户端子网

- [x] 启用DNSSEC

  

### DNS重写

```
dns.alidns.com
223.6.6.6

doh.pub
1.12.12.12
```



### 设置上网域名

doh.opendns.com
doh.dns.sb
dns9.quad9.net