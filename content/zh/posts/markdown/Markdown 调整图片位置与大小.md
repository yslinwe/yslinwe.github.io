---
title: "Markdown 调整图片位置与大小"
summary: Markdown 调整图片位置与大小
date: 2021-04-23
tags: ["Markdown"]
author: "YSL"
draft: false
weight: 3
image: https://cdn.pixabay.com/photo/2015/02/06/21/27/pyrite-626549__340.jpg
---
### 插入图片

使用 Markdown 编写文档或博客时，经常需要对图片的位置与尺寸进行调整。

插入图片后，Markdown 表示图片的语法格式如下：

```
![图片描述](图片链接)
```

### 调整图片位置

#### 居左

（1）方法一：添加位置标识。

```javascript
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822014538211.png#pic_left)
```

（2）方法二：嵌入 HTML 代码。

```javascript
<div align="left">
<img src=https://img-blog.csdnimg.cn/20200822014538211.png />
</div>
```

#### 居中

（1）方法一：添加位置标识。

```javascript
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822014538211.png#pic_center)
```

（2）方法二：嵌入 HTML 代码。

```javascript
<div align="center">
<img src=https://img-blog.csdnimg.cn/20200822014538211.png />
</div>
```

#### 居右

（1）方法一：添加位置标识。

```javascript
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822014538211.png#pic_right)
```

（2）方法二：嵌入 HTML 代码。

```javascript
<div align="right">
<img src=https://img-blog.csdnimg.cn/20200822014538211.png />
</div>
```

### 调整图片大小

#### 等比缩放

#### 相对于父级窗口

使用百分比只定义宽即可等比例缩放。注意：宽度相对于图片所在父级窗口。

```javascript
<img src=https://img-blog.csdnimg.cn/20200822014538211.png width=60% />
```

#### 相对于自身

#### 非等比缩放

将图片的宽高缩小或放大为原来的指定百分比。

#### 固定宽高

```javascript
<img src=https://img-blog.csdnimg.cn/20200822014538211.png width=200 height=100 />
```

