---
title: Anaconda使用笔记
date: '2023-02-14 23:15:00'
categories:
  - - 随笔
---
好记性不如烂笔头！本文记录我在使用`Anaconda3`过程中的一些笔记，以后遇到问题可以快速回来参考！

## 如何为虚拟环境设置环境变量？

- 【2022.2.14】
  用Anaconda的好处就是它能创建不同的虚拟环境，各个环境之间互不干扰。今晚，配置tensorflow环境时遇到错误如下：

````
ImportError: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/ubuntu/anaconda3/envs/tensorflow/lib/python3.10/site-packages/google/protobuf/pyext/_message.cpython-310-x86_64-linux-gnu.so) 
```bash
这个错误是在`Import tensorflow`时出现的。很明显，protobuf所要用的一个动态链接库找不到，当前python所搜寻的目录是`/lib`，而我们配置的虚拟环境所安装的库文件都在虚拟环境的目录下。譬如，我的就是`/home/ubuntu/anaconda3/envs/tensorflow/lib`。这时，就需要配置一个环境变量`LD_LIBRARY_PATH`。但是我只想让这个环境变量在激活我这个虚拟环境后才起作用，而不影响其他环境。这时候就需要为当前虚拟环境单独配置环境变量了。经过查询anacoda的文档，需要使用如下命令来设定。
```bash
conda env config vars set LD_LIBRARY_PATH=/home/ubuntu/anaconda3/envs/tensorflow/lib
````

