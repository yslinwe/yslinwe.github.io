---
title: "设置openwrt软件包"
summary: 设置openwrt软件包
date: 2022-12-11
tags: ["openwrt"]
author: "YSL"
draft: false
weight: 2
---

### 设置openwrt软件包

#### OPKG 基础配置

```
dest root /
dest ram /tmp
lists_dir ext /var/opkg-lists
option overlay_root /overlay
```

#### 发行版软件源

```
# add your custom package feeds here
#
# src/gz example_feed_name http://www.example.com/path/to/files
```

#### 自定义软件源

```
# add your custom package feeds here
#
# src/gz example_feed_name http://www.example.com/path/to/files
src/gz openwrt_core https://op.supes.top/targets/meson/meson8b/5.10.146
src/gz openwrt_base https://op.supes.top/packages/arm_cortex-a5_vfpv4/base
src/gz openwrt_packages https://op.supes.top/packages/arm_cortex-a5_vfpv4/packages
src/gz openwrt_luci https://op.supes.top/packages/arm_cortex-a5_vfpv4/luci
src/gz openwrt_routing https://op.supes.top/packages/arm_cortex-a5_vfpv4/routing
src/gz openwrt_kiddin9 https://op.supes.top/packages/arm_cortex-a5_vfpv4/kiddin9
```

