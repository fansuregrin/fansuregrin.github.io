---
title: ArchLinux安装JavaFX并配置Intellij IDEA
date: 2022-08-09 20:55:00
---
## 1.源起

最近，我在Java的官方教程中测试一个[代码示例](https://docs.oracle.com/javase/8/javafx/get-started-tutorial/hello_world.htm)，示例用到了JavaFX。但在Intellij IDEA中，我配置好久才成功运行，所以记录下来，防止以后忘记。

## 2.我的编码环境

以下是我使用的编码环境：

```
OS: ArchLinux
IDE: Intellij Idea 2022.1.4 Community Edition
```

## 3.配置过程

下面讲述两种JDK版本的配置过程。

### (1) JDK 18

操作系统上需要安装的包有：

- jdk-openjdk (openjdk在archlinux发行版上的最新版，撰写本文时为`18.0.2.u9`)
- java-openjfx (openjfx在archlinux发行版上的最新版，撰写本文时为`18.0.2.u2`)

如果要可视化编辑`fxml`文件，需要安装下面这个包：

- javafx-scenebuilder (scenebuilder在archlinux发行版上的最新版，撰写本文时为`18.0.0`，此软件包不在archlinux的软件仓库中，需要从**AUR**上安装)。

`jdk-openjdk`的jdk所在路径如下所示：

```
/usr/lib/jvm/java-18-openjdk/
├── bin
├── conf -> /etc/java-openjdk
├── demo
├── include
├── jmods
├── legal -> /usr/share/licenses/java-openjdk
├── lib
├── man -> /usr/share/man
└── release
```

`java-openjfx`的库文件安装在`jdk-openjdk`的lib目录下：

```
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx-swt.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.base.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.controls.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.fxml.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.graphics.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.media.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.properties
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.swing.jar
java-openjfx /usr/lib/jvm/java-18-openjdk/lib/javafx.web.jar
```

`scenebuilder 18`所在路径如下所示：

```
/opt/scenebuilder/
├── bin
│   └── SceneBuilder
├── lib
│   ├── app
│   ├── libapplauncher.so
│   ├── runtime
│   ├── scenebuilder.desktop
│   ├── SceneBuilder.png
│   └── scenebuilder-SceneBuilder.desktop
└── share
    └── doc
```

首先，在Idea中新建一个项目，jdk选择jdk-18。
![](https://img.fansuregrin.top/blog-img/2022-08-09_19-34.png#vwid=1078&vhei=758)

然后，点击菜单栏的`File -> Project Structure`(快捷键Ctrl+Alt+Shift+S)，选择`Modules`，在`Dependencies`中添加依赖。选中openjfx的8个jar文件。
![](https://img.fansuregrin.top/blog-img/2022-08-09_19-48.png#vwid=1040&vhei=669)

![](https://img.fansuregrin.top/blog-img/2022-08-09_19-49.png#vwid=722&vhei=531)

应用更改后，在src目录下新建示例文件，把示例代码粘贴过来，编译通过，但是运行会报错！
![](https://img.fansuregrin.top/blog-img/2022-08-09_20-49.png#vwid=1324&vhei=857)

![](https://img.fansuregrin.top/blog-img/2022-08-09_19-49_1.png#vwid=910&vhei=265)

这时候，我们还需要点击菜单栏的`Run -> Edit Configurations`，添加`VM Options`（快捷键Alt+V）。添加的参数如下:

```
--module-path /usr/lib/jvm/java-18-openjdk/lib/javafx.base.jar:/usr/lib/jvm/java-18-openjdk/lib/javafx.controls.jar:/usr/lib/jvm/java-18-openjdk/lib/javafx.graphics.jar --add-modules javafx.controls
```

![](https://img.fansuregrin.top/blog-img/2022-08-09_19-50.png#vwid=1340&vhei=800)

![](https://img.fansuregrin.top/blog-img/2022-08-09_19-51.png#vwid=1065&vhei=685)

![](https://img.fansuregrin.top/blog-img/2022-08-09_19-53.png#vwid=1075&vhei=701)

应用更改后，再次运行，成功！
![](https://img.fansuregrin.top/blog-img/2022-08-09_19-53_1.png#vwid=1312&vhei=698)

### (2) jdk 8

