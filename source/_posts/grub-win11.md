---
title: 为GRUB手动添加Windows 11引导选单
date: 2022-10-24 20:27:00
---
## 源起

入学后，老师给实验室新配了办公用的电脑，i5-12400 + RTX 2060 12G。但是，我还是习惯用自己的一套环境，于是就想着把它当成server来用，我只在我自己的笔记本上远程连接进行实验。说干就干，server当然选Linux作为系统，我喜欢ArchLinux这个发行版，就装它了。

## 难题

很奇怪，装完ArchLinux后grub识别不了Winsow11系统（对，在装Linux之前我已经装了Windows11系统）。排查一番后，我发现我安装了`os-prober`，也把`/etc/default/grub`中的`GRUB_DISABLE_OS_PROBER`选项的值设为了`False`。没办法，Google了一番后，只能手动添加一个Windows 11的启动选单。

## 解决方法

具体操作就是在`/etc/grub.d/40_custom`中添加以下文本：

```
menuentry 'Microsoft Windows 11' {
        insmod part_gpt
        insmod fat
        insmod chain
        search --fs-uuid --no-floppy --set=root xxxx-xxxx(此处改为windows系统的EFI分区的UUID）
        chainloader (${root})/EFI/Microsoft/Boot/bootmgfw.efi
}
```

**注意：上面一个UUID字段，需要按照自己的情况填写。** 我的Archlinux引导和Windows 11引导是放在了一个分区里面，在archlinux上显示是`/dev/nvme0n1p1`，你的可能与此类似，但也有可能会是`/dev/sdax`这个形式。然后用root用户执行`blkid`这条命令可以查看其UUID。输入输出如下：

```
# blkid /dev/nvme0n1p
/dev/nvme0n1p1: UUID="063B-8DD0" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="EFI system partition" PARTUUID="c32806b2-6cd1-477d-b7cf-aaa849f40a64"
```

然后，重新运行`grub-mkconfig -o /boot/grub/grub.cfg`即可。

