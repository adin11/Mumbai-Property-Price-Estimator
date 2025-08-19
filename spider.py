# Scrapy code for extracting data using magicbricks backend API.

import scrapy
import json

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.magicbricks.com"]
    start_urls = ["https://www.magicbricks.com"]

    # Base API URL with placeholders for pagination  
    base_url = "https://www.magicbricks.com/mbsrp/propertySearch.html?category=S&propertyType=10002,10003,10021,10022,10001,10017&city=4320&page={}&groupstart={}&sortBy=premiumRecent"
 
    def start_requests(self):
        page = 1
        groupstart = 0  # Starts at 0, increases by 60
        
        print(f"Scraping page {page} with groupstart {groupstart}")

        # Send the first request
        yield scrapy.Request(url=self.base_url.format(page, groupstart), callback=self.parse, meta={'page': page, 'groupstart': groupstart})

    def parse(self, response):
        data = json.loads(response.text)  # Convert API response to JSON

        # Extract property details
        for item in data.get("resultList", []):
            print("Yielding item:", item)

            yield {
                "property_type": item.get("transactionTypeD"),
                "furnish_status": item.get("furnishedD"),
                'bedrooms': item.get('url',"").split('-')[0],
                'carpet_area': item.get('url',"").split('-')[2] if len(item.get("url", "").split("-")) > 2 else "0", #Ensures that if the url doesnt have enough parts after split, avoids causing an index error.
                "bathrooms":  item.get("bathD"),
                "balconies": item.get("balconiesD"),
                "poss_status":item.get("possStatusD"),
                "location":item.get("lmtDName"),
                "latitude":item.get("pmtLat"),
                "longitude":item.get("pmtLong"),
                "price":item.get("price")
            }

        # Handle pagination by increasing page & groupstart
        current_page = response.meta["page"]
        current_groupstart = response.meta["groupstart"]
        
        next_page = current_page + 1
        next_groupstart = current_groupstart + 60  # Move to next 60 listings
        
        if response.json().get('resultList'):
            next_url = self.base_url.format(next_page, next_groupstart)
            yield scrapy.Request(url=next_url, callback=self.parse, meta={'page': next_page, 'groupstart': next_groupstart})









