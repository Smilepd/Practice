# 使用代理IP访问百度，搜索文件中的词

#### 1、
* 安装chrome浏览器

#### 2、  
* 将chromedriver复制到/usr/local/bin目录下（mac的复制方法）（chrome浏览器和hromedriver版本要对应
https://www.cnblogs.com/maomao20/p/8024291.html ）

#### 3、
* 将需要读取的文件和ch.py放在同一目录下

#### 4、
* 在pycharm上运行test.py文件

##### 注释：
  1、可用的代理IP很多，但访问百度会长时间无响应，所以设置了响应时间为15s，超过响应时间则抛出异常，重新选取IP去访问
  
  2、取一次IP，每使用100次爬取的IP列表后更新一次IP列表
  
  aa
