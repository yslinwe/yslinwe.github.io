---
title: "Mac终端美化"
summary: Mac终端美化
date: 2021-04-17
tags: ["Mac"]
author: "yanSl"
draft: false
weight: 3
---
#### Part1 安装oh-my-zsh
* 第一步 clone oh-my-zsh项目
```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```
* 第二步 复制 .zshrc
```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```
* 第三步 更改你的默认 Shell
```shell
chsh -s /bin/zsh
```
---
修改后终端变为这样<br>ps:这里选择了steeef主题，不是默认的robbyrussell主题
### 终端的命令提示符
<img src="https://img.imgdb.cn/item/607a4f2c8322e6675cd6199d.png" width="50%" div align=center />

#### Part2 主题配置
1. 修改.zshrc
```
cd ~
vim ~/.zshrc
```
* 更改主题
![主题](https://img.imgdb.cn/item/607a4f2c8322e6675cd619a2.png)

将 **ZSH_THEME="robbyrussell"** 改成 **ZSH_THEME="steeef"**
* 应用到.zshrc
```
source ~/.zshrc
```
P.S. 这些主题都保存在 "~/.oh-my-zsh/themes" 目录中

2. 插件
oh-my-zsh 的自带插件都储存在 "~/.oh-my-zsh/plugins" 目录中,
</br>在 **~/.zshrc** 中的 **plugins** 加入插件名称，这样设置就完成了。
![插件](https://img.imgdb.cn/item/607a4f2c8322e6675cd61999.png)

* 安装 zsh-syntax-highlighting
> 对于oh-my-zsh
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
在 **~/.zshrc** 中加入插件的名字
plugins=(zsh-syntax-highlighting) 
，最后source生效
```
source ~/.zshrc
```
> 对于osx
可以直接
```
brew install zsh-syntax-highlighting
```
并且source生效
```
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```