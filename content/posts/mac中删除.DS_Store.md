title: "Mac中删除.DS_Store"
summary: Mac中删除.DS_Store
date: 2021-04-25
tags: ["Mac"]
author: "yanSl"
draft: false
weight: 3

---

### 删除 .DS_Store

如果你的项目中还没有自动生成的 .DS_Store 文件，那么直接将 .DS_Store 加入到 .gitignore 文件就可以了。如果你的项目中已经存在 .DS_Store 文件，那就需要先从项目中将其删除，再将它加入到 .gitignore。如下：

#### 删除项目中的所有.DS_Store。这会跳过不在项目中的 .DS_Store

1. find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch

    将 .DS_Store 加入到 .gitignore

2. echo .DS_Store >> ~/.gitignore

#### 更新项目

3. git add --all

4. git commit -m '.DS_Store banished!'

如果你只需要删除磁盘上的 .DS_Store，可以使用下面的命令来删除当前目录及其子目录下的所有.DS_Store 文件:
```shell
find . -name '*.DS_Store' -type f -delete
```
禁用或启用自动生成

禁止.DS_store生成：
```shell
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```
恢复.DS_store生成：恢复.DS_store生成：
```shell
defaults delete com.apple.desktopservices DSDontWriteNetworkStores
```