---
title: "Win TASKKILL 杀死进程"
summary: Win TASKKILL 杀死进程
date: 2022-01-27
tags: ["Win","TASKKILL"]
author: "YSL"
draft: false
weight: 2
---
#### 参数列表
1. /S    system    指定要连接的远程系统。  

2. /U    [domain\]user    指定应该在哪个用户上下文执行这个命令。

3. /P    [password]       为提供的用户上下文指定密码。如果忽略，提示输入。

4. /FI   filter           应用筛选器以选择一组任务。允许使用 "*"。例如，映像名称 eq acme*

5. /PID  processid        指定要终止的进程的 PID。使用 TaskList 取得 PID。

6. /IM   imagename        指定要终止的进程的映像名称。通配符 '*'可用来 指定所有任务或映像名称。

7. /T                     终止指定的进程和由它启用的子进程。

8. /F                     指定强制终止进程。

9. /?                     显示帮助消息。

#### 杀死对应进程

```shell
taskkill /pid pid  

taskkill /im xxx.exe  

taskkill /fi "imagename eq xxx.exe"  

taskkill /fi "pid eq pid" 
```

可以加 /T /F 强制终止
```shell
taskkill  /T /F  /IM xxx
```