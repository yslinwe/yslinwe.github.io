---
title: "OneDriveUploader使用"
summary: OneDriveUploader使用
date: 2020-04-11
tags: ["onedrive"]
author: "yanSl"
draft: false
weight: 3
---

#### 将同目录下的 mm00.jpg 文件上传到 OneDrive 网盘根目录

```shell
OneDriveUploader -s "mm00.jpg"
```

#### 将同目录下的 mm00.jpg 文件上传到 OneDrive 网盘根目录,并改名为 mm01.jpg

```shell
OneDriveUploader -s "mm00.jpg" -n "mm01.jpg"
```

#### 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录

```shell
OneDriveUploader -s "Download" 
```

#### 将同目录下的 Download 文件夹上传到 OneDrive 网盘Test目录中

```shell
OneDriveUploader -s "Download" -r "Test"
```

#### 将同目录下的 Download 文件夹上传到 OneDrive 网盘Test目录中, 使用 10 线程

```shell
OneDriveUploader -t 10 -s "Download" -r "Test"
```

#### 将同目录下的 Download 文件夹上传到 OneDrive 网盘Test目录中, 使用 15 线程, 并设置分块大小为 20M

```shell
OneDriveUploader -t 15 -b 20 -s "Download" -r "Test"
```