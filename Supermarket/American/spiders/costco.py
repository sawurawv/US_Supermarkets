# -*- coding: utf-8 -*-
import scrapy
import json


class CostcoSpider(scrapy.Spider):
    name = 'costco'
    allowed_domains = ['www.costco.com']
    base_urls = 'https://www.costco.com/AjaxWarehouseBrowseLookupView?langId=-1&storeId=10301&numOfWarehouses={}&populat' \
                'eWarehouseDetails=true&latitude={}&longitude={}&countryCode=US'




    def parse(self, response):
        json_data = json.loads(response.text)
        for data in json_data:
            if isinstance(data, dict): #checking if type is dict
                item = {}
                item['Id'] = data.get('stlocID')
                item['Name'] = data.get('locationName')
                item['City'] = data.get('city')
                item['Street Address'] = data.get('address1')
                item['Country'] = data.get('country')
                item['State'] = data.get('state')
                item['Phone'] = data.get('phone')
                item['Longitude'] = data.get('longitude')
                item['Latitude'] = data.get('latitude')
                item['Link'] = 'https://www.costco.com/warehouse-locations/'+item['city']+'-'+item['state']+'-'+item['Id']+'.html'
                mon_fri = data.get('warehouseHours')
                item['Monday'] = item['Tuesday'] = item['Wednesday'] = item['Thursday'] = item[
                    'Friday'] = mon_fri[0].split('F ')[-1]
                item['Saturday'] = data.get('warehouseHours')[1].split('. ')[-1]
                item['Sunday'] = data.get('warehouse')[-1].split('. ')[-1]
                yield item