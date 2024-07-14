---
title: "vscode重复下载dotnet"
summary: vscode重复下载dotnet
date: 2021-05-21
tags: ["vscode重复下载dotnet"]
author: "YSL"
draft: false
weight: 2
---
### 修改.Net Install Tool的Setings文件：
```
"  dotnetAcquisitionExtension.existingDotnetPath": [

    {
        "extensionId": "ms-dotnettools.csharp",
        "path": "C:\\Program Files\\dotnet\\dotnet.exe"
    },
    {
        "extensionId": "ms-dotnettools.csdevkit",
        "path": "C:\\Program Files\\dotnet\\dotnet.exe"
    },
    {
        "extensionId": "visualstudiotoolsforunity.vstuc",
        "path": "C:\\Program Files\\dotnet\\dotnet.exe"
    }, 

],
```

