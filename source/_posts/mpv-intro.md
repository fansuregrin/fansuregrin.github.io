---
title: 简洁到不能再简洁的播放器：mpv
date: 2021-01-06 22:43:00
---
我一般喜欢比较简洁实用的软件，当然界面也不能过于丑陋。Potplayer和vlc是我用过的两个很不错的播放器，功能很多，从菜单栏就可以看出很多花样来。但今天说的这款播放器真的非常的简洁，因为打开它，甚至没有任何可以选择的菜单选项，甚至鼠标右键不能呼出任何选项。

![mpv仅提示将音视频文件拖入播放器播放](https://img.fansuregrin.top/blog-img/2020-12-31_19-24.png#vwid=834&vhei=449)

## 1.简介

> mpv是基于MPlayer和mplayer2的媒体播放器。它支持多种视频文件格式，音频和视频编解码器以及字幕类型。特殊输入URL类型可用于从磁盘文件以外的各种来源读取输入。根据平台，支持各种不同的视频和音频输出方法。

## 2.打开音视频文件和加载外挂字幕

### 一是直接从终端使用命令播放音视频文件

具体的使用规则如下：

```
Usage:   mpv [options] [url|path/]filename    #mpv  选项  参数（一般为音视频文件路径）

Basic options:
 --start=<time>    seek to given (percent, seconds, or hh:mm:ss) position
 --no-audio        do not play sound
 --no-video        do not play video
 --fs              fullscreen playback
 --sub-file=<file> specify subtitle file to use
 --playlist=<file> specify playlist file

 --list-options    list all mpv options
 --h=<string>      print options which contain the given string in their name
```

举个例子，播放一个mp4文件，并加载外挂srt字幕：

![mpv + “mp4文件路径” + “字幕参数=字幕文件路径”](https://img.fansuregrin.top/blog-img/2020-12-31_19-51.png#vwid=1542&vhei=356)

![终端显示详细播放信息](https://img.fansuregrin.top/blog-img/2020-12-31_19-52_1.png#vwid=1168&vhei=342)

![mpv启动播放视频并正确加载字幕](https://img.fansuregrin.top/blog-img/2020-12-31_19-53.png#vwid=1453&vhei=645)

### 二是直接打开mpv，将视频文件、字幕文件直接拖入mpv的窗口，简单粗暴。

## 3.交互

mpv虽然没有可见的菜单选项，但是可以通过键盘快捷键和鼠标来进行交互控制。

鼠标交互，可以播放、暂停，可以调节时间进度，可以控制音量（鼠标滚轮在音量标志上上下滚动可以调节音量大小），可以全屏等。

![](https://img.fansuregrin.top/blog-img/2020-12-31_20-04.png#vwid=1469&vhei=673)

- 鼠标左键双击：切换全屏开/关
- 鼠标右键单击：切换播放/暂停
- 鼠标滚轮上滚/下滚：时间进度向前/向后

键盘交互：

- v键：切换字幕可见性
- j/J键：向前或向后切换不同的字幕（如果你加载了多个外挂字幕或者视频内封装了多个字幕）
- ESC键：退出全屏
- q键：停止播放并退出
- [ 和 ] 键：将当前播放速度降低/提高10％
- { 和 } 键：将当前播放速度减半/加倍
- Backspace键（即退格键）：恢复到正常的播放速度
- space（即空格键）：播放/暂停
- / 和 * 键：音量减小和增加
- r 和 R键：向上或向下移动字幕
- s 和 S键：带字幕截图和不带字幕截图

具体介绍请看[mpv的文档](http://link.zhihu.com/?target=https%3A//mpv.io/manual/master/)。

本文视频：

<iframe src="//player.bilibili.com/player.html?aid=755962599&bvid=BV1m64y1Z7qG&cid=276210658&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="95%" height="600"> </iframe>

