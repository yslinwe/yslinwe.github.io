---
title: "input自动填充时背景色改变问题"
summary: input自动填充时背景色改变问题
date: 2022-03-16
tags: ["input","css"]
author: "YSL"
draft: false
weight: 2
---
### input 输入框 在自动填充时，背景颜色问题]

##### 问题:

自动填充前：

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094406899-4910542.png)

 自动填充后：

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094923153-337234637.png)

可以看出，自动填充后，input背景颜色变成了白色,

##### 解决办法：

1. ###### 纯色阴影覆盖底色

 ```css
      input:-webkit-autofill {
          box-shadow: 0 0 0 1000px #333333 inset;
          -webkit-text-fill-color: #fff;
      }
 ```

再看看，自动填充后的效果:

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094531265-808374865.png)

 注意： 这个方法有个问题，就是input 输入框，不能有 圆角(border-radius)，而且只适用于纯色背景框。

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094549963-671205407.png)

 可以看到，两边有明显的白色

2. ###### 设置透明：

```css
input:-internal-autofill-previewed,
input:-internal-autofill-selected {
    -webkit-text-fill-color: #807c7c;
    transition: background-color 5000s ease-out 0.5s;
}
```

效果：

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094656178-925469677.png)

3. ###### 利用动画延迟

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```css
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus, 
input:-webkit-autofill:active {
    transition-delay: 99999s;
    transition: color 99999s ease-out, background-color 99999s ease-out;
    -webkit-transition-delay: 99999s;
    -webkit-transition: color 99999s ease-out, background-color 99999s ease-out;
    -webkit-text-fill-color: #807c7c;
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

效果：

![img](https://img2020.cnblogs.com/blog/1251386/202005/1251386-20200527094804112-58612907.png)