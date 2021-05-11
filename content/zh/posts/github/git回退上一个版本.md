---
title: "git回退上一个版本"
summary: git回退上一个版本
date: 2021-04-21
tags: ["git"]
author: "YSL"
draft: false
weight: 3
 https://cdn.pixabay.com/photo/2021/01/15/17/01/green-5919790__340.jpg
---

### git回退到上个版本

```shell
git reset --hard HEAD^
```

###  回退到前3次提交之前，以此类推，回退到n次提交之前

```shell
git reset --hard HEAD~3
```

### 查看commit的sha码

```shell
git log
```

```shell
git show dde8c25694f34acf8971f0782b1a676f39bf0a46
```

### 退到/进到 指定commit的sha码

```shell
git reset --hard dde8c25694f34acf8971f0782b1a676f39bf0a46 
```

### 强推到远程

```
git push origin HEAD --force
```

### 把git add添加进去的文件撤销添加

**git reset HEAD 相对路径名**
```shell
git reset HEAD public/uploads/
```
### git练习地址:
<https://learngitbranching.js.org/?locale=en_US>