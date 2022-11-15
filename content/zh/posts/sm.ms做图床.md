---
title: "sm.ms作为图床"
summary: sm.ms作为图床
date: 2022-11-15
tags: [" sm.ms"]
author: "YSL"
draft: false
weight: 3
---
### 1、使用[sm.ms官网](https://link.zhihu.com/?target=https%3A//sm.ms/)进行注册，



![img](https://s2.loli.net/2022/11/15/yTrmKvMwqftbH5k.webp)

注册账号



### 2、登录后进入面板界面



![img](https://s2.loli.net/2022/11/15/7gqt4GejMnAJ9LI.webp)

dashborad



### 3、获取token



![img](https://s2.loli.net/2022/11/15/PMRm5TAFIbDQLhz.webp)

获取token



### 4、Typora配置图床



![img](https://s2.loli.net/2022/11/15/DBMxQncT5O3aLPo.webp)

文件-偏好设置



在第5步的时候将文件配置为

```json
{
  "picBed": {
    "current": "smms",
    "smms": {
      "token": "这里是你的 SM.MS 账号的 API Token"
    }
  },
  "picgoPlugins": {}
}
```

### 5、复制图片即可返回文件的url地址，也可在官网中查看到已上传的图片



![img](https://s2.loli.net/2022/11/15/BPDuE7ObWqyMG2Y.webp)

已上传的图片