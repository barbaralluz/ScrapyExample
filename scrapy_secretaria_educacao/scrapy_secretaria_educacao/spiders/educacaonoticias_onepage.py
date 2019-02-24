# -*- coding: utf-8 -*-
import scrapy

from scrapy_secretaria_educacao.items import ScrapySecretariaEducacaoItem

class EducacaonoticiasSpider(scrapy.Spider):
    name = 'educacaonoticias_onepage'
    start_urls = ['http://www.educacao.sp.gov.br/noticias/']

    def parse(self, response):
        for article in response.css("article"):
            item = ScrapySecretariaEducacaoItem()
            item['article_type'] = article.css("span.desktop-only.categoria.orange > a::text").get()
            item['title'] = article.css("h2.title>a::text").get()
            item['url'] = article.css("h2.title>a::attr(href)").get()
            item['image'] = "N/A" if not article.css("img.wp-image-thumb.img-responsive.minha-classe::attr(src)").get() else article.css("img.wp-image-thumb.img-responsive.minha-classe::attr(src)").get() 
            item['date'] = article.css("span.date::text").get()

            yield item
