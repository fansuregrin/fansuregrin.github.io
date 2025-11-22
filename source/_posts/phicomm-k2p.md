---
title: 都2025年了，Phicomm K2p还有人玩吗？
date: 2025-11-22 16:05:19
index_img: https://img.fansuregrin.top/blog-img/my_desktop.jpg
categories: 
  - - 随笔
tags:
  - Phicomm
---
> 都2025年了，当你从抽屉深处翻出那台泛着经典蓝光的 Phicomm K2P，或是偶然在某多平台瞥见它依然以50~70元的亲民价格悄然售卖--是否会产生一丝时空交错的恍？这台曾经被誉为“百元路由战神”的设备，在斐讯帝国崩塌多年后，竟依然在二手市场顽强流淌着数字血脉。
> 
> ——by DeepSeek

Phicomm 关门后，它的诸多遗物还在二手市场上流转，引起一些数码爱好者(垃圾佬)的亲睐。最近，在某多平台上淘了一件90.9999成新的 Phicomm K2p 无线路由器，抽空给刷上可玩性较高的 OpenWrt 系统。网络上关于Phicomm K2p 刷机的帖子和文章已经屡见不鲜，这里我只记录下个人刷机的过程，与其他文章中介绍内容的可能有差别。

## 一、介绍
首先，介绍下这款路由器的参数(Specifications)。这款路由生产时有4个不同的版本，分别为A1版、A2版、B1版和B2版，它们的主要差异在于使用的 CPU。A版使用的是 MediaTek 家的CPU，B版使用的是 Broadcom 家的CPU。我购入的是A2版，详细参数[^3]如下:
- CPU:MediaTek MT7621AT(880 MHz,2 cores)
- RAM:128 MiB(EtronTech EM6GC16EWKE-12H)
- FLA:16 MiB(MacronixMX25L12835FM21-10G)
- Wireless Chipset: 1x MediaTek MT7615DN(2X2T2R DBDC)
- Wireless Standard:802.11bgn(2.4GHz),802.11an/ac(5GHz)
- Wireless Speed:300Mbps for 2.4GHz,867Mbps for 5GHz

![phicomm_k2p_001](https://img.fansuregrin.top/blog-img/phicomm_k2p.jpg)

![phicomm_k2p_002](https://img.fansuregrin.top/blog-img/phicomm_k2p_02.jpg)

看完外观后，插电，LAN口连接网线到电脑上。Phicomm K2p 的默认IP地址是 `192.168.2.1`，浏览器访问后查看系统版本，不同的系统版本有不同的刷机方式（Hack方式）。我的这台系统版本是 `22.7.8.5`，需要开启系统的 telnet 功能，然后通过 telent 连接路由系统，刷入breed bootloader。后续是通过 breed 来刷入第三方固件。

![phicomm_k2p_sys_version](https://img.fansuregrin.top/blog-img/phicomm_k2p_sys_version.png)

## 二、刷机
### （1）启用系统的 Telnet
使用工具 RoutAckPro 打开 Phicomm K2p 的官方系统的 telnet，然后通过在自己电脑上的 telent 远程登入 phicomm K2p。我这里ip是 `192.168.3.1`，因为我手动改了 LAN 口的网段。[^1]

![RoutAckPro](https://img.fansuregrin.top/blog-img/RoutAckPro.png)

![telnet_to_phicomm_k2p](https://img.fansuregrin.top/blog-img/telnet_to_phicomm_k2p.png)

### （2）刷入breed bootloader
breed 是 [hackpascal](https://breed.hackpascal.net/) 大佬开发的一款 bootloader，被称为“不死鸟”，支持 k2p。这里使用的是 [iyc](https://iytc.net/wordpress/) 大佬的 breed 安装脚本[^4]。刷入 breed 后，路由器大概2~3分钟会自动复位重启。Breed的默认IP地址是 192.168.1.1，电脑需要设置下以太网的网络配置，子网掩码设置为 255.255.255.0，网关设置 192.168.1.1，电脑本机IP可以设置192.168.1.5，DNS可以随便填。然后，拔掉k2p电源，按住复位键不放手，插上电源，等待指示灯闪烁，即可放开复位键。然后，电脑浏览器中访问 `http://192.168.1.1` 即可打开 breed 界面。

![windows_static_ipv4_settings](https://img.fansuregrin.top/blog-img/windows_static_ipv4_settings.png)

![breed_web_interface](https://img.fansuregrin.top/blog-img/breed_web_interface.png)

### （3）刷入OpenWrt
OpenWrt 是一个开源的基于linux的可玩性较高的路由器操作系统，兼容 Phicomm K2p。到 OpenWrt 的官网中的 OpenWrt Firmware Selector 页面[^2]，可以选择 k2p 对应的固件系统进行下载。需要下载两个固件，一个kernel固件用于第一次初始化系统，另一个是 sysupgrade 固件用于后续升级系统。

![openwrt_firmware_selector](https://img.fansuregrin.top/blog-img/openwrt_firmware_selector.png)

OpenWrt 固件下载后，在breed控制台中选择“固件更新”，勾选“固件”选项，上传 OpenWrt kernel固件，闪存布局选择“公版0x50000”，勾选“自动重启”，然后点击“上传”，会跳转到新页面。在新页面中点击“更新”后，0penWrt kernel固件就自动刷写到 k2p中，等待2~3分钟路由器自动重启即可。

### （4）访问 0penWrt
OpenWrt 的默认 IP 是192.168.1.1，电脑浏览器访问，默认登录用户是 root，默认密码是root(也有可能是admin或者留空)。进入OpenWrt管理界面后，可以根据自己的需要进行配置。我这里是使用k2p 直接连接光猫，光猫改桥接，0penwrt中设置PPPOE拨号上网的。0penWrt官方软件源被墙最好改成清华大学的镜像源。默认系统语言只有 English，需要安装中文语言包，在“系统->软件包”中搜索“luci-i18n-base-zh-cn”安装即可。

![openwrt_web_interface](https://img.fansuregrin.top/blog-img/openwrt_web_interface.png)

## 后记
至此，Phicomm K2p 刷 OpenWrt 正式完成！

> 与这台K2P的搏斗终告结束。数小时的摸索无数次重启与变砖的担忧，都凝固在此刻后台稳定闪烁的指示灯里。过程虽煎熬，但当自由的OpenWrt界面在屏幕亮起，所有疲惫瞬间被一种微小的成就感取代。这不止是一次系统更新，更像为一位老将解开了封印。在2025年，花费几十元和一番心血，让经典重获新生--这本身，就是极客精神最朴素的浪漫。
> 
> —— by Deepseek

## 参考文献
[^1]: GoCloudK2PShuajiiaoChengV2.0.html http://help.gocloud.cn/nstallationGuide/FILES/GoCloudK2PShuajijiaoChengV2.0.html
[^2]: OpenWrt Firmware Selector https://firmware-selector.openwrt.org/?version=24.10.3&target=ramips%2Fmt7621&id=phicomm k2p
[^3]: Phicomm K2P-WikiDevi.Wi-Cat.Ru https://wikidevi.wi-cat.ru/Phicomm K2P
[^4]: 玉石云盘 http://woo.iytc.net/?dir=
