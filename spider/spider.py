# 简单爬虫实例
# 爬取熊猫直播TV 主播的昵称和人气

from urllib import request

class Spider():

    url = ''

    # __ 定义一个私有方法 
    # self 并实例方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # byte
        htmls = str(htmls, encoding = 'utf-8')

    

    def go(self):
        self.__fetch_content()

spider = Spider()
spider.go()