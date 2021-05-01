---
title: "Mac启动台App问号"
summary: Mac启动台App问号
date: 2021-02-21
tags: ["Mac"]
author: "YSL"
draft: false
weight: 3
---
##### Mac启动台App问号
```shell
defaults write com.apple.dock ResetLaunchPad -bool TRUE
killall Dock
```