---
title: "git 添加子项目"
summary: Git submodule添加子项目/库
date: 2021-07-30
tags: ["git"]
author: "YSL"
draft: false
weight: 2
---
开发过程中，经常会有一些通用的部分希望抽取出来做成一个公共库来提供给别的工程来使用，而公共代码库的版本管理是个麻烦的事情。git submodule命令就可以解决这个问题。

Git归并策略
Git归并有两种策略：递归，章鱼。

1.递归策略：当分支数只有两个的时候。

2.章鱼策略：当分支数大于两个的时候。

Git会自动选择归并的方法。

3.子树策略：是Git另一种归并方法。（submodule）

它可以把另一个子项目，嵌入到当前项目。而且会非常聪明的合并这些子项目。

添加
为当前工程添加submodule，命令如下：
```shell
git submodule add 仓库地址 路径
```
其中，仓库地址是指子模块仓库地址，路径指将子模块放置在当前工程下的路径。
注意：路径不能以 / 结尾（会造成修改不生效）、不能是现有工程已有的目录（不能順利 Clone）
示例:
```shell
git submodule add -f http://git.cs/Cmblife_iOS_Internal/modulesLib.git
```
-f 是强制的意思，一般不需要加
命令执行完成，会在当前工程根路径下生成一个名为“.gitmodules”的文件，其中记录了子模块的信息。添加完成以后，再将子模块所在的文件夹添加到工程中即可。

删除
submodule的删除稍微麻烦点：首先，要在“.gitmodules”文件中删除相应配置信息。然后，执行“git rm –cached ”命令将子模块所在的文件从git中删除。
下载的工程带有submodule

当使用git clone下来的工程中带有submodule时，初始的时候，submodule的内容并不会自动下载下来的，此时，只需执行如下命令：
```shell
git submodule update –init –recursive
```
即可将子模块内容下载下来后工程才不会缺少相应的文件。
————————————————
版权声明：本文为CSDN博主「糖果屋的世界」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ajdfhajdkfakr/article/details/77892137