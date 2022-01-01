---
title: "playtube宝塔安装"
summary: playtube宝塔安装
date: 2022-01-01
tags: ["playtube"]
author: "YSL"
draft: false
weight: 2
---
### Step1. 安装宝塔

根据自己的系统类型安装宝塔（宝塔软件官网：https://www.bt.cn/）

```
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh
```

### Step2. 安装软件

进入宝塔控制面板安装LAMP组合 (Nginx，Mysql，Pureftpd，Phpmyadmin，PHP)

### Step3. 安装PlayTube

下载 [PlayTube v1.4.2](https://pan.baidu.com/s/1V8GSpXviXxT9YdxlsXFjnQ) 提取码:3j9j 将程序上传到网站根目录解压，添加站点并添加伪静态规则，然后重启nginx：

```
if (!-f $request_filename){
    set $rule_0 1$rule_0;
}
if (!-d $request_filename){
    set $rule_0 2$rule_0;
}
if ($rule_0 = "21"){
    rewrite ^/$ /index.php?link1=home ;
}
rewrite ^/$ /index.php?link1=home ;
rewrite ^/reset-password/([^/]+)(/|)$ /index.php?link1=reset-password&code=$1 ;
rewrite ^/confirm/(.*)/(.*)$ /index.php?link1=confirm&code=$1&email=$2 ;
rewrite ^/api/v(([0-9])([.][0-9]+))(/|)$ /api.php?v=$1 ;
rewrite ^/admin-cp$ /admincp.php ;
rewrite ^/admin-cp/(.*)$ /admincp.php?page=$1 ;
rewrite ^/admin-cdn/(.*)$ /admin-panel/$1 last;
rewrite ^/videos/category/(.*)/rss(/|)$ /index.php?link1=videos&page=category&id=$1&feed=rss ;
rewrite ^/videos/category/(.*)$ /index.php?link1=videos&page=category&id=$1 ;
rewrite ^/videos/(.*)/rss(/|)$ /index.php?link1=videos&page=$1&feed=rss ;
rewrite ^/videos/(.*)$ /index.php?link1=videos&page=$1 ;
rewrite ^/articles(/|)$ /index.php?link1=articles ;
rewrite ^/articles/category/(.*)$ /index.php?link1=articles&category_id=$1 ;
rewrite ^/articles/read/(.*)$ /index.php?link1=read&id=$1 ;
if (!-f $request_filename){
    set $rule_14 1$rule_14;
}
if (!-d $request_filename){
    set $rule_14 2$rule_14;
}
if ($rule_14 = "21"){
    rewrite ^/aj/([^/.]+)/?$ /ajax.php?type=$1&first=$2 last;
}
rewrite ^/aj/([^/.]+)/([^/.]+)/?$ /ajax.php?type=$1&first=$2 last;
rewrite ^/aj/([^/.]+)/([^/.]+)/([^/.]+)/?$ /ajax.php?type=$1&first=$2&second=$3 last;
rewrite ^/edit-video/(.*)?$ /index.php?link1=edit-video&id=$1 last;
rewrite ^/watch/([^/]+)(/|)?$ /index.php?link1=watch&id=$1 last;
rewrite ^/watch/([^/]+)/list/([^/]+)(/|)?$ /index.php?link1=watch&id=$1&list=$2 last;
rewrite ^/embed/(.*)?$ /index.php?link1=embed&id=$1 last;
rewrite ^/resend/(.*)/(.*)?$ /index.php?link1=resend&id=$1&u_id=$2 last;
rewrite ^/redirect/(.*)?$ /index.php?link1=redirect&id=$1 last;
rewrite ^/settings/(.*)/(.*)$ /index.php?link1=settings&page=$1&user=$2 ;
rewrite ^/settings/(.*)$ /index.php?link1=settings&page=$1 ;
rewrite ^/terms/([^/]+)(/|)$ /index.php?link1=terms&type=$1 ;
rewrite ^/go_pro(/|)$ /index.php?link1=go_pro ;
rewrite ^/ads(/|)$ /index.php?link1=ads ;
rewrite ^/ads/create(/|)$ /index.php?link1=create_ads ;
rewrite ^/ads/edit/(d+)(/|)$ /index.php?link1=edit_ads&id=$1 ;
rewrite ^/contact-us(/|)$ /index.php?link1=contact ;
rewrite ^/@([^/]+)(/|)$ /index.php?link1=timeline&id=$1 ;
rewrite ^/messages/(.*)$ /index.php?link1=messages&id=$1 ;
if (!-f $request_filename){
    set $rule_33 1$rule_33;
}
if (!-d $request_filename){
    set $rule_33 2$rule_33;
}
if ($rule_33 = "21"){
    rewrite ^/([^/]+)(/|)$ /index.php?link1=$1 ;
}
```

### Step4. 网站域名(站点)进行安装

通过phpmyadmin进入到数据库，找到PlayTube所使用数据库，删除langs表，再将根目录里的langs.sql文件导入到数据库即可。授权码：nulled-by-reishi。刷新网站会看到有右下角语言有中文的，如果选择中文后，分类显示不出来，可能是分类语言乱码，这时候我们去根目录assets/langs，将乱码的语言文件改成中文.php即可。

### Step5. 要使用程序完整的功能，还需要安装ffmpeg，这里直接使用ffmpeg一键脚本。

```
wget https://www.moerats.com/usr/shell/ffmpeg.sh && sh ffmpeg.sh
ffmpeg -version
```

打开宝塔，点击：软件管理-PHP设置-禁用函数-删除shell_exec。

### Step6. 视频分类设置

网站目录./assets/langs/中文.php修改。

### Step7. 编辑样式表

./themes/default/css，主样式文件是style.css #添加自己的代码 想在head、body、footer标签中添加自己的代码，请在./themes/default/layout/container.html修改