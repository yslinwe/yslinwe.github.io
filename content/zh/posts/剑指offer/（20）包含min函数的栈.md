---
title: "剑指office（二十）包含min函数的栈"
date: 2020-04-29
description: "剑指office（二十）包含min函数的栈"
draft: false
hideToc: false
enableToc: true
enableTocContent: false
author: YSL
authorEmoji: 🎅
pinned: false
tags:
- 剑指office
series:
- 剑指office
categories:
- 剑指office
weight: 3

type: "notshow"
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