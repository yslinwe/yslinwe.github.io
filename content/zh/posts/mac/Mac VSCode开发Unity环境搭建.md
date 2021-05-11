---
title: "Mac VSCode开发Unity环境搭建"
summary: Mac VSCode开发Unity环境搭建
date: 2021-04-20
tags: ["VSCode Unity环境搭建"]
author: "YSL"
draft: false
weight: 3
 https://cdn.pixabay.com/photo/2019/10/02/06/27/mood-4520112__340.jpg
---
### 配置后的效果如下:

![](https://img.imgdb.cn/item/607d80f18322e6675caa93c1.gif)

### 1. 安装Unity
### 2.下载安装.Net Core SDK

![](https://img.imgdb.cn/item/607d823b8322e6675cad6399.png)

<https://dotnet.microsoft.com/download/dotnet>

运行命令检查安装是否成功
```shell
dotnet --version
```
![dotnet下载链接](https://img.imgdb.cn/item/607d82f28322e6675caeed1d.png)

### 3.下载安装Mono SDK

![](https://img.imgdb.cn/item/607d832e8322e6675caf717f.jpg)

<https://www.mono-project.com/download/stable/>

运行命令检查安装是否成功

```shell
mono --version
```

![](https://img.imgdb.cn/item/607d84f78322e6675cb380c2.png)

### 4. 安装VsCode
#### 4.1 安装VsCode插件

``` shell
C#
C# Extensions
C# FixFormat Fixed
Debugger for Unity
Unity Tools
Unity Code Snippets
Unity Snippets
```

#### 4.2 VsCode 配置omnisharp路径

设置路径
```
Code -> Preferences -> Settings, 检索mono, 点击settings.json
```

![](https://img.imgdb.cn/item/607d86dd8322e6675cb7eaca.png)

![](https://img.imgdb.cn/item/607d89468322e6675cbe0f86.png)

#### 配置omnisharp(很重要)

![](https://img.imgdb.cn/item/607d89ec8322e6675cbfd07d.png)

```shell
"omnisharp.monoPath": "/Library/Frameworks/Mono.framework/Versions/Current/Commands/mono",
"omnisharp.useGlobalMono": "always"
```

#### 设置.zshrc/.bash_profile环境变量(很重要)

```shell
export FrameworkPathOverride=/Library/Frameworks/Mono.framework/Versions/Current
```

#### 5.设置Unity代码编辑器

![](https://img.imgdb.cn/item/607d8ae58322e6675cc2c136.jpg)
