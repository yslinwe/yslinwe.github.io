---
title: "解决VSCode无法显示Unity代码提示的真正解决办法"
summary: 解决VSCode无法显示Unity代码提示的真正解决办法
date: 2021-08-11
tags: ["VSCode、Unity"]
author: "斯幽柏雷科技"
draft: false
weight: 2
---

## 步骤1：验证是否正确打开工程目录

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/20200422152014455.png)

> 你可以查看VSCode左侧的资源管理器，查看列表当中是否有sln文件。如果有继续往下看。

## 步骤2：验证工程是否指定正确

[VSCode无法进行Unity C#智能提示，代码补全以及方法跳转等功能的解决方案！](https://blog.csdn.net/qq_28299311/article/details/103060182)

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/2019111400573910.png)

按下键盘的Ctrl/Command + Shift+ P快捷键，选定工程目录下的sln文件。
至此，如果你以前是有代码提示的，稍等几秒等待自动加载完成以后你可以重试一下是否有代码提示功能

## 步骤3：检查和安装对应的.NET开发者版本

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/20201126055114718.png)

记住你的版本号，到这下载对应版本号的开发者版 .NET Framework 。
https://docs.microsoft.com/zh-cn/dotnet/framework/deployment/deployment-guide-for-developers

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/20201126055534771.png)

1. **注意你需要下载Developer版本的**，如果是Runtime版本很可能安装的时候会提示你已经安装了当前或更高版本的.NET从而拒绝你安装。当然稳妥方式都装一遍…
2. 装完以后，重开VSCode。你期待的代码提示就会出现了！

# 其他相关

## 利用控制台定位问题

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/20201126060745582.png)

1.留意你的VSCode控制台输出面板，通常在这里会弹出启动报错信息。仔细阅读输出的报错信息，大部分错误都会有告诉你解决问题的方式。

## 代码提示有了，但找不到UnityEngine.UI等类

步骤1：点开Unity的 Package Manager，找到右Visual Studio Code Editor，选择1.2.0以后的版本，然后点击右下角的升级按钮。(注意如果你用的2019,插件不要用太新的版本.否则还是会出现.不出来的情况.)

步骤2：保存并关闭Unity和VSCode，到工程目录下删除所有的*.sln和*.csproj文件。
步骤3：重新打开Unity和这个工程，刚被删除的这两个文件将会被重新创建，届时这个故障就解决了。
如果你不想重启unity和vscode参照这个帖子https://blog.csdn.net/weixin_45476117/article/details/108911678

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/20201126064747574.png)

## gameobject什么的只能.出一个智能引用

这里还是Unity Package Manager的插件惹的祸,我这里用1.2.0可以但是升级到1.2.3就出现这个问题.建议降级到低版本尝试.

![在这里插入图片描述](https://gitee.com/yslinxx/image-bed/raw/master/images/2021030421114365.png)