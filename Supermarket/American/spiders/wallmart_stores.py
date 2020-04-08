# -*- coding: utf-8 -*-
import scrapy
import  json

from scrapy import Request


class WallmartStoresSpider(scrapy.Spider):
    name = 'wallmart_stores'
    allowed_domains = ['walmart.com']
    base_url = 'https://www.walmart.com/store/finder/electrode/api/stores?singleLineAddr={}&distance=100'

    def start_requests(self):
        states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                  "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                  "Kansas", "Kentucky", "Louisiana", "Maine", "Montana", "Nebraska", "Nevada", "New Hampshire",
                  "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
                  "Oregon", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
                  "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                  "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        for state in states:
            url = self.base_url.format(state.strip())
            yield Request(url)


    def parse(self, response):
        json_data = json.loads(response.text)
        for data in json_data.get('payload').get('storesData').get('stores'):
            item = {}
            item['Id'] = data.get('id')
            item['Name'] = data.get('displayName')
            item['City'] = data.get('address').get('city')
            item['Street Address'] = data.get('address').get('address')
            item['Country'] = data.get('address').get('country')
            item['State'] = data.get('address').get('state')
            item['Phone'] = data.get('phone')
            item['Longitude'] = data.get('geoPoint').get('longitude')
            item['Latitude'] = data.get('geoPoint').get('latitude')
            item['Store URL'] = data.get('detailsPageURL')
            montofri_start = data.get('operationalHours', {}).get('monToFriHrs', {}).get('startHr')
            montofri_end = data.get('operationalHours', {}).get('monToFriHrs', {}).get('endHr')
            item['Monday'] = item['Tuesday'] = item['Wednesday'] = item['Thursday'] = item['Friday'] = montofri_start + ' - ' + montofri_end
            sat_start = data.get('operationalHours', {}).get('saturdayHrs', {}).get('startHr')
            sat_end = data.get('operationalHours', {}).get('saturdayHrs', {}).get('endHr')
            sun_start = data.get('operationalHours', {}).get('sundayHrs', {}).get('startHr')
            sun_end = data.get('operationalHours', {}).get('sundayHrs', {}).get('endHr')
            item['Saturday'] = sat_start + ' - ' + sat_end
            item['Sunday'] = sun_start + ' - ' + sun_end
            yield item