---
title: "aria2 简单使用"
summary: aria2 简单使用
date: 2021-07-03
tags: ["aria2"]
author: "YSL"
draft: false
weight: 2
---
### aria2 简单使用

整体方案是 独立的 aria2 程序 + aria2-conf + Chrome 插件

#### aria2

在 https://github.com/aria2/aria2/releases 下载最新的 Release

#### aria2-conf

使用 https://github.com/ttttmr/aria2-conf 的配置文件，下载 zip 包即可（或者 `git clone`）

### 配置

把下好的压缩包解压，存一起，重命名一下

```
aria2-1.34.0-win-64bit-build1` -> `bin
aria2-conf-master` -> `conf
```

[![img](https://tmr.js.org/p/1aa3893d/aria2.png)](https://tmr.js.org/p/1aa3893d/aria2.png)

先给 aria2 的 bin 配上环境变量，也方便命令行里用

然后配置一下 `conf/aria2.conf` 文件就可以用了

主要更改如下

```
#设置密码
18 rpc-secret = xxxxxx
...
89 dir = D:\Download
#填默认下载目录
```

双击 `HideRun.vbs` 就可以启动 aria2 了，需要自启的话可以将快捷方式发送到开始菜单 startup 里

> startup 在这里 `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`

> 启动双击 start.bat ，后台运行双击 HideRun.vbs ，关闭双击 stop.bat ，重启双击 restart.bat

### Chrome 联动

Chrome 插件用的是 [Aria2 for Chrome](https://chrome.google.com/webstore/detail/aria2-for-chrome/mpkodccbngfoacfalldjimigbofkhgjn)

一共有 2 个要填密码的地方

一个是在[插件设置](chrome-extension://mpkodccbngfoacfalldjimigbofkhgjn/options.html)填 RPC 地址

`http://token:xxxx@localhost:6800/jsonrpc` xxx 是你设置的密码

一个是 [ariang](chrome-extension://mpkodccbngfoacfalldjimigbofkhgjn/ui/ariang/index.html#!/settings/ariang) 的 RPC 配置

[![img](https://tmr.js.org/p/1aa3893d/ariang.png)](https://tmr.js.org/p/1aa3893d/ariang.png)