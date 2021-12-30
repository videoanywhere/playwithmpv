# Table of Contents

1.  [Installation](#org25786b0)
2.  [Preparation](#org28e0035)
3.  [Usage](#orgab901aa)
4.  [BTW](#org86b195e)

A server to support playing videos with mpv, which is suitable for bilibili.com based on Tampermonkey-script [Bilibili-Evolved](https://github.com/the1812/Bilibili-Evolved) .
It could be easily installed by `pip`.


<a id="org25786b0"></a>

# Installation

1.  Install [Python3](https://www.python.org/downloads/)/(>=3.8)/ and `pip`
2.  Run `pip install playwithmpv --user`

Maybe you want to use it to watch Bilibili vidoes, and you should do more &#x2013; Install some useful tools.


<a id="org28e0035"></a>

# Preparation

1.  Install [MPV](https://mpv.io/installation/) or [MPV<sub>lazy</sub>](https://github.com/hooke007/MPV_lazy) *(Amazing!)*
2.  Use mpv command line to play video url *(Prepare and test it works, maybe you should install some lib)*
3.  Install  [Bilibili-Evolved](https://github.com/the1812/Bilibili-Evolved) *(Also amazing)*
4.  Install “下载视频” 组件
5.  Install mpv-output-playlist 插件


<a id="orgab901aa"></a>

# Usage

1.  Run `playwithmpv` in console/terminal, which would start a server. (default `http://127.0.0.1:50000`)
2.  打开"下载视频“界面，"输出方式“中选择“MPV播放”，需配置mpv命令路径/（如果路径已加入环境变量，就不用改了）/，主机和端口默认是配置好的（ =<http://127.0.0.1:50000>=）
3.  Click "播放“. Actually MPV open a play list, and you can watch the expected eposide.


<a id="org86b195e"></a>

# BTW

Mpv is a so strong and free tool that can be easily used for many amazing files,
for instance, stream-video(no-download), free customization, amazing plugins and move enhacement support etc.
