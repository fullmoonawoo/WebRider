import requests
from bs4 import BeautifulSoup


class WebRider:
    def __init__(self, url):
        self.source = requests.get(url)
        self.content = None
        self.data = None
        self.collection = {}
        self.results = {}

    def get_content(self):
        if self.source.status_code == 200:
            self.content = BeautifulSoup(self.source.content, 'html.parser')
            self.data = self.content.find_all(class_=["product-title", "product-price-value product-price-value-primary"])
            #self.data = self.content.select("div.product-title.product-price-value")

            for index in range(1, len(self.data)):
                if index < len(self.data) - 1:
                    try:
                        product = self.data[index].text.strip()
                        price = float(self.data[index + 1].text.strip()[0:5].replace(",", "."))
                    except ValueError:
                        continue
                    else:
                        self.collection[product] = price
        return self.collection

    def check_for(self, price_under, name=None):
        if name:
            for product, price in self.collection.items():
                if name in product and price <= price_under:
                    self.results[product] = price
                    print("PRODUCT:", product, "PRICE: ", price, "€")
        else:
            for product, price in self.collection.items():
                if price <= price_under:
                    self.results[product] = price
                    print("PRODUCT:", product, "PRICE: ", price, "€")

        #print(self.results.values())
        return self.results


# website = "https://sortiment.metro.sk/sk/napoje-tabak/alkohol/gin/6898c/?view_price=s"  # Gin's
website = "https://sortiment.metro.sk/sk/napoje-tabak/alkohol/whisky-whiskey/5014c/?view_price=s"  # Whiskey's
metro = WebRider(website)
metro.get_content()
#metro.check_for(price_under=20, name="Beefeater")
metro.check_for(price_under=15, name="Ballantine´s")
