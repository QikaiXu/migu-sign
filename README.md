# 咪咕爱看签到

一点小羊毛

通过 github action 来实现自动签到（每天 50M 流量，每隔 5 天 0.38 元话费）

步骤：

1. 获取 cookie

   通过抓包咪咕爱看签到的请求，获取 cookie，其实只需要 cookie 中的 mToken 这个值就好了

2. 设置 cookie

   ![image-20210111220035535](README.assets/image-20210111220035535.png)

   在仓库中如图点击，然后添加一个名为 `COOKIE` 的变量，内容为获取到的 cookie

3. 随便发起一个 push 请求，可以修改一下 `README.md`，之后就会每小时进行一次签到。

