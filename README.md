# Aotu Role Automatic Generation Site

#### 介绍

本项目是送给各位凹凸世界迷的小礼物～

基于某大佬开发的凹凸世界作画AI（待那位大佬上传到托管平台就会放出项目链接）

本项目已经得到原作者的授权，并与原作者以相同的授权协议开放源代码

官方演示站点：[http://arags.acg.ghink.net](https://arags.acg.ghink.net)

本项目适合有一定计算机基础并且愿意折腾动手的小伙伴，如果只是为了下载QQ头像（误），我们的官方网站每周都会生成新的画作，可以直接前往下载哦

#### 软件架构

本项目使用Google的Tensorflow进行渲染
基于NVIDIA的CUDA计算与GAN生成对抗网络开发
使用Python进行核心部分开发


#### 硬件要求

1.  任意NVIDIA旗下支持CUDA计算的显卡
2.  主频高于2.0GHz的中央处理器
3.  大于等于8GB的运行内存
4.  不小于10MB/s读取速度的存储设备

示范：

1.  GTX660/2G
2.  E3-1230v3
3.  16G/DDR3
4.  西部数据Blue/2TB

#### 安装过程

1.  安装您的显卡对应的驱动程序（NVIDIA官网下载）
2.  安装本项目内的CUDAAPI包
3.  将本项目目内的cudnnlib包解压缩后放入CUDA安装目录内
4.  安装Python
5.  通过pip安装tensorflow_gpu-1.14.0（注意版本！1.14.0）
6.  通过pip安装numpy
7.  通过pip安装pillow

#### 参与贡献

1.  咕枣Rand（rand0mz）
2.  Bigsk（bigskcode）
