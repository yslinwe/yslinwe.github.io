---
title: "Vercel反向代理做CDN"
summary: Vercel反向代理做CDN
date: 2021-12-25
tags: ["Vercel"]
author: "YSL"
draft: false
weight: 2
---
1. node.js
2. 命令行
    ``` shell
    npm i -g vercel
    ```

    ``` shell
    vercel login
    ```
    `https://www.xxx.com`为代理网址
    ``` shell
    {
    "version": 2,
    "routes": [
        {"src": "/(.*)","dest": "https://www.xxx.com/$1"}
    ]
    }
    ```
    ```shell
    vercel -A xxx.json --prod
    ```