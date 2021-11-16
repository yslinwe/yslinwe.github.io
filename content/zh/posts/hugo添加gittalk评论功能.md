---
title: "hugo添加gittalk组件"
summary: hugo添加gittalk组件
date: 2021-11-16
tags: ["hugo、gittalk"]
author: "YSL"
draft: false
weight: 2
---
### 申请GitHub Oauth App

需要 **GitHub Application**，如果没有 [点击这里申请](https://github.com/settings/applications/new)，`Authorization callback URL` 填写当前使用插件页面的域名。

以本站为例，须填写以下内容：

| 字段                       | 内容                              | 备注         |
| -------------------------- | --------------------------------- | ------------ |
| Application name           | gittalk for xbc.me                | 填写应用名称 |
| Homepage URL               | [https://xbc.me](https://xbc.me/) | 主页地址     |
| Application description    | 神秘极客gtalk留言插件             | 备注         |
| Authorization callback URL | [https://xbc.me](https://xbc.me/) | 回调地址     |

### 创建模板

在主题目录下，新建模板，如themes/mainload/layouts/partials/gitalk.html

```html
{{ if .Site.Params.enableGitalk }}
<div id="gitalk-container"></div>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
<script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
<script>
  const gitalk = new Gitalk({
    clientID: '{{ .Site.Params.Gitalk.clientID }}',
    clientSecret: '{{ .Site.Params.Gitalk.clientSecret }}',
    repo: '{{ .Site.Params.Gitalk.repo }}',
    owner: '{{ .Site.Params.Gitalk.owner }}',
    admin: ['{{ .Site.Params.Gitalk.owner }}'],
    id: location.pathname, // Ensure uniqueness and length less than 50
    distractionFreeMode: false // Facebook-like distraction free mode
  });
  (function() {
    if (["localhost", "127.0.0.1"].indexOf(window.location.hostname) != -1) {
      document.getElementById('gitalk-container').innerHTML = 'Gitalk comments not available by default when the website is previewed locally.';
      return;
    }
    gitalk.render('gitalk-container');
  })();
</script>
{{ end }}
```

修改主题模板模板layouts/_default/single.html，在{{ partial “comment.html” . }}的下一行，添加以下内容:

```
{{ partial "gitalk.html" . }}
```

###在github中 添加仓库

创建一个public的仓库，记住仓库名称，填写在下面的repo

### 添加配置

需要修改config.toml配置，注意repo添加自己的版本库地址，一般是username.github.io。
记得开启主题评论功能
```toml
[Params]
  enableGitalk = true

[Params.Gitalk]
    clientID = "xxx" # Your client ID
    clientSecret = "xxx" # Your client secret
    repo = "xbc.me" # 仓库名称
    owner = "geekwho11" # github 名字
    admin= "geekwho11" # Required. Github repository owner and collaborators. (Users who having write access to this repository)
    id= "location.pathname" # The unique id of the page.
    labels= "gitalk" # Github issue labels. If you used to use Gitment, you can change it
    perPage= 15 # Pagination size, with maximum 100.
    pagerDirection= "last" # Comment sorting direction, available values are 'last' and 'first'.
    createIssueManually= false # If it is 'false', it is auto to make a Github issue when the administrators login.
    distractionFreeMode= false # Enable hot key (cmd|ctrl + enter) submit comment.
```

### 大功告成