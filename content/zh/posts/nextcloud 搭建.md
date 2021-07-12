---
title: "nextcloud搭建"
summary: nextcloud搭建
date: 2021-07-12
tags: ["nextcloud"]
author: "YSL"
draft: false
weight: 3
---

### 搭建网盘过程

### 1.安装docker

#### 通过yum源安装docker

```shell
sudo yum -y install docker
```

### 启动docker

```shell
sudo systemctl start docker
```

### 开机自启

```shell
sudo systemctl enable docker
```

### 2.获取nextcloud镜像, 完成网盘搭建

```shell
docker run -d -p 8080:80 nextcloud
```

