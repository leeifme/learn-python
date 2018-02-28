# 简单爬虫实例
# 爬取熊猫直播TV 主播的昵称和人气

from urllib import request
import re

class Spider():

    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # __ 定义一个私有方法 
    # self 并实例方法

    # __fetch_content 获取所爬去网页结构
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # byte
        htmls = str(htmls, encoding = 'utf-8')
        return htmls   

    # __analysis 通过正则表达式 从网页结构中获取所需要的数据
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        # print(root_html[0])
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors

    # 精简数据 排除干扰数据
    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l,anchors)

    def __sort(self,anchors):
        anchors = sorted(anchors,key = self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def show(self,anchors):
        for anchor in anchors:
            print(anchor['name'] + '------' + anchor['number'])

    # 主控函数
    def go(self):
        htmls = self.__fetch_content() 
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        # print(anchors)\
        anchors = self.__sort(anchors)
        self.show(anchors)

spider = Spider()
spider.go()