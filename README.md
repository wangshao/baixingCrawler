#baixingCrawler
简介：
  基于Scrapy+MongoDB的租房帖爬虫

需要：
  MongoDB, Scrapy, Python, PyMongo
  
流程:
 各大城市的租房列表为起始页面， 获取列表中小标题的连接和下一页的连接后， 在这里之抓取前5页，进入详细页面抓取信息， 由PyMongo作为Connection。存储进MongoDB。
 
步骤：
启动Mongod进程
进入baixing目录 运行scrapy crawl baixing (前提 已安装scrapy 和 pymongo)
抓取。。。
结束后可用Mongo Shell 查看结果
