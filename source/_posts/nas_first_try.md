---
title: NAS初尝试
date: 2025-11-18 01:11:38
index_img: https://img.fansuregrin.top/blog-img/omv1.png
categories:
  - - 随笔
tags:
  - NAS
---
手上有一块1T的硬盘，里面存了不少资料，所以，利用空闲时间来打造个人NAS。

硬件配置列表：
- cpu：i38100t（159RMB）
- 主板：EX-BM360-V（109RMB）
- 内存条：金士顿 8g ddr4（119RMB）
- 电源：铠甲650 350w（68RMB）
- 散热：利民AX120 R SE（65RMB）
- 机箱：Acer U200 MATX（65RMB）
- 系统盘：WD Green 480g 固态（闲置）
- 存储盘：WDC 机械硬盘 1t （闲置）

![](https://img.fansuregrin.top/blog-img/nas.jpg)

选取的 CPU 为 [Intel(R) Core(TM) i3-8100T](https://www.intel.com/content/www/us/en/products/sku/129944/intel-core-i38100t-processor-6m-cache-3-10-ghz/specifications.html)，四核四线程，不支持超线程技术，基础频率 3.10 GHz，自带核心显卡 Intel® UHD Graphics 630，支持虚拟化技术，热设计功耗35W。选取的主板为 [ASUS EX-B360M-V](https://product.yesky.com/product/1048/1048487/param.shtml)，Micro ATX 板型，CPU插槽 LGA 1511，两个内存插槽，最大内存支持32G，一个 PCI-E X16 显卡插槽，两个 PCI-E X1 插槽。

![EX-B360M-V + i3-8100T](https://img.fansuregrin.top/blog-img/EX-B360M-V_with_cpu.jpg)

软件配置：
- Debian 12 bookworm
- OpenMediaVault（简称OMV）
- Docker
- Alist

![omv](https://img.fansuregrin.top/blog-img/omv3.png)
