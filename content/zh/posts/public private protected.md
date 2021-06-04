---
title: "public，private，protected的区别，继承方法与访问权限"
summary: public，private，protected的区别，继承方法与访问权限
date: 2021-06-04
tags: [""public，private，protected"]
author: "YSL"
draft: false
weight: 2
---
第一部分：

public/private/protected的具体区别

在说明这四个关键字之前，就class之间的关系做一个简单的定义，对于继承自己的class，base class可以认为他们都是自己的子女，而对于和自己一个目录下的classes，认为都是自己的朋友。
1、public：public表明该数据成员、成员函数是对所有用户开放的，所有用户都可以直接进行调用
2、private：private表示私有，私有的意思就是除了class自己之外，任何人都不可以直接使用，私有财产神圣不可侵犯嘛，即便是子女，朋友，都不可以使用。
3、protected：protected对于子女、朋友来说，就是public的，可以自由使用，没有任何限制，而对于其他的外部class，protected就变成private。

![20161223101955854](https://gitee.com/yslinxx/image-bed/raw/master/images/20161223101955854.jpg)

第二部分：


派生类可以访问基类中所有的非私有成员。因此基类成员如果不想被派生类的成员函数访问，则应在基类中声明为 private。

我们可以根据访问权限总结出不同的访问类型，如下所示：

![20161223101949482](https://gitee.com/yslinxx/image-bed/raw/master/images/20161223101949482.jpg)

一个派生类继承了所有基类的方法，但下列情况除外：
*基类的构造函数、析构函数和拷贝构造函数（可能是为了多继承定义不出现冲突）
*除了赋值运算符重载函数以外，所有的运算符重载函数都可以被派生类继承。 （原因：“赋
值运算符重载函数”不是不能被派生类继承，而是被派生类的默认“赋值运算符重载函数”给
覆盖了。这就是 C++赋值运算符重载函数不能被派生类继承的真实原因！ ） ，更详细的解释传
送门：http://blog.csdn.net/wuyuan2011woaini/article/details/9407933，感谢这位网友。
*基类的友元函数（父亲的朋友不一定是你的朋友）
————————————————
版权声明：本文为CSDN博主「spu20134823091」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/spu20134823091/article/details/53836192