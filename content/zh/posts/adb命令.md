---
title: "adb命令"
summary: adb命令
date: 2021-05-21
tags: ["adb命令"]
author: "YSL"
draft: false
weight: 2
---
### adb命令是：
adb shell dumpsys meminfo
1、查看将要启动或退出app的包名

```
adb shell am monitor（只有在启动或退出的时候才会打印）
```
2、查看内存情况

```
adb shell dumpsys meminfo
```

3、查看安装的第三方app的包名

```
adb shell pm list packages -3
```
4、查看当前界面的app的包名

```
adb shell dumpsys window windows | findstr mFocusedApp
```
5、查看启动的app的包名

```
adb shell dumpsys activity top | find "ACTIVITY"
```
6、查看所有启动的应用的包名

```
adb shell dumpsys activity activities | findstr "Run"
```
7、查看当前启动应用的包名

```
adb shell dumpsys window w |findstr \/ |findstr name=
```
8、通过应用查看包名

```
aapt dump badging D:\test\xxx.apk(APK的全名)
```
（aapt不是可运行命令的话，需要配置环境）


9、其他方法

（1、查看进程的方法查看包名 2、查看日志的方法 3、直接在手机设置打开应用与权限查看）

**有些命令需要adb root ；  adb remount 之后才能使用 ;( remount不成功的话用：adb shell verity-disabled 运行之后重启手机在remount)