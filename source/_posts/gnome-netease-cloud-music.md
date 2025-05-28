---
title: Gnome桌面下网易云音乐无法显示托盘图标问题解决方案
date: '2022-09-12 21:58:00'
categories:
  - - linux
---
我在使用`Gnome`桌面环境过程中遇到一个问题，即打开官方的网易云音乐后Gnome的顶栏无法显示托盘图标。这倒不是因为`Gnome`官方取消了顶栏的托盘图标功能，因为我安装了相应的拓展——`gnome-shell-extension-appindicator`。

我起初怀疑是这个拓展的bug，但其实只要在网易云音乐的启动脚本中添加一行就可以解决这个问题。在archlinux下，网易云音乐的启动脚本位于`/opt/netease/netease-cloud-music/netease-cloud-music.bash`，其内容如下：

```
#!/bin/sh
HERE="$(dirname "$(readlink -f "${0}")")"
export LD_LIBRARY_PATH="${HERE}"/libs
export QT_PLUGIN_PATH="${HERE}"/plugins 
export QT_QPA_PLATFORM_PLUGIN_PATH="${HERE}"/plugins/platforms
export QT_QPA_PLATFORM=xcb
export LD_PRELOAD="${HERE}"/libnetease-patch.so

exec "${HERE}"/netease-cloud-music $@
```

在最后一行之前添加`unset DBUS_SESSION_BUS_ADDRESS`就能解决网易云音乐托盘图标不显示的问题。

