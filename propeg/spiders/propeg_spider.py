from scrapy import Spider, Request
from propeg.items import PropegItem
import re


class PropegSpider(Spider):

	name = 'propeg_spider'
	allowed_domains = ['www.propertyfinder.eg']
	start_urls = ['https://www.propertyfinder.eg/en/search?c=1&ob=mr&page=1']

	def parse(self, response):

		text = response.xpath('//div[@class="property-header__list-count ge_resultsnumber"]/text()').extract_first()
		numpages = re.findall('\d+', text)
		numpages = round(int(numpages[0])/27)	

		result_urls = ['https://www.propertyfinder.eg/en/search?c=1&ob=mr&page='+ str(x) for x in range(1, numpages + 1)]

		for url in result_urls:
			print('PAGE NUM URL', url)
			yield Request(url=url, callback=self.parse_result_page)


	def parse_result_page(self, response):
		detail_urls = response.xpath('//div[@class="card-list__item"]/a/@href').extract()

		for url in ['https://www.propertyfinder.eg{}'.format(x) for x in detail_urls]:
			yield Request(url=url, callback=self.parse_detail_page)

	def parse_detail_page(self, response):

		propname = response.xpath('//h1[@class="property-header__title--detail"]/text()').extract_first()
		address = response.xpath('//h2[@class="property-header__sub-title"]/text()').extract_first()
		price = response.xpath('//span[@class="facts__content--price-value"]/text()').extract_first()
		proptype = response.xpath('//div[@class="facts__content"]/text()').extract_first()
		ref = response.xpath('//div[@class="facts__content"]/text()').extract()[1]
		bed = response.xpath('//div[@class="facts__content"]/text()').extract()[2]
		bath = response.xpath('//div[@class="facts__content"]/text()').extract()[3]
		sqm = response.xpath('//div[@class="facts__content"]/text()').extract()[4].strip()
		description = response.xpath('//div[@data-qs="text-trimmer"]/text()').extract()
		link = response.xpath('//link[@href]/@href').extract_first()
		json1 = response.xpath('//script[@type="application/ld+json"]/text()').extract()[0].strip()
		json2 = response.xpath('//script[@type="application/ld+json"]/text()').extract()[1].strip()

		
		item = PropegItem()
		item['propname'] = propname
		item['address'] = address
		item['price'] = price
		item['proptype'] = proptype
		item['ref'] = ref
		item['bed'] = bed
		item['bath'] = bath
		item['sqm'] = sqm
		item['description'] = description
		item['link'] = link
		item['json1'] = json1
		item['json2'] = json2

		yield item
