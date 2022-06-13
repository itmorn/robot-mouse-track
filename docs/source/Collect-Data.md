# 鼠标轨迹数据的收集

## 浏览器端
在代码仓库中，我们提供了一个前端页面，其使用document.onmousemove监听鼠标的移动，
当点击提交之后，会将收集到的鼠标轨迹序列通过Ajax的方式发送给服务器端，
对应代码为：[collect_data.html](https://github.com/itmorn/robot-mouse-track/blob/main/examples/collect_data.html)

## 服务器端
服务器端采用了flask部署了一个微服务，可以打印收集到的轨迹，方便我们进行记录和分析，
对应代码为：[server.py](https://github.com/itmorn/robot-mouse-track/blob/main/examples/server.py)





