'''
### 脚本用法：

这是一个 python 脚本，下载安装 python 后，双击脚本就可以运行。

### 脚本用途：

首先用文本编辑器编辑脚本，
在下面设定一个日记本根目录，
然后运行这个脚本，
脚本根据当前的日期，在日记本根目录下创建对应的年文件夹、月文件夹，
然后新建一个今天日期的 md 文件，并且打开它。

比如你的笔记本根目录是 `D:/Diary` ，今天是 2020 年 11 月 5 日，那么在运行此脚本后，
会自动创建上 `D:/Diary/2020/11/05.md` 文件，并且会打开它，
如果你电脑装的有 Typora 等 Markdown 编辑器，就会用默认的 md 编辑器打开，
这就是今天的日记，每天只有这一个日期命名的文件，每日一记。

另外，在打开今天的日记之前，还会清理日记文件夹下所有的空白文件，
例如你昨天运行了脚本，打开了 04.md，但是什么都没写，就关闭了，
那这个文件就是空的，没有意义，只会占地方，清理掉更清爽。

'''



import os
import datetime
import time
import platform
import subprocess

日记根目录 = '/Users/popo/Documents/Github/yslinwe.github.io/content/zh/posts'


def clearFileDir(path):
    '''
    输入一个文件路径
    找到这个路径下所有的文件
    如果发现有空文件
    就把这些空文件删除
    并以列表形式返回删除的文件
    '''
    deleted = []
    if not os.path.exists(os.path.dirname(path)):
        return deleted # 如果这个文件的文件夹路径都不存在，就直接返回
    
    for file in os.listdir(os.path.dirname(path)):
        file = os.path.dirname(path) + '/' + file
        if os.path.getsize(file) == 0:  # 如果文件大小为 0 
            try:
                os.remove(file)         # 删掉文件
                deleted.append(file)    # 列表加上已删除的这个文件
                print(f'删除空白内容文件：{file}')
            except:
                print(f'有文件删除失败：{file}')
    return deleted  # 以列表形式返回删除的文件


def openFile(currentTime,path):
    '''
    输入一个文件路径
    如果路径不存在，那就先创建它
    然后用系统默认方式打开这个文件
    '''
    sysPlatfm = platform.system() # 先获得系统信息
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except:
            print(f'创建文件夹失败：{os.path.dirname(path)}')
            return False
    if not os.path.exists(path):
        try:
            with open(path,'w',encoding='utf-8')as file:
                file.write(
f'''---
title: ""
summary: 
date: {str(time.strftime("%Y-%m-%d",time.localtime()))}
tags: [""]
author: "YSL"
draft: false
weight: 2
---'''
                )
        except:
            print(f'创建 md 文件失败：{path}')
            return False
    try: # 如何打开文件还是要分系统的
        if sysPlatfm == 'Darwin': # 如果是 MacOS 系统
            import shlex
            os.system("open " + shlex.quote(path))
        elif sysPlatfm == 'Windows': # 如果是 Windows 系统
            os.startfile(os.path.realpath(path))
        elif sysPlatfm == 'Linux':
            subprocess.call(["xdg-open",path])
    except:
        print('未能打开文件')


# 得到当前时间，格式是这样的：
# time.struct_time(tm_year=2020, tm_mon=10, tm_mday=6, tm_hour=18, tm_min=41, tm_sec=53, tm_wday=1, tm_yday=280, tm_isdst=0)
currentTime = time.localtime(time.time())

# 得到当前日期下的日记路径
# 类似这样的：D:/Users/Haujet/Documents//Diary/2020/10/06.md
pathToTodayDiary = 日记根目录.replace('\\', '/').rstrip('/') + '/' + str(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())) + '.md'

# str(currentTime.tm_year) + '/' + '{:0>2d}'.format(currentTime.tm_mon) + '/' + '{:0>2d}'.format(currentTime.tm_mday)


# 清除日记目录下的空白文件，日记目录不需要存在空白的 md 文件
# clearFileDir(pathToTodayDiary)

# 打开今天的日记
openFile(currentTime,pathToTodayDiary)
