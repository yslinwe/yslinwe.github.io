---
title: "Github Action 同步gitee和github单个仓库"
summary: Github Action 同步gitee和github单个仓库
date: 2021-04-23
tags: ["Github Action","github"]
author: "YSL"
draft: false
weight: 3
---

### 入参

|       参数       |             描述              | 是否必传 |  默认值  |
| :--------------: | :---------------------------: | :------: | :------: |
| `gitee-username` |         `Gitee`用户名         |    是    |    -     |
| `gitee-password` |          `Gitee`密码          |    是    |    -     |
|   `gitee-repo`   | `Gitee`仓库（严格区分大小写） |    是    |    -     |
|     `branch`     |         要部署的分支          |    否    | `master` |
|   `directory`    |     要部署的分支上的目录      |    否    |    ''    |
|     `https`      |      是否强制使用`https`      |    否    |  `true`  |

### 示例

在`GitHub`的仓库创建 `.github/workflows/` 文件夹并且创建一个**`sync.yml`** 文件

```yaml
name: Sync
 
 
on:
  push:
    branches: [ giteePage ]
 
 
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Sync to Gitee
      uses: wearerequired/git-mirror-action@master
      env:
          # 注意在 Settings->Secrets 配置 PRIVATE 
          SSH_PRIVATE_KEY: ${{ secrets.PRIVATE }}
      with:
          # 注意替换为你的 GitHub 源仓库地址
          source-repo: "git@github.com:username/username.github.io.git"
          # 注意替换为你的 Gitee 目标仓库地址
          destination-repo: "git@gitee.com:username/username.git"
 
 
    - name: Build Gitee Pages
      uses: yanglbme/gitee-pages-action@master
      with:
          # 注意替换为你的 Gitee 用户名
          gitee-username: username
          # 注意在 Settings->Secrets 配置 PASSWORD
          gitee-password: ${{ secrets.PASSWORD }}
          # 注意替换为你的 Gitee 仓库
          gitee-repo: username/username
          # 提交到gitee的github仓库的分支
          branch: giteePage
```

先使用 `wearerequired/git-mirror-action` 将 `GitHub` 仓库同步到 `Gitee` 仓库，再使用 `yanglbme/gitee-pages-action` 实现 `Gitee Pages` 的自动部署。

运行需要在 `GitHub` 项目的 Settings -> Secrets 路径下配置好 **PRIVATE **以及 **PASSWORD** 两个密钥。其中：

> **PRIVATE **: 存放你的 `id_rsa` 私钥。**PASSWORD**: 存放你的 `Gitee` 账户密码。

### 1. 配置**PRIVATE**

* 生成SSH密钥

  ```shell
  ssh-keygen -t rsa -C "name"
  ```

  "name"是任意指定的标识

  * 获取公钥

  ```shell
  cat ~/.ssh/id_rsa.pub
  ```

  * 绑定`Gitee`

* 复制公钥，通过仓库主页个人图像下拉设置->SSH公钥添加公钥

  * 测试

    打开终端输入：

    ```shell
    ssh -T git@gitee.com
    ```

    显示如下图则成功

    ![image-20210430222406658](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/image-20210430222406658.png)

* 绑定`Github`

  复制公钥，通过仓库主页个人图像下拉Setting->SSH and GPG keys添加公钥

  * 测试

    打开终端输入：

    ```shell
    ssh -T git@github.com
    ```

    显示如下图则成功

    ![image-20210430222851660](https://cdn.jsdelivr.net/gh/yslinwe/image_bed@main/img/image-20210430222851660.png)

* 配置

  * 获取私钥

    ```bash
    cat ~/.ssh/id_rsa
    ```

    >  复制私钥，在仓库的Setting->Secrets路径下命名PRIVATE，**Value**添加私钥（记得复制全部内容）

### 2. 配置**PASSWORD**

> 在仓库的Setting->Secrets路径下命名**PASSWORD**，**Value**添加**`Gitee`**账户密码。

如果一切配置正常，并成功触发 `Gitee Pages Action` ，我们可能会收到一封来自 `Gitee` 的告警邮件/站内信。放心，这是 `GitHub Action` 程序帮我们登录到 `Gitee` 官网，并为我们点击了项目的部署按钮。

### FAQ
#### 问题 1：遇到短信验证码导致无法自动部署，怎么解决？

因为 `Gitee Pages Action` 使用的是 `GitHub` 自家的服务器（美国），在这种情况下，当 Action 自动	帮我们登录 `Gitee` 的时候，会触发 `Gitee` 帐号异常登录告警，提示用户在非正常的 `IP` 地址登陆	`Gitee`，需要输入验证码。



**解决方案**是：关注「**码云 Gitee**」 微信公众号，绑定个人微信到码云帐号。这样 Action 在登录的过程中，`Gitee` 就不会下发短信验证码，而是通过「**码云 Gitee**」公众号给我们发送一个登录通知，Action 就能成功登录了。

####  问题 2：报 deploy error occurred, message: 'NoneType' object has no attribute 'group' 错误，怎么办？

报了这个错误，说明 `Action` 已经成功帮我们登录 `Gitee` 帐号了，但在访问 `Gitee Repo` 的过程中出现问题。

这种情况，一般是 `Gitee Pages Action` 的参数配置错误导致，请仔细检查你的配置信息。

> 注意：`gitee-repo` 参数严格区分大小写，请准确填写，比如 `doocs/advanced-java`，当你写成 `doocs/Advanced-java` 的时候，是访问不到的，不信你可以试试访问：https://gitee.com/Doocs/Advanced-java