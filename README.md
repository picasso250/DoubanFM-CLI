豆瓣电台 命令行版
=================

下载豆瓣红心歌曲的方法
----------------------------

执行

```
python download-fav.py
```

就会将红心歌曲下载到工作目录下的文件夹 `songs` 中。

会要求用户名和密码，觉得不安全的请去自行浏览源码 :smile:

在登录时会自动打开一个浏览器窗口，里面是验证码图片，请在命令行中输入。

每下载一首歌会停10秒钟，这个是为了防止豆瓣启动机器人反制策略。（500首歌大概需要2个小时下载完成）

基本上具有断点续传功能……

每首歌都有源信息JSON文件。

在线听歌的用法
---------------------------

`python doubanfm.py`

**频道列表:**

```
-3   红心
 0   私人
 1   华语
 2   欧美
 3   七零
 4   八零
 5   九零
 6   粤语
 7   摇滚
 8   民谣
 9   轻音乐
10   电影原声
```

**功能列表:**

跳过输入 `n`

加心输入 `f`

删歌输入 `d`

(并按Enter键)

**配置**

配置文件名：`doubanfm.config`

这个配置文件是**可选**的，也就是说完全可以没有。

```
[DEFAULT]
interval=30 ; 歌与歌之间的沉默间隙，单位：秒。默认值：0
email=xxx@gmail.com; 登录用户名
passwd=xxx; 登录密码
```

**依賴**

- `python-gst` ，如debian系需要 `sudo apt-get install python-gst0.10`
- `Python Imaging Library` ，如debian系 `sudo apt-get install python-imaging`
- `python-dateutil` ，如debian系 `sudo apt-get install python-dateutil`
- `imagemagick` 如debian系 `sudo apt-get install imagemagick`
- `gstreamer0.10-plugins`
- `gstreamer0.10-plugins-ugly`

**其他**

- 不支持 Windows 

