---
title: "谷歌云开启SSH及设置root密码"
summary: 谷歌云开启SSH及设置root密码
date: 2021-12-02
tags: ["谷歌云"]
author: "YSL"
draft: false
weight: 3
---
一、设置root密码
1.先选择从浏览器打开ssh连接服务器
LINUX | 谷歌云开启SSH及设置root密码
2.切换到root账号
sudo -i
3.设置root密码
passwd
然后会要求输入新密码，然后再重复一次密码，输入密码的时候不会显示出来，所以直接输入密码，然后回车，再然后重复输入密码回车
LINUX | 谷歌云开启SSH及设置root密码 – Vedio Talk - VLOG、科技、生活、乐分享

二、开启SSH权限
①方法一
1.修改SSH配置文件/etc/ssh/sshd_config
vi /etc/ssh/sshd_config
2.然后再输”i”进入编辑模式
i
3.找到以下内容并修改
PermitRootLogin yes           //默认为no，需要开启root用户访问改为yes
PasswordAuthentication yes    //默认为no，改为yes开启密码登陆
LINUX | 谷歌云开启SSH及设置root密码 – Vedio Talk - VLOG、科技、生活、乐分享

4.修改完成后，再下按 esc 键，然后再输入
:wq
LINUX | 谷歌云开启SSH及设置root密码 – Vedio Talk - VLOG、科技、生活、乐分享

5.重启SSH服务
service sshd restart
②方法二
CentOS和Debian通用，输入以下两条命令
sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
Ubuntu系统，输入以下两条命令
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
重启服务器
reboot