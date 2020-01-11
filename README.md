# Aotu Role Automatic Generation Site

#### 介绍

本项目是送给各位凹凸世界迷的小礼物～

基于某大佬开发的凹凸世界作画AI（待那位大佬上传到托管平台就会放出项目链接）

本项目已经得到原作者的授权，并与原作者以相同的授权协议开放源代码

官方演示站点：[http://arags.acg.ghink.net:10000](http://arags.acg.ghink.net:10000)

本项目内有较大的文件无法上传码云，可以前往官方演示站下载

本项目适合有一定计算机基础并且愿意折腾动手的小伙伴，如果只是为了下载QQ头像（误），我们的官方网站每周都会生成新的画作，可以直接前往下载哦

#### 软件架构

本项目使用Google的Tensorflow进行渲染
基于NVIDIA的CUDA计算与GAN生成对抗网络开发
使用Python进行核心部分开发


#### 硬件要求

1.  任意NVIDIA旗下支持CUDA计算的显卡
2.  主频高于2.0GHz的中央处理器
3.  大于等于6GB的运行内存
4.  不小于10MB/s读取速度的存储设备

示范：

1.  GTX660/2G
2.  E3-1230v3
3.  16G/DDR3
4.  西部数据Blue/2TB

#### 环境要求

1.  Windows操作系统（推荐Windows10）
2.  完整安装的NVIDIA显卡驱动
3.  完整安装的已经安装了cudnn的我们提供的CUDA API程序
4.  完整安装的Python
5.  完整安装的Python-tensorflow_gpu-1.14.0
6.  完整安装的Python-numpy
7.  完整安装的Python-pillow

#### 安装过程

1.  安装您的显卡对应的驱动程序（NVIDIA官网下载）
2.  安装本项目内的CUDAAPI包（演示站下载）
3.  将本项目目内的cudnnlib包解压缩后放入CUDA安装目录内
4.  安装Python
5.  通过pip安装tensorflow_gpu-1.14.0（注意版本！1.14.0）
6.  通过pip安装numpy
7.  通过pip安装pillow

#### 使用方法

单次生成：

1.  在draw.py文件内修改你想要的保存目录与角色（文件内有注释）
2.  打开draw.py等待运行，完成后会自动退出

多次生成：

1.  在draw.py文件中修改你想要的保存目录与角色（文件内有注释）
2.  在redo.py文件中修改你想要的生成次数（文件内有注释）
3.  打开redo.py等待运行，完成后会自动退出

网站全自动：

1.  安装并配置支持目录浏览的网站编译程序，如IIS/NGINX/Apache（本文档不做过多解释）
2.  在redo.py文件中修改你各角色你想要的生成次数
3.  在系统内设置定时任务执行（本文不做过多解释）

注意，官方提供的redo中有删除旧文档功能，如果不要可以将其删除
没有Python基础的，尽量不要改动目录结构，防止无法生成甚至误删文件

#### 参与贡献

1.  咕枣Rand（rand0mz）
2.  Bigsk（bigskcode）
