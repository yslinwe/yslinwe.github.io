---
title: "剑指office（一）二维数组查找"
summary: 剑指office（一）二维数组查找
date: 2019-08-21
tags: ["剑指office"]
author: "yanSl"
draft: false
weight: 2
---

### 题目描述

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

#### 方法1

```c++
	//时间过长不能通过。

	bool Find(int target, vector<vector<int> > array) {
		int col = 0, row = 0;
		row = array.size();
		col = array[0].size();
		int up = 0, down = row - 1;
		int right = col - 1, left = 0;
		while (left < col-1&&right > 0&&down+1 > 0&&up < row-1)
		{
			int left_temp = left;
			int rl_mid = (right + left) / 2;
			cout << "rl_mid=" << rl_mid <<" "<<"right="<<right<<" "<<"left="<< left<< endl;
			int rl_val = array[up][rl_mid];
			if (target == rl_val)
				return true;
			else if (target < rl_val)
				right = rl_mid - 1;
			else left = rl_mid + 1;

			int ud_mid = (up + down) / 2;
			cout << "ud_mid=" << ud_mid <<" "<< "up="<<up<<" "<<"down="<<down <<endl;
			int ud_val = array[ud_mid][left_temp];
			if (target == ud_val)
				return true;
			else if (target < ud_val)
				down = ud_mid - 1;
			else up = ud_mid + 1;
		}
		return false;
	}
```

#### 方法2

```c++
	bool Find2(int target, vector<vector<int> > array) {
		int rows = array.size();
		int cols = array[0].size();
		if (!array.empty() && rows > 0 && cols > 0) {
			int row = 0;
			int col = cols - 1;
			while (row < rows && col >= 0) {
				if (array[row][col] == target) {
					return true;
				}
				else if (array[row][col] > target) {
					--col;
				}
				else {
					++row;
				}
			}
		}
		return false;
	}
```
#### 方法3

```c++
	bool Find3(int target, vector<vector<int> > array)
	{
		int rows = array.size();
		int cols = array[0].size();
		int row = 0;
		int col = cols - 1;
			while(!array.empty() && col > 0 && row < rows)
			{
				if (array[row][col] == target)
					return true;
				else if (array[row][col] < target)
					row++;
				else col--;
			}
			return false;
	}
```