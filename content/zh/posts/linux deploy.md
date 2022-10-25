---
title: "Linux Deploy使用教程"
summary: Linux Deploy使用教程
date: 2022-10-25
tags: ["Linux"]
author: "YSL"
draft: false
weight: 2
---
### 扩容

根目录扩容也就是把linux deploy镜像容量扩容

第一步：用shell连接linux

第二步：

```
dd if=/dev/zero bs=1024 count=1048576 >> /mnt/sdcard/linux.img   
```

其中

- **if 表示input file，表示输入的文件，这里的输入文件为/dev/zero，也就是说扩容的时候，以/dev/zero的内容进行扩容，这里的/dev/zero的内容一般为二进制数据**
- **bs 表示1 block = 1024字节为扩容单位，也就是1K为基本单位扩容**
- **count 表示开辟多少个block，这里是1048576和block，大小即为：1048576/1024/1024 = 1G，也就是说，当前扩容的文件为1GB大小的空间**
- **/mnt/sdcard/linux.img //你的镜像路径。**
- 其他的不需要改



第三步：

```
 e2fsck -f /mnt/sdcard/linux.img
```

第四步：

```
resize2fs /mnt/sdcard/linux.img
```


至此扩容完成，可以查看镜像文件.img已增大。


### 安装服务

1. snapdrop
	
	```
	git clone https://github.com/Bellisario/node-snapdrop.git && cd node-snapdrop
	```
	
	Install all dependencies with NPM: (npm install 失败 更新nodejs)
	
	```
	npm install
	```
	
	Start the server with:
	
	```
	node index.js
	```
	
	### Public Run
	
	If you want to run in your public "sharable" IP instead of locally, you can use this command:
	
	```
	node index.js public
	```
	
	> Remember to check your IP Address using your OS command to see where you can access the server.

2. 更新python

   3.3 安装Python

   回到/root继续安装Python

   ```
   cd ~
   ```

   Python官网的下载页面：

   ```
   https://www.python.org/downloads/source/
   ```

   下载

   ```
   wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz
   tar -zxvf Python-3.9.13.tgz
   cd Python-3.9.13
   ```

   编译

   ```
   LD_RUN_PATH=/usr/local/lib ./configure LDFLAGS="-L/usr/local/lib" CPPFLAGS="-I/usr/local/include"
   LD_RUN_PATH=/usr/local/lib make -j8
   ```
   安装
   ```
   sudo make install
   ```

   

   