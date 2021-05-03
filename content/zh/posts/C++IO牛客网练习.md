---
title: "C++IO牛客网"
summary: C++IO牛客网
date: 2021-04-16
tags: ["牛客网"]
author: "YSL"
draft: false
weight: 3
image: https://cdn.pixabay.com/photo/2020/04/28/12/40/tulips-5104311__340.jpg
---
#### 牛客网IO练习
<https://ac.nowcoder.com/acm/contest/5657#question>
## 计算a+b (1)
### 题目描述 

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question
#### 输入描述:
>输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。
#### 输出描述:
>输出a+b的结果
#### 示例1
#### 输入

>1 5
></br>10 20
#### 输出

>6
></br>30
```C++
#include<iostream>
using namespace std;

int main(){
    int a, b;
    while(cin>>a>>b)
        cout<<a+b<<endl;
    return 0;
}
```
## 计算a+b (2)
#### 题目描述 
计算a+b
打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question

#### 输入描述:
>输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)
#### 输出描述:
>输出a+b的结果
#### 示例1
#### 输入

>2</br>
1 5</br>
10 20</br>
#### 输出

>6</br>
30
```C++
#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int a, b;
        while(cin>>a>>b)
            cout<<a+b<<endl;
    }

    return 0;
}
```
## 计算a+b (3)
### 题目描述 
计算a+b
打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question

#### 输入描述:
>输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
#### 输出描述:
>输出a+b的结果
#### 示例1
#### 输入
>1 5</br>
10 20</br>
0 0</br>
#### 输出
>6</br>
30</br>
```C++
#include<iostream>
using namespace std;

int main(){
    int a, b;
    while(cin>>a>>b){
        if(a==0&&b==0)
            break;
        cout<<a+b<<endl;
    }
        

    return 0;
}
```
## 计算a+b (4)
### 题目描述 
计算一系列数的和
</br>打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question

#### 输入描述:
>输入数据包括多组。
</br>每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
</br>接下来n个正整数,即需要求和的每个正整数。
#### 输出描述:
>每组数据输出求和的结果

#### 示例1
#### 输入
>4 1 2 3 4
</br>5 1 2 3 4 5
</br>0

#### 输出
>10
</br>15
```C++
#include<iostream>
using namespace std;

int main(){
    int n;
    while(cin>>n){
        if(n==0)
            break;
        int sum = 0,temp;
        while(n--){
            cin>>temp;
            sum += temp;
        }
        cout<<sum<<endl;

    }
    return 0;
}
```
## 计算a+b (5)
### 题目描述 
计算一系列数的和

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question


#### 输入描述:

>输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
</br>接下来t行, 每行一组数据。
</br>每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。
#### 输出描述:
每组数据输出求和的结果

#### 示例1
#### 输入
>2
</br>4 1 2 3 4
</br>5 1 2 3 4 5
#### 输出
>10
</br>15
```C++
#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int sum = 0,temp;
        while(n--){
            cin>>temp;
            sum += temp;
        }
        cout<<sum<<endl;
    }
    return 0;
}
```
## 计算a+b (6)
### 题目描述 
计算一系列数的和

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question


#### 输入描述:
>输入数据有多组, 每行表示一组输入数据。
</br>每行的第一个整数为整数的个数n(1 <= n <= 100)。
</br>接下来n个正整数, 即需要求和的每个正整数。
#### 输出描述:
>每组数据输出求和的结果
#### 示例1
#### 输入

>4 1 2 3 4
</br>5 1 2 3 4 5
#### 输出

>10
</br>15
```C++
#include<iostream>
using namespace std;

int main(){
    int t;
    while(cin>>t){
        int sum = 0;
        while(t--){
            int temp;
            cin>>temp;
            sum += temp;
        }
        cout<<sum<<endl;
    }
    return 0;
}
```
## 计算a+b (7)

### 题目描述 
计算一系列数的和

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question


#### 输入描述:
>输入数据有多组, 每行表示一组输入数据。
</br>每行不定有n个整数，空格隔开。(1 <= n <= 100)。
#### 输出描述:
>每组数据输出求和的结果
#### 示例1
#### 输入

>1 2 3
</br>4 5
</br>0 0 0 0 0
#### 输出
>6
</br>9
</br>0
```C++
#include<iostream>
using namespace std;

int main(){
    int temp,sum = 0;
    while(cin>>temp){
        sum += temp;
        if(cin.get()=='\n'){
            cout<<sum<<endl;
            sum = 0;
        }
        
    }
    return 0;
}
```
## 字符串排序（1）
### 题目描述 
对输入的字符串进行排序后输出

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question

#### 输入描述:
>输入有两行，第一行n
</br>第二行是n个空格隔开的字符串
#### 输出描述:
>输出一行排序后的字符串，空格隔开，无结尾空格
#### 示例1
#### 输入
>5
</br>c d a bb e
#### 输出
>a bb c d e
```C++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n;
	string *pstr;
	vector<string> que;
	cin >> n;
	pstr = new string[n];
	for (int i = 0; i < n; i++)
	{
		cin >> pstr[i];
		que.push_back(pstr[i]);
	}
	sort(que.begin(), que.end());
	for (int i = 0; i < n; i++)
	{
		cout << que[i] << " ";
	}
}
```
## 字符串排序 （2）
### 题目描述 
对输入的字符串进行排序后输出

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question


#### 输入描述:
>多个测试用例，每个测试用例一行。
</br>每行通过空格隔开，有n个字符，n＜100
#### 输出描述:
>对于每组测试用例，输出一行排序过的字符串，每个字符串通过空格隔开
#### 示例1
#### 输入
>a c bb
</br>f dddd
<br>nowcoder
#### 输出
>a bb c
</br>dddd f
</br>nowcoder
```C++
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    string str;
    vector<string> s;
    while(cin>>str)
    {
        s.push_back(str);
        if(cin.get()=='\n')
        {
            sort(s.begin(),  s.end());
            int n = s.size();
            for(int i = 0;i<n;i++)
            {
                cout<<s[i]<<" ";
            }
            s.clear();
            cout<<endl;
        }
    }
}
```
## 字符串排序 （3）


### 题目描述 
对输入的字符串进行排序后输出

打开以下链接可以查看正确的代码
>https://ac.nowcoder.com/acm/contest/5657#question


#### 输入描述:
>多个测试用例，每个测试用例一行。
</br>每行通过,隔开，有n个字符，n＜100
#### 输出描述:
>对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格
#### 示例1
#### 输入

>a,c,bb
</br>f,dddd
</br>nowcoder
##### 输出

>a,bb,c
</br>dddd,f
</br>nowcoder
```C++
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>

using namespace std;
int main()
{
    string line;
    string str;
    vector<string> s;
    while(cin>>line)
    {
        stringstream ss(line);
        while(getline(ss, str, ','))
        {
            s.push_back(str);
        }

        sort(s.begin(),s.end());
        if(s.size()==1)
            cout<<s[0];
        else
        for(int i = 0;i<s.size();i++)
        {
            if(i!=s.size()-1)
                cout<<s[i]<<',';
            else
                cout<<s[i];
        }
        s.clear();
        cout<<endl;
        
    }
}
```