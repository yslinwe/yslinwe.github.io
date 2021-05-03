---
title: "Mac启动台App问号"
summary: Mac启动台App问号
date: 2021-02-21
tags: ["Mac"]
author: "YSL"
draft: false
weight: 3
image: https://cdn.pixabay.com/photo/2021/04/20/08/14/fiber-6193207__340.jpg
---
##### Mac启动台App问号
```shell
defaults write com.apple.dock ResetLaunchPad -bool TRUE
killall Dock
```