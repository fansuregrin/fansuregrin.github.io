---
title: Archlinux下discover未找到应用程序后端解决办法
date: 2020-11-27 22:11:00
---
## 一、问题来源

Archlinux使用的包管理器名为`pacman`，`discover`是一个包管理的前端实现，但是我在安装了discover后发现里面是找不到任何应用，提示“找不到应用后端...”，问题出在了哪里呢？
![](https://img.fansuregrin.top/blog-img/2020-06-21_22-41.png#vwid=1313&vhei=769)

## 二、解决问题

在搜集了一番后，问题的原因就是少装了必要的包，我们将这些缺失的包安装后就可以正常使用discover了。

安装必要的包：

```
sudo pacman -S archlinux-appstream-data  packagekit-qt5  flatpak fwupd
```

安装完成后，就可以看到效果了：
![](https://img.fansuregrin.top/blog-img/2020-06-21_22-47.png#vwid=1274&vhei=830)

