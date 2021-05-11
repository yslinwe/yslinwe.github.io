---
title: "Docker删除镜像和容器"
summary: Docker删除镜像和容器
date: 2021-05-10
tags: ["Docker"]
author: "YSL"
draft: false
---

### Docker删除镜像和容器

#### 查看运行的容器

```shell
docker ps
```

#### 查看已经退出的容器

```shell
docker ps -a
```

#### 删除镜像

```shell
docker rmi -f 镜像id
```

#### 删除容器

```shell
docker rm -f 容器id
```

