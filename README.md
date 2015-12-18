#Bing Wallpaper


它是我用来练习python编程的实践性作品。可以自动从[Bing.com](http://bing.com/)上获取主页背景，并设置为Ubuntu壁纸。

##运行

可以执行(需要python3)

```
python3 main.py
```

程序将自动把图片下载到

```
/home/用户名/Pictures/
```
以 **bingwallpaper+日期.jpg** 命名，并自动设置壁纸。

##自动执行
可以利用**shell**命令

```
crontab -e
```
定时运行。

具体用法可自行Google。
