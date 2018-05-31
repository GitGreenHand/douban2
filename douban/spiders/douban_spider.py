# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
	name = 'douban_spider'
	start_urls = ['https://www.douban.com/people/indiekid/photos']

	def parse(self, response):
		# 获取四个值
		#获取下一页的url

		object_list = response.xpath("//div[@class='albumlst']")
		for one_list in object_list:
			item=DoubanItem()
			# 1 获取图片的路径
			image = one_list.xpath("./a/img/@src").extract()
			#print("image",image)
			#print("@"*30)
			item['image']=image[0]
			# 2 获取图片的标题
			title = one_list.xpath("./div/div/a/text()").extract()
			#print("title",title)
			#print("#"*30)
			item['title']=title[0]
			title_url = one_list.xpath("./div/div/a/@href").extract()
			#print("title_url",title_url)
			#print("$"*30)
			item['title_url']=title_url[0]
			# 3 获取图片的描述
			info = one_list.xpath("./div/div[2]/text()").extract()
			#print("info",info)
			#print("%"*30)
			if len(info)!=0:
				item['info']=info[0]
			else:
				item['info']= ''
			# 4 获取细节信息
			detail = one_list.xpath("./div/span/text()").extract()
			#print("detail",detail)
			#print("^"*30)
			item['detail']=detail[0]
			yield item
		next_url=response.xpath("//span[@class='next']/a/@href").extract()
		print('next_url',next_url[0])
		print("*"*40)
		if (len(next_url))==0:
				#说明还没到最后一页
			pass
		else:
			yield scrapy.Request(next_url[0],callback=self.parse)

