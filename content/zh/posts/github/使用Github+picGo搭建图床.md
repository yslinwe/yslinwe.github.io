---
title: "使用Github+picGo搭建图床"
summary: 使用Github+picGo搭建图床
date: 2022-07-21
tags: ["Github","picGo"]
author: "YSL"
draft: false
weight: 3


---

## **1. 注册一个Github账号**

首先你需要一个github账号，如果没有的话，先注册。

github官网地址： [https://github.com/](https://link.zhihu.com/?target=https%3A//github.com/)

注册过程省略，因为这是保姆都不管的事情。

友情提示：可能在注册过程中会出现 “Unable to verify your captcha response… …”，一直不能正常注册。

网上有各种解决方案：换浏览器、换电脑… …

## 2. 配置Github

### 2.1 创建一个新仓库，用于存放图片。

![img](https://pic1.zhimg.com/80/v2-59b7f87b4fbe21a2492e4b9e529fe87c_720w.jpg)

填写仓库名称和描述，且仓库必须是public的，否则存储的图片不能正常访问。

![img](https://pic3.zhimg.com/80/v2-d3733c14e8c9b53cb5cf9f7607d51c8a_720w.jpg)

### 2.2 生成一个token，用于picGo访问github

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-4d227062bcfa58dba6c0582c982b737b_720w.jpg)

选择左侧菜单的Developer settings

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-4d227062bcfa58dba6c0582c982b737b_720w.jpg)

之后选择左侧Personal access tokens，再点击Generate new token

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-2d5bcabac97557591c4203009d306750_720w.jpg)

填写Note，勾选repo.

![img](https://pic2.zhimg.com/80/v2-346da4ccf189eb5997abe2fadadca331_720w.jpg)

注意，生成的token只会在这里显示一次，所以记得单独保存下来哦。

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-354ea85a4bd9cfc99157b86cae9a2332_720w.jpg)

至此，Github的配置完成。

## 3. 下载picGo，并进行配置

### 3.1 下载

网络不好的情况下，PicGo下载可能会多次失败，所以我把下载好的应用放在百度网盘了。

大家按需取用。

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-279f576c0dc0861fd7edcf1d43e5675f_720w.jpg)

网盘地址：[https://pan.baidu.com/s/1LvkzLJyZcjpflK2Evq3X9A](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1LvkzLJyZcjpflK2Evq3X9A) 提取码：s6x7

下载完成，双击启动安装即可。

如果安装成功，picGo不能正常使用，则可以用兼容模式启动。【此问题因电脑而异，也是我在配置过程中踩过的坑。】

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-3f60ccb549e01c95a1702ceca9bda95d_720w.jpg)

### 3.2 配置

仓库名：[github用户名]/[第一步新建的仓库名称]

分支：默认master，从2020.10.01开始，github的默认分支名变更为main

设定token：第一步创建的token

指定存储路径：可填可不填，如果填写了，图片就会存储在img文件夹下

设定自定义域名：https://cdn.jsdelivr.net/gh/[github用户名]/[仓库名]@main，注意，此处的分支一定要填写@main，否则默认使用master分支。而现在github创建的默认分支名为main，如果不指定，则会出现图片不能上传的情况。【踩坑两小时】

![img](https://pic3.zhimg.com/80/v2-62e4faaa7999d1d32fa80aec44b4034e_720w.jpg)

至此，github+picGo的配置完成，可以在上传区进行图片上传了。

### 3.3 补充几点

1.原本github的自定义域名应该是：[https://raw.githubusercontent.com/[username\]/[仓库名]](https://link.zhihu.com/?target=https%3A//raw.githubusercontent.com/%5Busername%5D/%5B%E4%BB%93%E5%BA%93%E5%90%8D%5D)

但是使用这种方式访问图片巨慢，所以教程中使用了jsdelivr作为cdn加速。改变域名即可，不需要任何其他配置。

2.配置完成，可能出现不能上传的情况，请大家耐心检查，也许某一步的配置出现了问题，就像检查bug一样耐心、细心。想象一下图床搭建成功后，写起文章来的丝滑感，是不是又有动力了？

## 4. PicGo集成Typora

使用MarkDown语法写文章，我使用的编辑器是typora，一款超级好用的编辑器。在一个编辑框内，编辑完成后，可以马上显示MarkDown语法效果。

举个栗子：

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-ce0b207c19d6ca32ac22937f1dc6cfcd_720w.jpg)

并且typora可以和picGo联合在一起使用，当你在编辑器中插入、粘贴图片时，typora+picGo的组合方式，可以自动把图片上传至github保存。

### 4.1 下载安装

Typora新版本是收费的，所以建议大家使用旧版本就可以了，完全能满足写作需求。

旧版本安装包和picGo放在一起了（下载地址见上文），大家按需取用即可。

下载完成后正常步骤安装即可。

### 4.2 配置

在typora顶部菜单界面，选择“文件” - > “偏好设置”，设置图片存储方式。

![img](https://pic1.zhimg.com/80/v2-f595cf5c8a0e3b62944c68deb8fb5878_720w.jpg)

选择图片存储方式：上传图片。

上传服务：PicGo(app)

PicGo路径：picGo安装的地址

设置完成，点击“验证图片上传”，提示上传成功，即代表配置成功。

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-e27e9f198aef7bdea365549b2257025d_720w.jpg)

注意一点，typora图片验证中的端口，需要与picGo中的server设置内的端口一致，否则typora中不能正常上传。



### 4.3 picGo监听端口设置

选择“PicGo设置”–>“设置server”

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-8ff622935a6b0597a21e68e7575e16ef_720w.jpg)

【此处有坑】如果监听端口不是36677，则需要修改为36677。否则会出现picGo能正常上传 图片，而typora上传图片失败的情况。

![img](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/v2-304589efaed9a1ba3caf5e8827e77582_720w.jpg)

最后，在苹果电脑中可以使用**Typora+Ipic+Github**的方式，有兴趣的话可以自行尝试

**总结：github+picGo+typora他们三个是好基友。**