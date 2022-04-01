---
title: "git 配置多个账号"
summary: git 配置多个账号
date: 2022-03-28
tags: ["git","github"]
author: "YSL"
draft: false
weight: 2
---

```shell
ssh-keygen -t rsa -f ~/.ssh/id_rsa_x -C "fourousky@163.com".      //一般都是保存在用户目录的.ssh文件夹下面，这里的id_rsa_x是为了和本来有的id_rsa文件作区分
touch config //编写config文件，指明路径
vim config 
```

> 其中config文件主要是为了提交远程仓库的时候，ssh 做区分用的
>
> 填写config 内容

```shell
# 第一个账号，默认使用的账号
Host github.com
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa
# 第二个账号
Host second.github.com  # second为前缀名，可以任意设置
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_x #私钥名称
```

```shell
ssh-agent bash
ssh-add id_rsa # 添加私钥
ssh-add id_rsa_x
```

查看添加的私钥

```shell
ssh-add -l
```

测试是否连通

```shell
ssh -T git@github.com
ssh -T git@second.github.com
```

使用说明

主要区分也是通过HOST区分的，所以在以后的提交和拉去过程中，要主要，如果用的第一个，都是正常pull和push，但是对于第二个，要改成自己设置的别名second.github.com
