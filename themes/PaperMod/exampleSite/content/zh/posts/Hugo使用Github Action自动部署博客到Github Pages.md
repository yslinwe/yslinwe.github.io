---
title: "Hugo使用Github Action自动部署博客到Github Pages"
summary: Hugo使用Github Action自动部署博客到Github Pages
date: 2021-04-20
tags: ["Github Action","Hugo"]
author: "yanSl"
draft: false
weight: 3
---
### 创建repo

    repo名称为<username>.github.io

### 设置github actions自动部署
将博客源码放到一个private repo 或者 public repo 中，
</br>创建一个blogSite分支。
</br>blogSite分支，用于存放博客源码
</br>master分支，用于存放博客网页代码

需要获取一个personal_token或者deploy_key来获取repo的权限，这里选择personal_token的方式，这种方式更简单，后者可以自行了解。

### 生成一个**personal_token**

点击GitHub头像在下拉栏里进入**Setting-Developer** **->**  **Setting-Personal access**
选择 **Generate new token**

![1.png](https://img.imgdb.cn/item/607ee8038322e6675c0e837a.png)

在上方填入名字**ACTION_ACCESS_TOKEN**，并勾选repo里的所有选项，还有**admin:repo_hook**

![2.png](https://img.imgdb.cn/item/607ee8038322e6675c0e837e.png)

![3.png](https://img.imgdb.cn/item/607ee8038322e6675c0e8385.png)

点击 **Generate token** 生成 **token**，
<br>并先复制保存该**token**（记得保存后面要用到）

然后执行以下几步：

    1.在源码repo里新建一个blogSite分支：git checkout -b blogSite

    2.在repo根目录新建嵌套的两个文件夹.github/workflows

    3.在workflows里新建一个后缀为.yml的配置文件，名字自取。

    4.写进去以下配置（从hugo官方文档修改而来）：

```yaml
name: github pages # 名字自取

on:
  push:
    branches:
      - blogSite  # 这个是博客源码分支

jobs:
  deploy: # 任务名自取
    runs-on: ubuntu-18.04	# 在什么环境运行任务
    steps:
      - uses: actions/checkout@v2	# 引用actions/checkout这个action，与所在的github仓库同名
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive) 获取submodule主题
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo	# 步骤名自取
        uses: peaceiris/actions-hugo@v2	# hugo官方提供的action，用于在任务环境中获取hugo
        with:
          hugo-version: 'latest'	# 获取最新版本的hugo
          # extended: true

      - name: Build
        run: hugo --minify	# 使用hugo构建静态网页

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3	# 一个自动发布github pages的action
        with:
          # github_token: ${{ secrets.GITHUB_TOKEN }} 该项适用于发布到源码相同repo的情况，不能用于发布到其他repo
          external_repository: username/username.github.io	# username 是你的仓库repo的名称，也是你的用户名
          personal_token: ${{ secrets.ACTION_ACCESS_TOKEN }}	# 发布到其他repo需要提供上面生成的personal access token
          publish_dir: ./public	# 注意这里指的是要发布哪个文件夹的内容，而不是指发布到目的仓库的什么位置，因为hugo默认生成静态网页到public文件夹，所以这里发布public文件夹里的内容
          publish_branch: master	# 发布到哪个branch
```
* 记得修改 external_repository中的<font color=red>username</font>

#### 接下来在源码repo中添加上面的personal access token：

进入repo的Settings-Secrets一栏，选择New repository secret

![5.png](https://img.imgdb.cn/item/607ee8038322e6675c0e838e.png)

在下面填入刚才生成的token，名字注意需要与上面yml文件里XXX相同
personal_token: ${{ secrets.XXX }} 
</br>这里的名称是ACTION_ACCESS_TOKEN

![6.png](https://img.imgdb.cn/item/607ee8038322e6675c0e8393.png)

添加token之后，进入github actions里点击刚才失败的任务，点击右上角Re-run jobs
</br>这时应该能够成功运行该任务，这说明自动部署已经开始在工作了，以后往blogSite分支push新文章时github actions会自动生成静态博客并发布到master中。
