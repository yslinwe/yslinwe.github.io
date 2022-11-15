---
title: "Aria2 VPS下载器"
summary: Aria2 VPS下载器
date: 2021-11-12
tags: ["aria2"]
author: "YSL"
draft: false
weight: 3
---
1. 安装Aria2

```shell
wget -N https://git.io/aria2.sh && chmod +x aria2.sh && bash aria2.sh
```

系统要求：CentOS 6+ / Debian 6+ / Ubuntu 14.04+。

输入“1”开始安装，完成后记录下图的信息：

![15-图2](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE2.jpg)

2. 安装AriaNg

手机端安装包：[点击下载](https://github.com/Xmader/aria-ng-gui-android/releases/tag/v1.2.3) ；

依次点击“AriaNg设置”——“RPC”，

> 在Aria2 RPC地址栏输入之前记录的Aria2配置信息的地址，在Aria2 RPC密钥栏中输入之前记录的Aria2配置信息的密钥，然后点击“Reload Page”即可远程连接Aria2。

![15-图4-1-738x1536](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE4-1-738x1536.jpg)

Windows系统安装包：[点击下载](https://github.com/Xmader/aria-ng-gui/releases/tag/v3.1.0)；

设置方法和手机端一样.

3. 安装可道云

   安装宝塔

   ```shell
   yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
   ```

   其他VPS系统脚本命令可以到宝塔[官方网站](https://www.bt.cn/)查询，安装完成后登录宝塔面板，安装运行环境，这里需要注意要安装PHP7.2，否则无法安装可道云。

   ![15-图9](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE9.jpg)

然后安装宝塔一键部署源码![15-图10-1536x536](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE10-1536x536.jpg)

然后一键部署可道云，域名栏输入VPS的ip即可：

![15-图11-1536x674](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE11-1536x674.jpg)

点击“提交”开始部署，然后访问站点并设置密码：

![15-图12](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE12.jpg)

![15-图13](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE13.jpg)

4. 更改Aria2的默认下载目录；

   由于AriaNg无法管理所下载的文件，比如对文件进行打开或删除的操作，所以需要把Aria2的默认下载目录修改到可道云中，在可道云的【我的文档】建一个名为【download】的文件夹：

![15-图15](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE15.jpg)

右键点击文件夹download，打开属性，记录下完整的路径.

再次执行

```shell
wget -N https://git.io/aria2.sh && chmod +x aria2.sh && bash aria2.sh
```

输入“7”，再输入“3”，然后粘贴上面的路径就可以修改Aria2的默认下载目录：

> 记得放行6800端口；因为安装了宝塔面板，会屏蔽部分端口，包括6800端口，导致Aria2无法连接，所以需要通过宝塔面板放行6800端口，操作方法如下图：

![15-图19-1536x510](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/15-%E5%9B%BE19-1536x510.jpg)