---
title: "剑指office（二十）包含min函数的栈"
date: 2020-04-29
description: "剑指office（二十）包含min函数的栈"
draft: false
hideToc: false
enableToc: true
enableTocContent: true
author: YSL
authorEmoji: 🎅
pinned: true
tags:
- 剑指office
series:
- 剑指office
categories:
- 剑指office
weight: 3
image: https://cdn.pixabay.com/photo/2021/04/12/02/40/love-6171182__340.png


---

### 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

```c++
class Solution {
public:
    stack<int> v;
    stack<int> minV;
    void push(int value) {
        v.push(value);
        if(minV.empty())
            minV.push(value);
        if(minV.top()>value)
        {
           minV.push(value);
        }
    }
    void pop() {
        if(v.top()==minV.top())
            minV.pop();
        v.pop();
    }
    int top() {
        return v.top();
    }
    int min() {
        return minV.top();
    }
};
```