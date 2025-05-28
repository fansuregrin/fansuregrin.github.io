---
title: Archlinux上Nvidia和Intel双显卡切换方案记录
date: '2020-11-27 22:14:00'
categories:
  - - linux
tags:
  - linux
---
我的笔记本是Intel和Nvidia双显卡，在安装[Arch Linux](https://www.archlinux.org/)后，我一直在寻找双显卡切换方案。

## ArchLinux WIKI上的解决方案

遇到问题，自然去万能的wiki上找一找，官方wiki上提供了以下[几种方案](https://wiki.archlinux.org/index.php/NVIDIA_Optimus#Use_switchable_graphics)：

- Using PRIME render offload
- Using nouveau
- Using Bumblebee
- Using nvidia-xrun
- Using optimus-manager

![Use switchable graphics](https://img.fansuregrin.top/blog-img/2020-09-02_19-38-19.png#vwid=1049&vhei=540)

但作为一个新手，我也不知道哪种方案最有效，于是，我又陷入了困境......

## 遇到大佬的博客

在`等我稍后补充昵称`的[博客](https://www.bwsl.wang/arch/67.html)上，我看到他推荐`Using Optimus-manager`，于是我也决定来试一试。

### 1.安装Nvidia和Intel显卡驱动

1.[安装Nvidia显卡驱动](https://wiki.archlinux.org/index.php/NVIDIA)

2.[安装Intel显卡驱动](https://wiki.archlinux.org/index.php/Intel_graphics)
一般是`sudo pacman -S xf86-video-intel`

### 2.安装Optimus-manager

具体详情参照[Optimus-manager的GitHub页面](https://github.com/Askannz/optimus-manager)

我使用的是kde桌面环境，所以我的安装过程是

```
sudo pacman -S bbswitch 
yay -S optimus-manager  #需安装yay
yay -S optimus-manager-qt  #optimus-manager的qt前端，是可选择的，安装这个能通过gui来操作
```

![](https://img.fansuregrin.top/blog-img/2021-02-25_11-37.png#vwid=1199&vhei=311)

### 3.安装完成后的状态

安装完成后就可以在任务栏上找到`Optimus Manager Qt`这一项，右键可以切换显卡，之后会自动注销; 你也可以打开设置进行设置。
![](https://img.fansuregrin.top/blog-img/2020-09-13_14-45.png#vwid=503&vhei=495)
![](https://img.fansuregrin.top/blog-img/2020-09-13_14-47.png#vwid=803&vhei=591)

