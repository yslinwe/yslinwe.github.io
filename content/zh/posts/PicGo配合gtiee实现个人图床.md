---
title: "PicGo配合gtiee实现个人图床"
summary: PicGo配合gtiee实现个人图床
date: 2021-04-23
tags: ["PicGo","个人图床"]
author: "YSL"
draft: false
weight: 3
---
### 安装软件

1. 安装 node.js [下载地址](https://nodejs.org/en/)

2. 安装PicGO客户端 [下载地址](https://github.com/Molunerfinn/PicGo/releases)

3. 在Picgo里面安装Gitee扩展插件
   
   ![截屏2021-04-23 上午11.04.39](https://gitee.com/yslinxx/image-bed/raw/master/images/%E6%88%AA%E5%B1%8F2021-04-23%20%E4%B8%8A%E5%8D%8811.04.39.png)

3. 安装完成后重启应用在图床设置会显示gitee

      ![截屏2021-04-23 上午11.08.03](https://gitee.com/yslinxx/image-bed/raw/master/images/%E6%88%AA%E5%B1%8F2021-04-23%20%E4%B8%8A%E5%8D%8811.08.03.png#pic_left)

   ### 注册Gitee账号并创建图床仓库，获取Token

   1. 自行注册账号，创建仓库，仓库记得初始化。  [Gitee官网](https://gitee.com/)

   2. ```shell
      个人图片下拉栏 -> 设置 -> 私人令牌 
      ```

      在设置中创建私人令牌（Token）自行保存好，它只会在创建的时候显示一次，之后就不再显示，只能重新生成或者创建

         ![截屏2021-04-23 上午11.14.06](https://gitee.com/yslinxx/image-bed/raw/master/images/%E6%88%AA%E5%B1%8F2021-04-23%20%E4%B8%8A%E5%8D%8811.14.06.png)

### 配置Picgo上的Gitee

   ![截屏2021-04-23 上午11.15.30](https://gitee.com/yslinxx/image-bed/raw/master/images/%E6%88%AA%E5%B1%8F2021-04-23%20%E4%B8%8A%E5%8D%8811.15.30.png)

**至此Picgo搭配Gitee的图床就搭建完了** 

**刚快尝试上传图片吧。**

### 使用Typora的Picgo插件

1. 下载 Typora [下载地址](https://typora.io/)
2. 配置Picgo
   1. 进入Typora设置

      ![截屏2021-04-23 上午11.28.06](https://gitee.com/yslinxx/image-bed/raw/master/images/%E6%88%AA%E5%B1%8F2021-04-23%20%E4%B8%8A%E5%8D%8811.28.06.png)

2. 该设置完成之后，直接将图片复制进Typora 的编辑区即可完成图片的上传，并且文章使用的图片Url就是图床相应的Url。