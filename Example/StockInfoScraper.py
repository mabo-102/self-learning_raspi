from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, element


@dataclass(kw_only=True)
class StockInfo:
    name: str
    price: str
    change: str
    timestamp: str


class StockInfoScraper:
    def __init__(self, url: str, debug_mode: bool = False) -> None:
        self.url = url
        self.DEBUG = debug_mode

    def remove_span_tags(self, element: BeautifulSoup) -> None:
        for th_tag in element.find_all('th'):
            for span_tag in th_tag.find_all('span'):
                span_tag.decompose()

    def get_stock_columns(self, stock_row: element.Tag | element.NavigableString) -> StockInfo:
        stock_columns = stock_row.find_all_next('td')[:3]
        name = stock_row.text.strip()
        price = stock_columns[0].text.strip()
        change = stock_columns[1].text.strip()
        timestamp = stock_columns[2].text.strip()

        return StockInfo(name=name, price=price, change=change, timestamp=timestamp)

    def print_stock_info(self, stock_info: list[StockInfo]) -> None:
        for info in stock_info:
            print(f"{info.name}: {info.price} {info.change} {info.timestamp}")

    def get_stock_info(self, stock_list: list[str]) -> list[StockInfo]:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.remove_span_tags(soup)
        stock_info = []

        for stock_name in stock_list:
            stock_row = soup.find('th', string=stock_name)
            if stock_row:
                info = self.get_stock_columns(stock_row)
                stock_info.append(info)
            else:
                print(f"{stock_name} not found")

        if self.DEBUG:
            self.print_stock_info(stock_info)

        return stock_info

if __name__ == "__main__":
    from time import sleep

    url = "https://www.nikkei.com/markets/worldidx/"
    stock_list = ['TOPIX', 'ドル・円', 'NYダウ工業株30種（ドル）']

    scraper = StockInfoScraper(url, debug_mode=True)

    try:
        while True:
            stock_info: list[StockInfo] = scraper.get_stock_info(stock_list)
            sleep(300)
    except KeyboardInterrupt:
        print("Stoped Stock Info Scraper.")
