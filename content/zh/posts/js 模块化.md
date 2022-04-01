---
title: "js 模块化"
summary: js 模块化
date: 2022-04-01
tags: ["js"]
author: "YSL"
draft: false
weight: 2
---

为什么有模块概念？
理想情况下，开发者只需要实现核心的业务逻辑，其他都可以加载别人已经写好的模块。

但是，Javascript不是一种模块化编程语言，在es6以前，它是不支持”类”（class），所以也没有”模块”（module）。

在js里，何为“模块”？
在js里面，我们可以把模块定义为实现特定功能的一组方法，只要把实现某一功能的函数放一起，就可以看成是一个“模块”。

1. ##### 模块的基础写法
```js
//  例如：
//  这是一个弹窗功能的一组方法
 
//  创建弹窗
function fn1(){
    // do  something
}
 
// 打开弹窗
function fn2(){
    // do  something
}
 
// 关闭弹窗
function fn3(){
    // do  something
}
```
这种做法的缺点很明显：”污染”了全局变量，无法保证不与其他模块发生变量名冲突，而且模块成员之间看不出直接关系。

2. ##### 对象写法

为了解决上面这种基础写法的缺陷，我们可以把它写成一个对象，模块成员被包含在内。

 ```js
let moduleAlert =  {
       id: 1,
       fn1: function {
           // do  something
       },
       fn2: function {
           // do  something
       },
       fn3: function {
           // do  something
       }
}
 ```
调用：
```js
moduleAlert.fn1();
moduleAlert.fn2();
moduleAlert.fn3();
```
封装了一层，更加清晰，调用的时候一目了然。

3. ##### 模块模式

编程语言中，比如 Java，是支持将方法声明为私有的，即它们只能被同一个类中的其它方法所调用。
而 JavaScript 没有这种原生支持，但我们可以使用闭包来模拟私有方法。
私有方法不仅仅有利于限制对代码的访问：还提供了管理全局命名空间的强大能力，避免非核心的方法弄乱了代码的公共接口部分。
下面的示例展现了如何使用闭包来定义公共函数，并令其可以访问私有函数和变量。这个方式也称为 模块模式（module pattern）：

```js
 var Counter = (function() {
     var privateCounter = 0;
      function changeBy(val) {
          privateCounter += val;
      }
      return {
          increment: function() {
              changeBy(1);
          },
          decrement: function() {
              changeBy(-1);
          },
          value: function() {
              return privateCounter;
          }
      }   
  })();
 
  console.log(Counter.value()); /* logs 0 */
  Counter.increment();
  Counter.increment();
  console.log(Counter.value()); /* logs 2 */
  Counter.decrement();
  console.log(Counter.value()); /* logs 1 */
```


* 该共享环境创建于一个立即执行的匿名函数体内。这个环境中包含两个私有项：名为 . privateCounter 的变量和名为 changeBy 的函数。
* 这两项都无法在这个匿名函数外部直接访问。必须通过匿名函数返回的三个公共函数访问。
* 这三个公共函数是共享同一个环境的闭包。多亏 JavaScript 的词法作用域，它们都可以访问 privateCounter 变量和 changeBy 函数。
————————————————
版权声明：本文为CSDN博主「欧阳呀」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_35942348/article/details/110475765