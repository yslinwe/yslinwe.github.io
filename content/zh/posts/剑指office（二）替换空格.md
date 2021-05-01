---
title: "剑指office（二）替换空格"
summary: 剑指office（二）替换空格
date: 2020-04-10
tags: ["剑指office"]
author: "yanSl"
draft: false
weight: 3
---

### 题目描述

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy

#### 方法1

```c++
    //需要头文件：
	#include<iostream>
	#include<stdlib.h>
	#include<string>

	void replaceSpace(char* str, int length) {
		int count = 0;
		for (int i = 0; i < length; i++)
		{
			if (str[i] == ' ')
				count++;
		}
		int new_length = length + 2 * count;
		int j = length-1;
		for (int i = new_length-1; i >= 0;)
		{
			if (str[j] == ' ')
			{
				str[i--] = '0';
				str[i--] = '2';
				str[i--] = '%';
			}
			else
			{
				str[i--] = str[j];
			}
			j--;
		}
	}
```

#### 方法2

```c++
	void replaceSpace2(char* str, int length) {
		int i = 0;
		int numSpace = 0;
		while (str[i] != '\0')
		{
			if (str[i] == ' ')
				numSpace++;
			++i;
		}
		int newLen = i + numSpace * 2;
		if (newLen > length)
			return;
		for (int j = i; j >= 0, newLen >= 0;)
		{
			if (str[j] == ' ')
			{
				str[newLen--] = '0';
				str[newLen--] = '2';
				str[newLen--] = '%';
			}
			else
				str[newLen--] = str[j];
			j--;
		}
	}
```

#### 方法3

```c++
	#pragma warning(disable:4996)
	void replaceSpace3(char* str, int length)
	{
		string s = str;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == ' ') {
				s.replace(i, 2, "%20");
			}
		}
		str = new char[s.size()];
		strcpy(str,s.c_str());
		cout << str;
	}
```